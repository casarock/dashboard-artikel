import plotly.express as px

def get_wordlwide_cases(df):
    """ Get plotly express figure for world wide cases
    
    Arguments:
        df {Datafram} -- Pandas Dataframe for the cases
    
    Returns:
        figure -- Ploty Figure
    """
    fig_geo_ww = px.scatter_geo(df, 
                     locations="Country_Region",
                     hover_name="Country_Region",
                     hover_data=['Confirmed', 'Recovered', 'Deaths'],
                     size="Confirmed",
                     locationmode='country names',
                     text='Country_Region',
                     scope='world',
                     labels={
                         'Country_Region':'Land',
                         'Confirmed':'Bestätigte Fälle',
                         'Recovered':'Wieder geheilt',
                         'Deaths':'Verstorbene',
                     },
                     size_max=35,
                     template='ggplot2',)

    fig_geo_ww.update_layout(
        title_text = 'Bestätigte Infektionen weltweit',
        title_x = 0.5,
        height = 600,
        geo = dict(
            showframe = False,
            showcoastlines = True,
            projection_type = 'equirectangular'
        )
    )

    return fig_geo_ww

def get_country_names(df):
    """Get all country names in time series dataframe
    
    Arguments:
        df {Dataframe} -- Pandas Dataframe with time series data
    
    Returns:
        List - List with all Names.
    """
    cols = list(df.columns)
    cols.pop(0) # remove Date
    return cols

def get_german_barchart(df):
    """Get Barchart with infections from germanies federal states
    
    Arguments:
        df {Dataframe} -- Pandas Datafram with german data
    
    Returns:
        Figure -- Plotly Figure
    """
    df.sort_values(by=['Anzahl'], ascending=True, inplace=True)
    fig_fs = px.bar(df, x='Anzahl', 
                y='Bundesland',
                hover_data=['Gestorben'],
                height=450, 
                orientation='h',
                labels={'Gestorben':'Bereits verstorben'},
                template='ggplot2')

    fig_fs.update_layout(xaxis={
                       'title': 'Anzahl der Infektionen'
                     },
                     yaxis={
                       'title': '',
                     },
                     title_text='Infektionen in Deutschland')
    return fig_fs

def get_german_piechart(df):
    """Get Pie Chart for german infections
    
    Arguments:
        df {Dataframe} -- Pandas Dataframe
    
    Returns:
        Figure -- Plotly Figure with Pie Chart
    """
    fig_fs_pie = px.pie(df, 
                    values='Anzahl', 
                    names='Bundesland', 
                    title='Verteilung auf Bundesländer', 
                    template='ggplot2')
    
    return fig_fs_pie

def get_worldwide_facts(df):
    """Get summary of world wide datas
    
    Arguments:
        df {Dataframe} -- Pandas Dataframe
    
    Returns:
        List -- List with data
    """
    totals = df.sum()
    return {
        'total': totals.Confirmed,
        'deaths': totals.Deaths,
        'recovered':totals.Recovered,
        'active':totals.Active,
    }


def get_lineplot(country, df):
    """Get a Lineplot for a country
    
    Arguments:
        country {String} -- Country
        df {Dataframe} -- Dataframe with country data
    
    Returns:
        Figure -- Plotly Figure with a Line plot.
    """
    fig_line = px.line(df, 
                 x="Date", 
                 y=country)

    fig_line.update_layout(xaxis_type='date',
                  xaxis={
                      'title': 'Datum'
                  },
                  yaxis={
                      'title': 'Infektionen',
                      'type': 'linear',
                  },
                  height= 450,
                  title_text='Infektionen: ')
    return fig_line