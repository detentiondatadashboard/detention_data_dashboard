# "Shut it down!" A detention data dashboard

[![Coverage Status](https://coveralls.io/repos/github/detentiondatadashboard/detention-data-dashboard/badge.svg?branch=main)](https://coveralls.io/github/detentiondatadashboard/detention-data-dashboard?branch=main)

## About the project

A dashboard and data repository of ICE immigration detention facilities and trends.

Data source: the [University of Washington's Center for Human Rights](https://jsis.washington.edu/humanrights/)

Through numerous FOIA requests and litigation, UW’s Center for Human Rights has obtained dozens of
datasets spanning roughly 2010-2020 related to ICE migrant detention facilities across the US. 
Datasets include variables on detention facilities, law enforcement, and bond rates.

## Software dependencies

- Python3
- For required python packages, see requirements.txt

## Directory structure

```bash
.
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── assets
│   └── style.css
├── data
│   ├── README.md
│   ├── arrest_dtypes.yaml
│   ├── arrests.csv
│   ├── arrests.csv.zip
│   ├── arrests_by_fy.csv
│   ├── encounter_dtypes.yaml
│   ├── encounters.csv
│   ├── encounters.csv.zip
│   ├── encounters_by_fy.csv
│   ├── ice-facilities.csv
│   ├── ice-facilities.csv.zip
│   ├── lat_long_det_fac_99.csv
│   ├── removal_dtypes.yaml
│   ├── removals.csv
│   ├── removals.csv.zip
│   └── removals_by_fy.csv
├── detention_data_dashboard
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── data_download.cpython-310.pyc
│   │   └── figure.cpython-310.pyc
│   ├── data_download.py
│   ├── data_exploration
│   │   ├── Arrests_descriptive_analysis.ipynb
│   │   ├── Encounters_Descriptive_Analysis.ipynb
│   │   ├── Geospatial_Plot.ipynb
│   │   ├── Removals_Descriptive_Analysis.ipynb
│   │   ├── maddie_exploration.ipynb
│   │   ├── plot_2.ipynb
│   │   └── test.png
│   ├── figure.py
│   └── tests
│       ├── __init__.py
│       ├── test_data_download.py
│       ├── test_figure.py
│       └── test_images
│           ├── ATL.png
│           ├── ATL1.png
│           ├── All.png
│           ├── All1.png
│           ├── BAL.png
│           ├── BAL1.png
│           ├── BOS.png
│           ├── BOS1.png
│           ├── BUF.png
│           ├── BUF1.png
│           ├── CHI.png
│           ├── CHI1.png
│           ├── DAL.png
│           ├── DAL1.png
│           ├── DEN.png
│           ├── DEN1.png
│           ├── DET.png
│           ├── DET1.png
│           ├── ELP.png
│           ├── ELP1.png
│           ├── East\ Coast.png
│           ├── East\ Coast1.png
│           ├── HOU.png
│           ├── HOU1.png
│           ├── HQ.png
│           ├── HQ1.png
│           ├── LOS.png
│           ├── LOS1.png
│           ├── MIA.png
│           ├── MIA1.png
│           ├── Midwest.png
│           ├── Midwest1.png
│           ├── NEW.png
│           ├── NEW1.png
│           ├── NOL.png
│           ├── NOL1.png
│           ├── NYC.png
│           ├── NYC1.png
│           ├── PHI.png
│           ├── PHI1.png
│           ├── PHO.png
│           ├── PHO1.png
│           ├── SEA.png
│           ├── SEA1.png
│           ├── SFR.png
│           ├── SFR1.png
│           ├── SLC.png
│           ├── SLC1.png
│           ├── SNA.png
│           ├── SNA1.png
│           ├── SND.png
│           ├── SND1.png
│           ├── SPM.png
│           ├── SPM1.png
│           ├── Southwest.png
│           ├── Southwest1.png
│           ├── WAS.png
│           ├── WAS1.png
│           ├── West\ Coast.png
│           └── West\ Coast1.png
├── doc
│   ├── software_design.md
│   └── tech_reviews
│       ├── Tech\ Review\ -\ Web\ Development\ Apps\ for\ Python.txt
│       └── Technology\ Review\ -\ Dashboards\ in\ Python.pptx
├── environment.yml
├── requirements.txt
├── runtime.txt
└── setup.py
```

## How to use

Access the dashboard online here: https://detentiondata.herokuapp.com/

## Dash app tutorial

[to be added]
