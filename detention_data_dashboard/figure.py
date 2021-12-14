import plotly.express as px

def display_reg_plot(us_loc, df):

    #df = data_download(us_loc)
    
    fig = px.line(df, x=df['date'], y=[df['encounters'], df['removals'], df['arrests']],
              title = "Encounters, Removals, and Arrests in Region per FY",
              labels=dict(x="Fiscal Year", y="Number of Arrests"))
    fig.update_xaxes(title="Fiscal Year", nticks = 4)
    fig.update_yaxes(title="Number of Arrests")
    fig.update_layout(legend_title_text=None)

    return fig

def display_aor_arrests_plot(aor, df):
    fig = px.line(df, x=df['apprehension_date'], 
              y=df[aor], 
              title = "Arrests in AOR per FY",
              labels=dict(x="Fiscal Year", y="Number of Arrests"))
    fig.update_xaxes(title="Fiscal Year", nticks = 4)
    fig.update_yaxes(title="Number of Arrests")
    fig.update_layout(legend_title_text='AOR')

    return fig