from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum
import sys

def generate_top_developer_stats(listaGeneros, output_path, number_choice):
    spark = SparkSession.builder.appName("TopDeveloperStats").getOrCreate()

    file_path = "Google-Playstore.csv"
    df = spark.read.option("header", "true").csv(file_path)

    filtered_df = df.filter(col("Category").isin(listaGeneros))
    filtered_df = filtered_df.filter(col("Developer Id").isNotNull() & (col("Developer Id") != ""))

    developer_stats_df = filtered_df.groupBy("Developer Id").agg(
        count("App Name").alias("Numero di App"),
        sum(col("Maximum Installs").cast("long")).alias("Somma Maximum Installs")
    )

    sorted_df = developer_stats_df.orderBy(col("Somma Maximum Installs").desc())
    top_df = sorted_df.limit(number_choice)

    top_df.write.option("header", "true").csv(output_path, mode="overwrite")

    spark.stop()
    print(f"File CSV '{output_path}' generato con successo.")


print("Argomenti di input:", sys.argv)
listaGeneros = sys.argv[1].split(',')
number_choice = int(sys.argv[2])
if not listaGeneros:
    print("Specifica almeno un genere.")
    sys.exit(1)

output_path = "output_top/Top_Developer_Stats.csv"
generate_top_developer_stats(listaGeneros, output_path, number_choice)

