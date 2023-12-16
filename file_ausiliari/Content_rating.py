from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def print_distinct_content_ratings(file_path):
    # Crea una sessione Spark
    spark = SparkSession.builder.appName("DistinctContentRatings").getOrCreate()

    # Leggi il file CSV
    df = spark.read.option("header", "true").csv(file_path)

    # Definisci i valori noti come rating
    known_ratings = ["Unrated", "Everyone", "Everyone 10+", "Teen", "Mature 17+", "Adults only 18+"]

    # Filtra le righe in base alla colonna 'Content Rating'
    filtered_df = df.filter(col("Content Rating").isin(known_ratings))

    # Ottieni i valori distinti sotto la colonna 'Content Rating'
    distinct_content_ratings = filtered_df.select("Content Rating").distinct().collect()

    # Stampa i valori distinti
    print("Valori distinti sotto la colonna 'Content Rating':")
    for row in distinct_content_ratings:
        print(row["Content Rating"])

    # Chiudi la sessione Spark
    spark.stop()

# Esempio di utilizzo
file_path = "../Google-Playstore.csv"  # Aggiungi il percorso corretto se necessario
print_distinct_content_ratings(file_path)

