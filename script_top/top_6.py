from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def generate_top_Pegi18_csv(listaGeneros, output_path, number_choice):
    spark = SparkSession.builder.appName("TopPegi18").getOrCreate()

    file_path = "Google-Playstore.csv"
    df = spark.read.option("header", "true").csv(file_path)

    filtered_df = df.filter(col("Category").isin(listaGeneros) & ((col("Content Rating") == "Mature 17+") | (col("Content Rating") == "Adults only 18+")))
    sorted_df = filtered_df.orderBy(col("Maximum Installs").cast("int").desc())

    top_20_df = sorted_df.limit(number_choice)
    result_df = top_20_df.select("App Name", "Content Rating", "Maximum Installs")

    result_df.write.option("header", "true").csv(output_path, mode="overwrite")

    spark.stop()
    print(f"File CSV '{output_path}' generato con successo.")

print("Argomenti di input:", sys.argv)
listaGeneros = sys.argv[1].split(',')
number_choice = int(sys.argv[2])

if not listaGeneros:
    print("Specifica almeno un genere.")
    sys.exit(1)

output_path = "output_top/Top_Pegi18.csv"
generate_top_Pegi18_csv(listaGeneros, output_path, number_choice)

