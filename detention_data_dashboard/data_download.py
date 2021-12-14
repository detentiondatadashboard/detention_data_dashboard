import pandas as pd

def data_download(us_loc):

    if us_loc == "West Coast":
        reg = ['LOS', 'SEA',  'SFR', 'SND']
    elif us_loc == "East Coast":
        reg = ['ATL', 'BAL', 'BOS', 'BUF', 'DET',  'MIA', 'NEW', 'NOL', 'NYC', 'PHI', 'WAS', 'HQ']
    elif us_loc == "Midwest":
        reg = ['CHI', 'SPM']
    elif us_loc == "Southwest":
        reg = ['DAL', 'DEN', 'ELP', 'HOU', 'PHO',  'SLC', 'SNA']
    elif us_loc == "All":
        reg = ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']
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
    columns_ = ['date', 'encounters', 'removals', 'arrests']

    d = []
    for i in ind:
        d.append([date[i], sum(enc.iloc[i]), sum(rem.iloc[i]), sum(arr.iloc[i])])
    df = pd.DataFrame(data = d, columns = columns_)

    return df