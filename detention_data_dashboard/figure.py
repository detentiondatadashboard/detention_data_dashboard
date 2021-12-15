"""
File containing relevant functions for generating figures.
"""

import plotly.express as px
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

    raise NameError('Please enter in a dataframe')

def display_ice_detention_map(data_frame, color):
    """
    Generates plotly map of ice detention centers in the US

    parameters:
        data_frame: a pandas dataframe containing latitudes, longitudes, and addresses of the
        ice detention centers in the us
        color: a string with the color of the dots on the map
    returns:
        fig: a plotly map of ice detention centers in the US
    """

    fig = go.Figure(
        data=go.Scattergeo(
            lon = data_frame['long'],
            lat = data_frame['lat'],
            text = data_frame['address'],
            mode = 'markers',
            marker_color = color,
            ))
    fig.update_layout(
        title = 'ICE Detention Facilities across the US',
        geo_scope='usa',
    )
    return fig
