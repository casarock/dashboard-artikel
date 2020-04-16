import pandas as pd

def clean_and_save_country(country_name, df):
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
    country['date'] = pd.to_datetime(country['index'])
    country.drop(columns = ['index'], inplace=True)
    country.to_csv(country_name + '_timeseries.csv')

def clean_and_save_worldwide(df):
    drop_columns = ['FIPS',
                    'Lat', 
                    'Long_', 
                    'Combined_Key', 
                    'Admin2', 
                    'Province_State']

    df.drop(columns=drop_columns, inplace=True)

    df_cases = df.groupby(['Country_Region'], as_index=False).sum()
    df_cases.to_csv('Total_cases_wordlwide.csv')

def clean_and_save_german_states(df):
    df.columns = ['Bundesland', 'Anzahl', 'diff', 'Pro_Tsd', 'Gestorben']
    df.drop(columns=['diff'], index=[16], inplace=True)
    df.to_csv('cases_germany_states.csv')

if __name__ == '__main__':

    df_countries = pd.read_csv('../time_series_covid19_confirmed_global.csv')
    df_world_wide = pd.read_csv('../04-13-2020.csv')
    df_rki = pd.read_html('../Fallzahlen.html', decimal=',', thousands='.')
    df_de_states = df_rki[0]

    clean_and_save_country('Germany', df_countries)
    clean_and_save_worldwide(df_world_wide)
    clean_and_save_german_states(df_de_states)
    

    exit(0)