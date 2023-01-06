import ingest_modules as mods

# Read in config file
config = mods.readConfig()

# Get file path
file_name = config['file']['file_path']
sheet_name = config['file']['sheet_name'].strip('"')

# Read file into datafame
df = mods.readExcelFile(file_name, sheet_name)

# Write file to Snowflake
table_name = 'outcomes'
mods.writeDFToSnowflake(df, table_name)

