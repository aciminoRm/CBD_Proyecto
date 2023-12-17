# CBD_Proyecto
Analizar un Dataset PlayStore Google Android para ofrecer al los usuarios un resumen completo sobre las caracteristicas de las Apps 

# Miembros
* Neve Luca 
* Cimino Alessio

# Project Website
https://sites.google.com/view/procloapps

# Google Playstore
El archivo sobre el que trabajamos contiene más de 2,4 millones de aplicaciones. Para cada uno de estos hay información de cualquier tipo sobre la aplicación y también sus desarrolladores.
El programa se realizó en una máquina virtual kali linux, algunos scripts se adaptaron para poder trabajar también en el Cloud

# Linux
Para que funcione en linux, una vez descargados los archivos, siga los pasos siguientes:
  ## 1. Instalación de Python
  ```
    $ sudo apt-get update
    $ sudo apt-get install python.
  ```
  ## 2. Instalación de Spark
  ```
    $ sudo apt install default-jre pip
    $ pip install pyspark
    $ source ~/.profile
  ```
  ## 3. Instalación del paquete inquirer
  ```
    $ pip install inquirer
  ```
  ## 4. Ejecución
  ```
    $ python recomendador_de_app.py
```
# Cloud
los archivos ejecutables en el Cloud son solo aquellos en las carpetas que contienen la palabra Cloud al final
1. **Creación de Cluster**
En la consola de Cloud:
```
$ gcloud dataproc clusters create example-cluster --region europe-west6 --master-boot-disk-size 50GB --worker-boot-disk-size 50GB --enable-component-gateway
```
2. **Creación Bucket** 
   1. Ve a Navigation menu () > Cloud Storage > Buckets.
   2. Click CREATE.
   3. Rellena la información del bucket information y click CONTINUE
   4. Click CREATE
   5. Sube los archivos que deseas ejecutar en el Bucket
3. **Enviar el trabajo de Spark desde Cloud Shell**
   ```
   BUCKET=gs://<YOUR_BUCKET_NAME>
   gcloud dataproc jobs submit pyspark --cluster example-cluster --region=europe-west6 $BUCKET/wordcount.py
   ```



