# "Shut it down!" A detention data dashboard

[![Coverage Status](https://coveralls.io/repos/github/detentiondatadashboard/detention-data-dashboard/badge.svg?branch=main)](https://coveralls.io/github/detentiondatadashboard/detention-data-dashboard?branch=main)

## About the project

A dashboard and data repository of ICE detention facilities and their characteristics

Data source: All data courtesy of the [University of Washington's Center for Human Rights](https://jsis.washington.edu/humanrights/)

Through numerous FOIA requests and litigation, UW’s Center for Human Rights has obtained dozens of
datasets spanning roughly 2010-2020 related to ICE migrant detention facilities across the US. 
Datasets include variables on detention facilities, law enforcement, and bond rates.

## Software dependencies

- Python3
- For required python packages, see requirements.txt

## How to install


## Directory structure

detention-data-dashboard/
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── data
│   ├── README.md
│   ├── arrest_dtypes.yaml
│   ├── arrests.csv
│   ├── arrests_by_fy.csv
│   ├── encounter_dtypes.yaml
│   ├── encounters.csv
│   ├── ice-facilities.csv
│   ├── removal_dtypes.yaml
│   └── removals.csv
├── detention_data_dashboard
│   ├── __init__.py
│   ├── data_exploration
│   │   ├── Arrests_descriptive_analysis.ipynb
│   │   ├── Encounters_Descriptive_Analysis.ipynb
│   │   ├── Removals_Descriptive_Analysis.ipynb
│   │   └── maddie_exploration.ipynb
│   └── tests
│       ├── __init__.py
│       └── test_core.py
├── doc
│   ├── Tech\ Review\ -\ Web\ Development\ Apps\ for\ Python.txt
│   ├── Technology\ Review\ -\ Dashboards\ in\ Python.pptx
│   └── software_design.md
├── environment.yml
├── plot_downloads
│   └── test.png
├── requirements.txt
└── runtime.txt


## Dash app tutorial

![image](https://user-images.githubusercontent.com/91341415/145093061-76cfece2-e7af-47e9-b188-31eee1b8c960.png)
