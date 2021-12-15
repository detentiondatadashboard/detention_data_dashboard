"""
File containing relevant functions for generating figures.
"""

import plotly.express as px
import plotly
import plotly.graph_objects as go

def display_reg_plot(data_frame):
    """
    Generates plotly figure of encounters, removals, and arrests per region per fiscal year

    parameters:
        data_frame: a pandas dataframe containing information about encounters, removals, and
        arrests per region per fiscal year
    returns:
        fig: a plotly line plot figure of the encounters, removals, and arrests per region per
        fiscal year
    """
    if str(type(data_frame)) == "<class 'pandas.core.frame.DataFrame'>":
        fig = px.line(data_frame, x=data_frame['date'], y=[data_frame['encounters'],
                  data_frame['removals'], data_frame['arrests']],
                  title = "Encounters, Removals, and Arrests in Region per FY",
                  labels=dict(x="Fiscal Year", y="Total"))
        fig.update_xaxes(title="Fiscal Year", nticks = 4)
        fig.update_yaxes(title="Total")
        fig.update_layout(legend_title_text=None)

        return fig

    else:
        raise NameError('Please enter in a dataframe') 


def display_aor_arrests_plot(data_frame):
    """
    Generates plotly figure of arrests per aor per fiscal year

    parameters:
        data_frame: a pandas dataframe containing information about arrests per aor per fiscal year
    returns:
        fig: a plotly line plot figure of the arrests per aor per fiscal year
    """
    if str(type(data_frame)) == "<class 'pandas.core.frame.DataFrame'>":
        fig = px.line(data_frame, x=data_frame['date'],
                  y=data_frame['arrests'],
                  title = "Arrests in AOR per FY",
                  labels=dict(x="Fiscal Year", y="Total Arrests"))
        fig.update_xaxes(title="Fiscal Year", nticks = 4)
        fig.update_yaxes(title="Total Arrests")
        fig.update_layout(legend_title_text='AOR')

        return fig

    else:
        raise NameError('Please enter in a dataframe')

def display_ice_detention_map(df, color):

    fig = go.Figure(
        data=go.Scattergeo(
            lon = df['long'],
            lat = df['lat'],
            text = df['address'],
            mode = 'markers',
            marker_color = color,
            ))
    fig.update_layout(
        title = 'Ice Detention Centers',
        geo_scope='usa',
    )
    return fig

