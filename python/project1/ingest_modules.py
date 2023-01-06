import configparser
import pandas as pd
from sqlalchemy import create_engine

def readConfig():
    config = configparser.ConfigParser()
    config.read('python\project1\config.ini')

    return config


def readExcelFile(file_name, sheet_name):
    # read in file and sheet to pandas datafame
    dfs = pd.read_excel(file_name, sheet_name)
    df = pd.DataFrame(dfs)

    # convert columns to upper case
    df.columns=map(str.upper, df.columns)

    return df

def writeDFToSnowflake(df, table_name):
    # Read in config file
    config = readConfig()

    # get Snowflake connection parameters from config file
    account_identifier = config['snowflake']['account_identifier']      
    user = config['snowflake']['user']
    password = config['snowflake']['password']
    database_name = config['snowflake']['database_name']
    schema_name = config['snowflake']['schema_name']
    warehouse = config['snowflake']['warehouse']
    role_name= config['snowflake']['role_name']

    # construct connection string
    conn_string = f"snowflake://{user}:{password}@{account_identifier}/{database_name}/{schema_name}?warehouse={warehouse}&role={role_name}"
    engine = create_engine(conn_string)

    # write dataframe to Snowflake
    df.to_sql(table_name, engine, index=False, if_exists='replace')

    # cleanup
    engine.dispose()

