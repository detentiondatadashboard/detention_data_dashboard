import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go # or plotly.express as px


app = dash.Dash()

fig_names = ['fig1', 'fig2']
fig_dropdown = html.Div([
    dcc.Dropdown(
        id='fig_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names],
        value=None
    )])
fig_plot = html.Div(id='fig_plot')
app.layout = html.Div([fig_dropdown, fig_plot])

@app.callback(
dash.dependencies.Output('fig_plot', 'children'),
[dash.dependencies.Input('fig_dropdown', 'value')])
def update_output(fig_name):
    return name_to_figure(fig_name)

def name_to_figure(fig_name):
    figure = go.Figure()
    if fig_name == 'fig1':
        figure.add_trace(go.Scatter(y=[4, 2, 1]))
    elif fig_name == 'fig2': 
        figure.add_trace(go.Bar(y=[2, 1, 3]))
    return dcc.Graph(figure=figure)

app.run_server(debug=True, use_reloader=False)