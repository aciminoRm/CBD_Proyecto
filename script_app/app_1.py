from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def generate_app_info(app_name):
    spark = SparkSession.builder.appName("AppInfo").getOrCreate()

    file_path = "Google-Playstore.csv" 
    df = spark.read.option("header", "true").csv(file_path)

    app_info_df = df.filter(col("App Name") == app_name)

    if app_info_df.count() == 0:
        print(f"Nessuna informazione trovata per l'app '{app_name}'.")
        spark.stop()
        return

    selected_columns = ["App Name", "App Id", "Category", "Rating", "Rating Count", "Installs", "Size", "Developer Id",
                         "Released", "Last Updated"]
    app_info_df = app_info_df.select(*selected_columns)

    app_info_df.show(truncate=False)
    spark.stop()


app_name_input = sys.argv[1]
generate_app_info(app_name_input)


