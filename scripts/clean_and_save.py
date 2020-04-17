import pandas as pd

def clean_and_save_country(country_name, df):
    """ Clean country data and save cleaned CSV
    
    Arguments:
        country_name {String} -- Name of the Country to save
        df {Dataframe} -- Pandas Dataframe
    """
    drop_columns = ['Lat', 
                    'Long', 
                    'Province/State']

    df.drop(columns=drop_columns, inplace = True)
    df_group = df.groupby(['Country/Region'])

    country = df_group.get_group(country_name)
    country.drop(columns = ['Country/Region'], inplace=True)
    country = country.agg(['sum'])
    country = country.T
    country.reset_index(level=0, inplace=True)
    country['index'] = pd.to_datetime(country['index'])
    country.rename(columns={'index': 'date'}, inplace=True)

    country.to_csv('../data/' + country_name + '_timeseries.csv', index=False)

def clean_and_save_worldwide(df):
    """Clean Worldwide infections and save to CSV
    
    Arguments:
        df {Dataframe} -- Pandas Dataframe to be cleaned.
    """
    drop_columns = ['FIPS',
                    'Lat', 
                    'Long_', 
                    'Combined_Key', 
                    'Admin2', 
                    'Province_State']

    df.drop(columns=drop_columns, inplace=True)

    df_cases = df.groupby(['Country_Region'], as_index=False).sum()
    df_cases.to_csv('../data/Total_cases_wordlwide.csv', index=False)

def clean_and_save_german_states(df):
    """Clean Data for fedaral states in germany. Save as CSV
    
    Arguments:
        df {Dataframe} -- PAndas Dataframe to be cleaned.
    """
    df.columns = ['Bundesland', 'Anzahl', 'diff', 'Pro_Tsd', 'Gestorben']
    df.drop(columns=['diff'], index=[16], inplace=True)
    df.to_csv('../data/cases_germany_states.csv', index=False)


if __name__ == '__main__':
    df_countries = pd.read_csv('../original_data/time_series_covid19_confirmed_global.csv')
    df_world_wide = pd.read_csv('../original_data/04-13-2020.csv')
    df_rki = pd.read_html('../original_data/Fallzahlen.html', decimal=',', thousands='.')
    df_de_states = df_rki[0]

    clean_and_save_country('Germany', df_countries)
    clean_and_save_worldwide(df_world_wide)
    clean_and_save_german_states(df_de_states)
    
    exit(0)