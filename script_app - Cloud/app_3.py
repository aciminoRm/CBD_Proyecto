from pyspark.sql import SparkSession
from pyspark.sql.functions import col
#import sys

def print_developer_info(app_name):
    spark = SparkSession.builder.appName("PrintDeveloperInfo").getOrCreate()

    file_path = "Google-Playstore.csv"
    df = spark.read.option("header", "true").csv(file_path)

    app_info_df = df.filter(col("App Name") == app_name)

    if app_info_df.count() == 0:
        print(f"Nessuna informazione trovata per l'app '{app_name}'.")
        spark.stop()
        return

    selected_columns = ["App Name", "Developer Id", "Developer Website", "Developer Email"]
    developer_info_df = app_info_df.select(*selected_columns)

    developer_info_df.show(truncate=False)
    spark.stop()

#app_name_input = sys.argv[1]
app_name_input = "Instagram"
print_developer_info(app_name_input)
