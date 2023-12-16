from pyspark.sql import SparkSession
from pyspark.sql.functions import col
#import sys

def print_app_info(app_name):
    # Crea una sessione Spark
    spark = SparkSession.builder.appName("PrintAppInfo").getOrCreate()

    file_path = "Google-Playstore.csv" 
    df = spark.read.option("header", "true").csv(file_path)

    app_info_df = df.filter(col("App Name") == app_name)

    if app_info_df.count() == 0:
        print(f"Nessuna informazione trovata per l'app '{app_name}'.")
        spark.stop()
        return

    selected_columns = ["App Name", "Content Rating", "Price", "Currency"]
    app_info_df = app_info_df.select(*selected_columns)

    app_info_df.show(truncate=False)
    spark.stop()

#app_name_input = sys.argv[1]
app_name_input = "Akinator VIP"
print_app_info(app_name_input)

