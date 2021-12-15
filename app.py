import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from detention_data_dashboard.data_download import data_download_reg, data_download_arrests_aor, data_download_ice_detention
from detention_data_dashboard.figure import display_reg_plot, display_aor_arrests_plot, display_ice_detention_map

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title = "ICE Detention Data Dashboard"

fy = ['2015-10-01', '2016-10-01', '2017-10-01', '2018-10-01']

loc_list = ["East Coast", "West Coast", "Southwest", "Midwest", "All"]
aor_list = [
    'ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ',
    'LOS', 'MIA', 'NEW', 'NOL', 'NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC',
    'SNA', 'SND', 'SPM', 'WAS'
]
dataset_list = ['arrests', 'encounters', 'ice-facilities', 'removals']

clicks_1 = None
clicks_2 = None
clicks_3 = None
clicks_4 = None

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H1(children="ICE Detention Analytics",
                    className="header-title"),
            html.P(
                children="A dashboard and data repository of"
                " ICE detention trends and facilities across the US"
                " between 2010 and 2020",
                className="header-description",
            ),
            html.Div(id="data-bar",
                     children=[
                         dcc.Dropdown(
                             id='all-data',
                             options=[{
                                 'value': x,
                                 'label': x
                             } for x in dataset_list],
                             value=dataset_list[-1],
                         ),
                         html.Button("Download Dataset",
                                     id="btn_download_data"),
                         dcc.Download(id="download-dataset"),
                     ])
        ],
        className="header",
    ),
    html.Div(children=[
        html.Div(
            children=[
                dcc.Graph(id="ice_detention", ),
                dcc.RadioItems(id='color',
                               options=[{
                                   'value': 'blue',
                                   'label': 'blue'
                               }],
                               value='blue',
                               labelStyle={'display': 'inline-block'}),
                html.Button("Download CSV", id="btn_csv"),
                dcc.Download(id="download-dataframe-csv")
            ],
            className="card",
        ),
        dcc.Dropdown(
            id='us_loc',
            options=[{
                'value': x,
                'label': x
            } for x in aor_list],
            value=aor_list[0],
        ),
        html.Div(
            children=[
                dcc.Graph(id="fy_arrests", ),
                html.Button("Download CSV", id="btn_csv2"),
                dcc.Download(id="download-dataframe-csv2")
            ],
            className="card",
        ),
        dcc.Dropdown(
            id='dropdown1',
            options=[{
                'value': x,
                'label': x
            } for x in loc_list],
            value=loc_list[-1],
        ),
        html.Div(
            children=[
                dcc.Graph(id="plot2"),
                html.Button("Download CSV", id="btn_csv3"),
                dcc.Download(id="download-dataframe-csv3")
            ],
            className="card",
        ),
    ],
             className="wrapper"),
])


@app.callback(Output("ice_detention", "figure"), Input("color", "value"))
def return_ice_detention_fig(value):
    """
    pieces of code taken from https://www.kaggle.com/pavansanagapati/interactive-choropleth-point-maps-using-plotly?scriptVersionId=36440837&cellId=19
    """
    df = data_download_ice_detention()
    fig = display_ice_detention_map(df, 'blue')

    return fig


@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    global clicks_2

    if clicks_2 == n_clicks: return

    clicks_2 = n_clicks
    df = data_download_ice_detention()
    return dcc.send_data_frame(df.to_csv, "mydf.csv")


@app.callback(Output("fy_arrests", "figure"), [Input("us_loc", "value")])
def return_arrest_aor_plot(value):
    df = data_download_arrests_aor(value)
    fig = display_aor_arrests_plot(df)

    return fig


@app.callback(
    Output("download-dataframe-csv2", "data"),
    Input("btn_csv2", "n_clicks"),
    Input("us_loc", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, value):
    global clicks_3

    if clicks_3 == n_clicks: return

    clicks_3 = n_clicks
    df = data_download_arrests_aor(value)
    return dcc.send_data_frame(df.to_csv, "mydf.csv")


@app.callback(Output("plot2", "figure"), Input("dropdown1", "value"))
def return_reg_plot(value):
    df = data_download_reg(value)
    fig = display_reg_plot(df)

    return fig


@app.callback(
    Output("download-dataframe-csv3", "data"),
    Input("btn_csv3", "n_clicks"),
    Input("dropdown1", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, value):
    global clicks_4

    if clicks_4 == n_clicks: return

    clicks_4 = n_clicks
    df = data_download_reg(value)
    return dcc.send_data_frame(df.to_csv, "mydf.csv")


@app.callback(
    Output("download-dataset", "data"),
    Input("btn_download_data", "n_clicks"),
    Input("all-data", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, value):
    global clicks_1

    if clicks_1 == n_clicks: return

    clicks_1 = n_clicks
    return dcc.send_file('./data/' + value + '.csv.zip')


if __name__ == "__main__":
    app.run_server(debug=True)
