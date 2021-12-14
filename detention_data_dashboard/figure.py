import plotly.express as px

def display_aor_plot(us_loc):

    df = data_download(us_loc)
    
    fig = px.line(df, x=df['date'], y=[df['encounters'], df['removals'], df['arrests']],
              title = "Encounters, Removals, and Arrests in Region per FY",
              labels=dict(x="Fiscal Year", y="Number of Arrests"))
    fig.update_xaxes(title="Fiscal Year", nticks = 4)
    fig.update_yaxes(title="Number of Arrests")
    fig.update_layout(legend_title_text=None)

    return fig