from sqlalchemy import create_engine
import pandas as pd
import configparser

# Configuration file with Snowflake connection settings
config = configparser.ConfigParser()
config.read('python\project1\config.ini')

file_name = "C:\Temp\outcomes_data.xlsx"
columns= ['ParticipantID', 'PreHLCRefYN', 'POSTHLCRefYN', 'NewPreHLCAdmYN', 'POST_HLCAdmYN', 'PreER', 'POST_ER', 'DischargeMonth', 'DischargeCode', 'IntakeMonth', 'Age', 'AgeGroup', 'Gender', 'Transgender', 'SexOrient', 'SexOrientBinary', 'Therapist', 'IntakeDate', 'DateDischarge', 'SessionsAttend', 'WeeksAttend', 'SessionsAttend2', 'PrePHQScore', 'NewPreABASI_Think', 'NewPreABASI_Solution', 'NewPostABASI_Think', 'NewPostABASI_Solution', 'PreERWhy', 'POST_ERWhy', 'PreSelfHarmBinary', 'PostSelfHarmBinary', 'PreASQ1Wished', 'PreASQ2FamBetter', 'PreASQ3ThoughtsWk', 'PreASQ5ThoughtsNow', 'PostASQ1Wished', 'PostASQ2FamBetter', 'PostASQ3ThoughtsWk', 'PostASQ5ThoughtsNow', 'HLCAdm_PreCH', 'PreERNum', 'PrePHQ1', 'PrePHQ2', 'PrePHQ3', 'PrePHQ4', 'PrePHQ5', 'PrePHQ6', 'PrePHQ7', 'PrePHQ8', 'PrePHQ9', 'PostPHQ1', 'PostPHQ2', 'PostPHQ3', 'PostPHQ4', 'PostPHQ5', 'PostPHQ6', 'PostPHQ7', 'PostPHQ8', 'PostPHQ9', 'PreCRAFFTQ1DaysDrink', 'PreCRAFFTQ2DaysMarij', 'PreCRAFFTQ3DaysOther', 'PreCRAFFTQ4DaysRelax', 'PreCRAFFTQ5DaysAlone', 'PreCRAFFTQ6DaysForget', 'PreCRAFFTQ7DaysTrouble', 'PreCRAFFTQ8ToldStop', 'PreCRAFFTQ9Car', 'PostCRAFFTQ1DaysDrink', 'PostCRAFFTQ2DaysMarij', 'PostCRAFFTQ3DaysOther', 'PostCRAFFTQ4DaysRelax', 'PostCRAFFTQ5DaysAlone', 'PostCRAFFTQ6DaysForget', 'PostCRAFFTQ7DaysTrouble', 'PostCRAFFTQ8ToldStop', 'PostCRAFFTQ9Car']

# read in file and sheet to pandas datafame
dfs = pd.read_excel(file_name, sheet_name='Outcomes Data')
df = pd.DataFrame(dfs, columns)

# convert columns to upper case
df.columns=map(str.upper, df.columns)


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

# connect to Snowflake
connection = engine.connect()

# write dataframe to Snowflake
df.to_sql("OUTCOMES", engine, index=False, if_exists='append')
