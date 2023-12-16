import csv

def leggi_categorie(file_csv):
    categorie_set = set()

    with open(file_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            categorie = row['Category'].split('&')
            categorie_set.update(categorie)

    return sorted(set(c.strip() for c in categorie_set))

if __name__ == "__main__":
    file_csv = 'Google-Playstore.csv'  # Sostituisci con il percorso del tuo file CSV
    categorie = leggi_categorie(file_csv)

    print("Categorie senza ripetizioni in ordine alfabetico:")
    for categoria in categorie:
        print(categoria)



