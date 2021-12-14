import pandas as pd

def data_download(us_loc):

    if us_loc == "West Coast":
        aor = ['LOS', 'SEA',  'SFR', 'SND']
    elif us_loc == "East Coast":
        aor = ['ATL', 'BAL', 'BOS', 'BUF', 'DET',  'MIA', 'NEW', 'NOL', 'NYC', 'PHI', 'WAS', 'HQ']
    elif us_loc == "Midwest":
        aor = ['CHI', 'SPM']
    elif us_loc == "Southwest":
        aor = ['DAL', 'DEN', 'ELP', 'HOU', 'PHO',  'SLC', 'SNA']
    elif us_loc == "All":
        aor = ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']
    else:
        raise NameError('Please enter in a valid US region')

    arrests_by_fy = pd.read_csv("./detention_data_dashboard/data/arrests_by_fy.csv")
    encounters_by_fy = pd.read_csv("./detention_data_dashboard/data/encounters_by_fy.csv")
    removals_by_fy = pd.read_csv("./detention_data_dashboard/data/removals_by_fy.csv")
    date = encounters_by_fy['event_date'].values.tolist()
    enc = encounters_by_fy[aor]
    rem = removals_by_fy[aor]
    arr = arrests_by_fy[aor]
    ind = arr.index.tolist()
    columns_ = ['date', 'encounters', 'removals', 'arrests']

    d = []
    for i in ind:
        d.append([date[i], sum(enc.iloc[i]), sum(rem.iloc[i]), sum(arr.iloc[i])])
    df = pd.DataFrame(data = d, columns = columns_)

    return df
