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

    arrests_by_fy = pd.read_csv("./data/arrests_by_fy.csv")
    encounters_by_fy = pd.read_csv("./data/encounters_by_fy.csv")
    removals_by_fy = pd.read_csv("./data/removals_by_fy.csv")
    date = encounters_by_fy['event_date'].values.tolist()
    enc = encounters_by_fy[aor_].to_numpy().flatten()
    rem = removals_by_fy[aor_].to_numpy().flatten()
    arr = arrests_by_fy[aor_].to_numpy().flatten()
    columns_ = ['date', 'encounters', 'removals', 'arrests']
    data_ = []
    for i in range(len(date)):
        data_.append([date[i],enc[i],rem[i],arr[i]])
    temp = pd.DataFrame(data = data_, columns = columns_)
