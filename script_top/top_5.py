from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp, datediff, current_date
from pyspark.sql.types import TimestampType

import sys

def generate_top_lastUpdated_csv(listaGeneros, output_path, number_choice):
    spark = SparkSession.builder.appName("ToplastUpdated").getOrCreate()

    file_path = "Google-Playstore.csv"
    df = spark.read.option("header", "true").csv(file_path)

    filtered_df = df.filter(col("Category").isin(listaGeneros))
    filtered_df = filtered_df.filter(col("Last Updated").isNotNull() & (col("Last Updated") != ""))
    date_format = "MMM d, yyyy"
    filtered_df = filtered_df.withColumn("Last Updated", unix_timestamp(col("Last Updated"), date_format).cast(TimestampType()))
    filtered_df = filtered_df.withColumn("DateDifference", datediff(current_date(), col("Last Updated")))
    sorted_df = filtered_df.orderBy("DateDifference")

    top_df = sorted_df.limit(number_choice)
    result_df = top_df.select(
        "App Name",
        "Released",
        col("Last Updated").cast("date").alias("Last Updated"),
        "DateDifference"
    )

    result_df.write.option("header", "true").csv(output_path, mode="overwrite")

    spark.stop()
    print(f"File CSV '{output_path}' generato con successo.")

print("Argomenti di input:", sys.argv)
listaGeneros = sys.argv[1].split(',')
number_choice = int(sys.argv[2])

if not listaGeneros:
    print("Specifica almeno un genere.")
    sys.exit(1)

output_path = "output_top/Top_lastUpdated.csv"
generate_top_lastUpdated_csv(listaGeneros, output_path, number_choice)
