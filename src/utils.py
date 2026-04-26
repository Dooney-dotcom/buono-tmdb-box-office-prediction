import pandas as pd
import ast

def parse_json(x):
    '''Parses a JSON string into a Python object. If the input is already a list, it returns it as is. If the input is NaN or an empty string, it returns an empty list.'''
    if pd.isna(x) or x == '':
        return []
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        return ast.literal_eval(x)
    return []

def extract_from_json(df, column, key):
    '''Extracts values from a JSON string in a specified column of a DataFrame. It applies a function to each element in the column, parsing the JSON and extracting the value associated with the specified key from each dictionary in the list. If the key is not found in a dictionary, it is skipped. The result is a list of values for each row in the DataFrame.'''
    return df[column].apply(
        lambda x: [d[key] for d in parse_json(x) if isinstance(d, dict) and key in d]
    )

def extract_role_from_crew(df, role):
    '''Extracts the name of a specific role (e.g., Director) from the 'crew' column of a DataFrame. The 'crew' column is expected to contain JSON strings representing lists of dictionaries, where each dictionary contains information about a crew member, including their job. The function parses the JSON, checks for the specified role, and returns the name of the crew member with that role. If the role is not found or if the 'crew' column is NaN, it returns None.'''
    temp = df.copy()
    return temp['crew'].apply(
        lambda x: next(
            (m['name'] for m in ast.literal_eval(x) if m.get('job') == role),
            None
        ) if pd.notna(x) else None
    )

def extract_dictionaries(df):
    '''Extracts specific information from JSON strings in various columns of a DataFrame. It creates new columns for each type of information (e.g., 'belongs_to_collection', 'genres', 'production_companies', etc.) by applying the 'extract_from_json' function to the corresponding columns. Additionally, it extracts the director's name from the 'crew' column using the 'extract_role_from_crew' function. The resulting DataFrame contains the original data along with the newly extracted information in separate columns.'''
    temp = df.copy()

    temp['belongs_to_collection'] = extract_from_json(temp, 'belongs_to_collection', 'name')
    temp['genres'] = extract_from_json(temp, 'genres', 'name')
    temp['production_companies'] = extract_from_json(temp, 'production_companies', 'name')
    temp['production_countries'] = extract_from_json(temp, 'production_countries', 'name')
    temp['spoken_languages'] = extract_from_json(temp, 'spoken_languages', 'iso_639_1')
    temp['Keywords'] = extract_from_json(temp, 'Keywords', 'name')
    temp['cast'] = extract_from_json(temp, 'cast', 'name')

    # Crew column contains different roles, we will extract only directors
    temp['director'] = extract_role_from_crew(temp, 'Director')
    temp['crew'] = extract_from_json(temp, 'crew', 'name')

    return temp

def parse_release_dates(df):
    '''Parses the 'release_date' column of a DataFrame, which contains date strings in the format '%m/%d/%y'. It converts these strings into datetime objects. If the year in the parsed date is greater than 2019, it assumes that the date is in the 20th century and subtracts 100 years from it. This is done to correct for any dates that may have been misinterpreted as being in the 21st century due to the two-digit year format. The resulting DataFrame contains the original data with the 'release_date' column converted to datetime objects.'''
    df = df.copy()
    df['release_date'] = pd.to_datetime(
        df['release_date'],
        format='%m/%d/%y'
    )

    df.loc[df['release_date'].dt.year > 2019, 'release_date'] -= pd.DateOffset(years=100)

    return df

def fix_dataset(df):
    '''Applies a series of transformations to a DataFrame to clean and prepare the data for analysis. It first creates a copy of the input DataFrame to avoid modifying the original data. Then, it calls the 'extract_dictionaries' function to extract specific information from JSON strings in various columns and create new columns for that information. After that, it calls the 'parse_release_dates' function to convert the 'release_date' column from string format to datetime objects, correcting any misinterpreted dates as needed. Finally, it returns the cleaned and transformed DataFrame ready for further analysis or modeling.'''
    df = df.copy()
    df = extract_dictionaries(df)
    df = parse_release_dates(df)
    return df
