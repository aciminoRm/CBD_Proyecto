from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def generate_top_rating_csv(listaGeneros, output_path, number_choice):
    spark = SparkSession.builder.appName("TopRating").getOrCreate()

    file_path = "Google-Playstore.csv"
    df = spark.read.option("header", "true").csv(file_path)

    filtered_df = df.filter(col("Category").isin(listaGeneros))
    sorted_df = filtered_df.orderBy(col("Maximum Installs").cast("int").desc())

    top2_df = sorted_df.limit(number_choice * 5)
    sorted_top2_df = top2_df.orderBy(col("Rating").cast("float").desc())
    top_df = sorted_top2_df.limit(number_choice)

    result_df = top_df.select("App Name", "Rating", "Rating Count", "Maximum Installs")

    result_df.write.option("header", "true").csv(output_path, mode="overwrite")

    spark.stop()
    print(f"File CSV '{output_path}' generato con successo.")

print("Argomenti di input:", sys.argv)
listaGeneros = sys.argv[1].split(',')
number_choice = int(sys.argv[2])
    
if not listaGeneros:
    print("Specifica almeno un genere.")
    sys.exit(1)

output_path = "output_top/Top_Rating.csv"
generate_top_rating_csv(listaGeneros, output_path, number_choice)

