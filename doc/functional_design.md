# User Stories:

## Researchers:
- Trends in migrant detention facilities over the last 10 years to answer questions about the impact of opening and closing detention facilities
- Visualize certain trends, pull our data and the way that we have organized it so that they can work with it
- Interacting via a webpage 
- More technical experience

## Policymakers/Advocates:
- Visualize trends in order to get summary level statistics in order to make broad policy decisions
- A way to output visualizations
- Easy drop down menus to change relevant variables (years, citizenship, various demographics)
- Less technical, make it very very clear and easy to use


## Technician/Data Scientist:
- Add to or edit data that already exists on the portal
- Add to or edit visualization formatting and displays
- Add to or edit language on the user interface

# Functional Design: 

## Researchers:

- Include drop down boxes for charts so that users can download figures with formatting options
- Have a separate tab for exporting spreadsheets with options for data format
- Allow users to download the data they want:
  - All the data
  - Prespecified subsets of the data
  - Data that you visualized through the interface
- Allow users to download visualizations:
  - Tables
  - Interactive plots downloaded as still figures

# Component Design

Dataframes:
- Facilities data
- Bond data
- Enforcement data (Encounters, Arrests, Removals)
- Demographic data


Dropdown options:
- Chart type (map, bar, line, etc.)
- Time (year, month, day)
- Geographic levels (aor, state, county)
- Variables


