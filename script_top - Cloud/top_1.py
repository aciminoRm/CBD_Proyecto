from pyspark.sql import SparkSession
from pyspark.sql.functions import col
#import sys

def generate_top_download_csv(listaGeneros, output_path, number_choice):
    spark = SparkSession.builder.appName("TopDownloads").getOrCreate()

    file_path = "Google-Playstore.csv"
    df = spark.read.option("header", "true").csv(file_path)

    filtered_df = df.filter(col("Category").isin(listaGeneros))
    sorted_df = filtered_df.orderBy(col("Maximum Installs").cast("int").desc())
    top_df = sorted_df.limit(number_choice)
    result_df = top_df.select("App Name", "Category", "Maximum Installs")

    result_df.write.option("header", "true").csv(output_path, mode="overwrite")

    spark.stop()
    print(f"File CSV '{output_path}' generato con successo.")

#print("Argomenti di input:", sys.argv)
#listaGeneros = sys.argv[1].split(',')
#number_choice = int(sys.argv[2])
#if not listaGeneros:
    #print("Specifica almeno un genere.")
    #sys.exit(1)
listaGeneros = ["Action", "Social", "Music"]
number_choice = 10

output_path = "output_top/Top_Download.csv"
generate_top_download_csv(listaGeneros, output_path, number_choice)

