import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash import callback_context

df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()

app = dash.Dash(__name__)
server = app.server

df_csv = df

app.layout = html.Div([
    html.P("Candidate:"),
    dcc.RadioItems(
        id='candidate', 
        options=[{'value': x, 'label': x} 
                 for x in candidates],
        value=candidates[0],
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="choropleth"),
    html.Button("Download CSV", id="btn_csv"),
    dcc.Download(id="download"),
    html.Button("Download Figure", id="btn_fig")
])


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
    Output("download", "data"),
    Input("btn_csv", "n_clicks"),
    Input("btn_fig", "n_clicks"),
    prevent_initial_call=True,
)
def download(btn_csv, btn_fig):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btn_csv' in changed_id:
        return dcc.send_data_frame(df_csv.to_csv, "mydf.csv")
    elif 'btn_fig' in changed_id:
        return dcc.send_file("./plot_downloads/test.png")
    else:
        msg = "Click Download!"
        return html.Div(msg)


if __name__ == "__main__":
    app.run_server(debug=True)
