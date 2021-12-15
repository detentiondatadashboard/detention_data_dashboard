import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from detention_data_dashboard.data_download import data_download_reg, data_download_arrests_aor, data_download_ice_detention
from detention_data_dashboard.figure import display_reg_plot, display_aor_arrests_plot, display_ice_detention_map

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title = "ICE Detention Data Dashboard"

fy = ['2015-10-01', '2016-10-01', '2017-10-01', '2018-10-01']

loc_list = ["East Coast", "West Coast", "Southwest", "Midwest", "All"]
aor_list = ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']
dataset_list = ['arrests', 'encounters', 'ice-facilities', 'removals']

color_list = ['red', 'blue', 'green']
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="ICE Detention Analytics", className="header-title"
                ),
                html.P(
                    children="A dashboard and data repository of"
                    " ICE detention trends and facilities across the US"
                    " between 2010 and 2020",
                    className="header-description",
                ),
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id='all-data',
                            options=[
                                {'value': x, 'label': x}
                                for x in dataset_list
                            ],
                            value=dataset_list[-1],
                        ),
                        html.Button("Download Dataset", id="btn_download_data"),  
                        dcc.Download(id="download-dataset"),                      
                    ]
                )
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[dcc.Graph(
                        id="ice_detention", config={"displayModeBar": False},
                    ),
                    dcc.RadioItems(
                    id='color', 
                    options=[{'value': x, 'label': x} 
                            for x in color_list],
                    value='blue',
                    labelStyle={'display': 'inline-block'}),

                    html.Button("Download CSV", id="btn_csv"),
                    dcc.Download(id="download-dataframe-csv"),
                    html.Button("Download Image", id="btn_image"),
                    dcc.Download(id="download-image")],
                    className="card",
                ),
                dcc.Dropdown(
                    id='us_loc', 
                    options=[{'value': x, 'label': x} 
                            for x in aor_list],
                    value=aor_list[0],
                ),
                html.Div(
                    children=dcc.Graph(
                        id="fy_arrests",
                    ),
                    className="card",
                )],
                
            className="wrapper"),
            
        
                
        html.Div(
            children = [
                dcc.Dropdown(
                    id='dropdown1',
                    options=[{'value': x, 'label': x} 
                            for x in loc_list],
                    value=loc_list[-1],
                ),
                html.Div(
                    children=dcc.Graph(
                        id="plot2"
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)
@app.callback(
    Output("ice_detention", "figure"),
    Input("color", "value"))

def return_ice_detention_fig(value): 
    """
    pieces of code taken from https://www.kaggle.com/pavansanagapati/interactive-choropleth-point-maps-using-plotly?scriptVersionId=36440837&cellId=19
    """
    df = data_download_ice_detention()
    #lat = df['latitude']
    #ong_ = df['longitude']
    fig = display_ice_detention_map(df, value)

    return fig

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "mydf.csv")

@app.callback(
    Output("download-image", "data"),
    Input("btn_image", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "./plot_downloads/test.png"
    )

@app.callback(
    Output("fy_arrests", "figure"),
    [Input("us_loc", "value")])

def return_arrest_aor_plot(value):
    df = data_download_arrests_aor(value)
    fig = display_aor_arrests_plot(df)

    return fig

@app.callback(
    Output("plot2", "figure"),
    Input("dropdown1", "value")
    )

def return_reg_plot(value):
    df = data_download_reg(value)
    fig = display_reg_plot(df)

    return fig


@app.callback(
    Output("download-dataset", "data"),
    Input("btn_download_data", "n_clicks"),
    Input("all-data", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, value):
    file = './data/' + value + '.csv'
    dt = pd.read_csv(file, sep='|')
    return dcc.send_data_frame(dt.to_csv, "dataset.csv")


if __name__ == "__main__":
    app.run_server(debug=True)
