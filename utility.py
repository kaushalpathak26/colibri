#create directory to store file and  delta table loaction
dbutils.fs.mkdirs("/FileStore/Colibri/raw/turbine_data");
dbutils.fs.mkdirs("/FileStore/Colibri/landing/turbine_metrics")
dbutils.fs.mkdirs("/FileStore/Colibri/silver/turbine_data")
dbutils.fs.mkdirs("/FileStore/Colibri/bronze/turbine_data")
dbutils.fs.mkdirs("/FileStore/Colibri/gold/turbine_metrics")
#path where delta tables will be stored
raw_path = "/FileStore/Colibri/landing/turbine_metrics/"
bronze_path = "/FileStore/Colibri/bronze/turbine_data/"
silver_path = "/FileStore/Colibri/silver/turbine_data/"
gold_path = "/FileStore/Colibri/gold/turbine_metrics/"
