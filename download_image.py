import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px

FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)

df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()

external_stylesheets = [dbc.themes.BOOTSTRAP, FONT_AWESOME]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets

app.layout = dbc.Container(
	[
	
	html.Div([
    html.P("Candidate:"),
    dcc.RadioItems(
        id='candidate', 
        options=[{'value': x, 'label': x} 
                 for x in candidates],
        value=candidates[0],
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="choropleth"),
    ]),

	dbc.Button(id='btn',
            children=[html.I(className="fa fa-download mr-1"), "Download"],
            color="info",
            className="mt-1"
        ),

        dcc.Download(id="download-component"),
    ],
    className='m-4'
)


@app.callback(
    [Output("choropleth", "figure"), Output("download-component", "data")];
    [Input("candidate", "value"), Input("btn", "n_clicks")],
    prevent_initial_call=True
)
def func(n_clicks):
    return dcc.send_file(
        "./dash_docs/assets/images/gallery/dash-community-components.png"
    )

def display_choropleth(candidate):
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)