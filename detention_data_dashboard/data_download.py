"""
File containing relevant functions for obtaining and downloading data.
"""

import pandas as pd

def data_download_reg(us_loc):
    """
    Generates pandas dataframe of encounters, removals, and arrests per region per fiscal year

    parameters:
        us_loc: a string of a region in the US: West Coast, East Coast, Midwest, Southwest, or All
    returns:
        data_frame: a pandas dataframe containing information about encounters, removals, and
            arrests per region per fiscal year
    """
    if us_loc == "West Coast":
        reg = ['LOS', 'SEA',  'SFR', 'SND']
    elif us_loc == "East Coast":
        reg = ['ATL', 'BAL', 'BOS', 'BUF', 'DET',  'MIA', 'NEW', 'NOL', 'NYC', 'PHI', 'WAS', 'HQ']
    elif us_loc == "Midwest":
        reg = ['CHI', 'SPM']
    elif us_loc == "Southwest":
        reg = ['DAL', 'DEN', 'ELP', 'HOU', 'PHO',  'SLC', 'SNA']
    elif us_loc == "All":
        reg = ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS',
            'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA',
            'SFR', 'SLC', 'SNA', 'SND', 'SPM','WAS']
    else:
        raise NameError('Please enter in a valid US region')

    arrests_by_fy = pd.read_csv("./data/arrests_by_fy.csv")
    encounters_by_fy = pd.read_csv("./data/encounters_by_fy.csv")
    removals_by_fy = pd.read_csv("./data/removals_by_fy.csv")
    date = encounters_by_fy['event_date'].values.tolist()
    enc = encounters_by_fy[reg]
    rem = removals_by_fy[reg]
    arr = arrests_by_fy[reg]
    ind = arr.index.tolist()
    cols = ['date', 'encounters', 'removals', 'arrests']

    data_list = []
    for i in ind:
        data_list.append([date[i], sum(enc.iloc[i]), sum(rem.iloc[i]), sum(arr.iloc[i])])
    data_frame = pd.DataFrame(data = data_list, columns = cols)

    return data_frame

def data_download_arrests_aor(aor):
    """
    Generates pandas dataframe containing information about arrests per aor per fiscal year

    parameters:
        aor: a string of the area of responsibility region code
    returns:
        data_frame: a pandas dataframe containing information about arrests per aor per fiscal year
    """
    arrests = pd.read_csv("./data/arrests_by_fy.csv")
    aor_list = ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']

    if aor in aor_list:
        arrests_aor = arrests[aor]
        date = arrests['apprehension_date'].values.tolist()
        ind = arrests.index.tolist()
        cols = ['date', 'arrests']

        data_list = []
        for i in ind:
            data_list.append([date[i], arrests_aor[i]])
        data_frame = pd.DataFrame(data = data_list, columns = cols)

        return data_frame

    else:
         raise NameError('Please enter in a valid AOR')

    return data_frame

def data_download_ice_detention():
    data_frame = pd.read_csv("./data/lat_long_det_fac_99.csv")

    return data_frame

