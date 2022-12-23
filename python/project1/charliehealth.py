# Import pandas
import pandas as pd
import pyodbc
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

file_name = "C:\Temp\outcomes_data.xlsx"

dfs = pd.read_excel(file_name, sheet_name='Outcomes Data')
df = pd.DataFrame(dfs, columns= ['ParticipantID', 'PreHLCRefYN', 'POSTHLCRefYN', 'NewPreHLCAdmYN', 'POST_HLCAdmYN', 'PreER', 'POST_ER', 'DischargeMonth', 'DischargeCode', 'IntakeMonth', 'Age', 'AgeGroup', 'Gender', 'Transgender', 'SexOrient', 'SexOrientBinary', 'Therapist', 'IntakeDate', 'DateDischarge', 'SessionsAttend', 'WeeksAttend', 'SessionsAttend2', 'PrePHQScore', 'NewPreABASI_Think', 'NewPreABASI_Solution', 'NewPostABASI_Think', 'NewPostABASI_Solution', 'PreERWhy', 'POST_ERWhy', 'PreSelfHarmBinary', 'PostSelfHarmBinary', 'PreASQ1Wished', 'PreASQ2FamBetter', 'PreASQ3ThoughtsWk', 'PreASQ5ThoughtsNow', 'PostASQ1Wished', 'PostASQ2FamBetter', 'PostASQ3ThoughtsWk', 'PostASQ5ThoughtsNow', 'HLCAdm_PreCH', 'PreERNum', 'PrePHQ1', 'PrePHQ2', 'PrePHQ3', 'PrePHQ4', 'PrePHQ5', 'PrePHQ6', 'PrePHQ7', 'PrePHQ8', 'PrePHQ9', 'PostPHQ1', 'PostPHQ2', 'PostPHQ3', 'PostPHQ4', 'PostPHQ5', 'PostPHQ6', 'PostPHQ7', 'PostPHQ8', 'PostPHQ9', 'PreCRAFFTQ1DaysDrink', 'PreCRAFFTQ2DaysMarij', 'PreCRAFFTQ3DaysOther', 'PreCRAFFTQ4DaysRelax', 'PreCRAFFTQ5DaysAlone', 'PreCRAFFTQ6DaysForget', 'PreCRAFFTQ7DaysTrouble', 'PreCRAFFTQ8ToldStop', 'PreCRAFFTQ9Car', 'PostCRAFFTQ1DaysDrink', 'PostCRAFFTQ2DaysMarij', 'PostCRAFFTQ3DaysOther', 'PostCRAFFTQ4DaysRelax', 'PostCRAFFTQ5DaysAlone', 'PostCRAFFTQ6DaysForget', 'PostCRAFFTQ7DaysTrouble', 'PostCRAFFTQ8ToldStop', 'PostCRAFFTQ9Car'])

#https://bf02095.east-us-2.azure.snowflakecomputing.com/
account_identifier = 'bf02095.east-us-2.azure'
user = 'NJKROES'
password = 'bo7Cu8cyET4e'

conn_string = f"snowflake://{user}:{password}@{account_identifier}"
engine = create_engine(conn_string)


connection = engine.connect()
#results = connection.execute('select current_version()').fetchone()
#print(results[0]) 

df.to_sql("Outcomes", engine, schema='raw', index=False, if_exists='append')

connection.close()
engine.dispose()
