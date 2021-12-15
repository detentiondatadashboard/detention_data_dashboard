# "Shut it down!" A detention data dashboard

[![Coverage Status](https://coveralls.io/repos/github/detentiondatadashboard/detention-data-dashboard/badge.svg?branch=main)](https://coveralls.io/github/detentiondatadashboard/detention-data-dashboard?branch=main)

## About the project

A dashboard and data repository of ICE immigration detention facilities and trends.

Access the dashboard online here: https://detentiondata.herokuapp.com/

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

## Tutorials

Video tutorial on how to use use online dashboard: https://youtu.be/6wihXwGH7GE

Video tutorial on how to pip install: https://youtu.be/fuL_vFVhTDs
