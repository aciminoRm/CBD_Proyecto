from pyspark.sql import SparkSession
from pyspark.sql.functions import col
#import sys

def find_apps_by_developer(developer_name):
    spark = SparkSession.builder.appName("FindAppsByDeveloper").getOrCreate()

    file_path = "Google-Playstore.csv"  # Aggiungi il percorso corretto se necessario
    df = spark.read.option("header", "true").csv(file_path)

    apps_df = df.filter((col("Developer Id") == developer_name) | (col("Developer Email") == developer_name))

    if apps_df.count() == 0:
        print(f"Nessun developer trovato con il nome '{developer_name}'.")
        spark.stop()
        return

    result_df = apps_df.select("Developer Id", "App Name", "Category", "Rating", "Maximum Installs")
    sorted_df = result_df.orderBy(col("Maximum Installs").cast("int").desc())

    sorted_df.show(truncate=False)
    spark.stop()

#developer_name = sys.argv[1]
developer_name = "Google LLC"

find_apps_by_developer(developer_name)


