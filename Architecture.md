# Overview
The task provided was to ingest a provided Excel file of outcomes data using Python to a SQL database, transform and populate a data model and analyze the data.

## Architecture
To complete this, the technologies used were:
- Python
- Snowflake
- DBT

![Overview](docs\overview.png)

## Python
To ingest the excel file into Snowflake, the following packages were implemented:
- SQLAlchemy 
- pandas
- configparser
- openpyxl


 openpyxl is used to read in the XLSX file and sheet into a pandas dataframe. SQLAlchemy is then used to create a connection to Snowflake and then the `to_sql` function of the pandas dataframe is used to write the dataframe to Snowflake.

## Snowflake
Snowflake is setup into three different zones in order to be consistent with the ELT approach:
- Raw
- Transformed
- Marts

The data from the Excel file is ingested into the **Raw** zone in Snowflake in its raw form.

The next stage in the **Transform** zone which contains views that read from the **Raw** zone and transforms the data.

The last stage is the **Marts** zone which is the published layer where data is structured for analysis.

## DBT
DBT is used to perform the transformations inside of Snowflake. The project is setup using DBT's recommended approach for project structure. The layers are:
- Staging
- Intermediate
- Marts

**Staging** and **Intermediate** models are persisted as views and the **Marts* models are persisted as tables.



