import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import detention_data_dashboard
import plotly.express as px
import pandas as pd
from dash import callback_context

df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title = "ICE Detention Data Dashboard"

fy = ['2015-10-01', '2016-10-01', '2017-10-01', '2018-10-01']

loc = ["East Coast", "West Coast", "Southwest", "Midwest", "All"]

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
            ],
            className="header",
        ),
        html.Div(
            children=[
                dcc.RadioItems(
                id='candidate', 
                options=[{'value': x, 'label': x} 
                    for x in candidates],
                value=candidates[0],
                labelStyle={'display': 'inline-block'}
                ),
                html.Div(
                    children=[dcc.Graph(
                        id="choropleth", config={"displayModeBar": False},
                    ),
                    html.Button("Download CSV", id="btn_csv"),
                    dcc.Download(id="download-dataframe-csv"),
                    html.Button("Download Image", id="btn_image"),
                    dcc.Download(id="download-image")],
                    className="card",
                ),
                dcc.RadioItems(
                    id='us_loc', 
                    options=[{'value': x, 'label': x} 
                            for x in loc],
                    value=loc[0],
                    labelStyle={'display': 'inline-block'}
                ),
                html.Div(
                    children=dcc.Graph(
                        id="fy_arrests",
                    ),
                    className="card",
                ),
            ],
            className="wrapper",

        ),
        html.Div(
            children = [
                dcc.Dropdown(
                    id='dropdown1',
                    options=[{'label': 'SEA', 'value': 'SEA'} ,
                        {'label': 'ATL','value': 'ATL'}],
                    value='dish',
                ),
                dcc.Graph(id="plot2")
                ]

            )

    ]
)
@app.callback(
    Output("choropleth", "figure"), 
    [Input("candidate", "value")])

def display_choropleth(candidate):
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

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
    Output("plot2", "figure"),
    Input("dropdown1", "value")
    )

data_download(us_loc)

display_aor_plot(us_loc)

if __name__ == "__main__":
    app.run_server(debug=True)
