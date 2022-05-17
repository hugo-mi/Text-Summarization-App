# Text Summarization App

![](https://github.com/hugo-mi/Text-Summarization-App/blob/main/img/Homepage.png)

# **FRANCAIS**

## Description

Réalisation de deux POC orientés résumé et génération automatique de textes en français

Application d'une approche d'apprentissage par transfert : 
- Fine-tuning avec le dataset ``ML SUM`` du transformer ``CamemBERT`` pour la tâche de synthèse extractive
- Fine-tuning du transformer ``OrangeSUM`` ``mBART'hez`` pour la tâche de synthèse abstractive

Développement d'une application end-to-end pour l'automatisation de la rédaction d'un compte rendu de réunion en français :
- Intégration des deux modèles "fine-tuné" (CamemBERT et mBART'hez) de résumé de textes automatique.

## Application NLP développée par l'équipe NLP-2021

Cette application web génère automatiquement un compte-rendu de réunion.
Pour développer cette solution nous avons utilisé les technologies suivantes :

- Front-end : Svelte.js
- Back-end : Flask
- Transcription de l'audio : Rev.AI
- Méthodes de résumé de texte: 
**Camembert-base fine-tuned** pour la génération extractive and **mBART'hez fine-tuned** pour la génération abstractive
- Base de données : MongoDB
- Web Server : NGINX

## Pré-Requis 

- Installer docker (https://www.docker.com/products/docker-desktop)
- Télécharger les poids des modèles (>2Go) :
    * Se connecter au serveur S3 https://s3.console.aws.amazon.com/s3/home?region=eu-west-1#
    * Aller dans le dossier aoc-innov-data-nlp > Data, où vous trouverez des dossiers pour les deux modèles utilisés (mBARThez et CamemBERT)
    * Télécharger les poids des deux modèles (pytorch_model.bin)
    * Les placer dans les dossiers correspondant dans le projet (engine/data/\{camembert, mbarthez\})
- Mettre à jour la clé API Rev.AI dans le fichier `docker-compose.yaml`. (REV_AI_KEY)

Pré-requis sur les PC Aubay :
- Dans Docker Client > Settings (à côté de Upgrade) > Docker Engine > json file : mettre l'option `buildkit` a 'false'.
- Dans Docker Client > Settings > Ressources > Proxies > Web Server (HTTP) : mettre le proxy http://proxy.aubay.com:3128

## Instructions

1. Créer les images 

```docker-compose build --build-arg http_proxy="http://proxy.aubay.com:3128" --build-arg https_proxy="http://proxy.aubay.com:3128"``` en première utilisation  

```docker-compose build``` sinon

2. Lancer les containers  
```docker-compose up```

3. Accéder au site  
- Front-end est accessible sur `localhost:8080/`
- Back-end est accessible sur `localhost:8080/api` (les endpoint de test sont accessibles sur `localhost:8080/api/test`, les endpoint d'engine test sur `localhost:8080/api/testengine`, les endpoint de test de la base de données sur `localhost:8080/api/testdb`)

4.  Arrêter l'application
- Eteindre les containers
 ```docker-compose down``` or Ctrl+C

- Supprimer les containers  
 ```docker-compose rm```


# **ENGLISH**

## Description

Realization of two POCs focused on summarization and automatic generation of French texts

Application of a transfer learning approach: 
- Fine-tuning with the ``ML SUM'' dataset of the ``CamemBERT'' transform for the extractive summarization task
- Fine-tuning of the ``OrangeSUM`` ``mBART'hez`` transform for the abstractive synthesis task

Development of an end-to-end application for the automation of the writing of a meeting report in French:
- Integration of the two "fine-tuned" models (CamemBERT and mBART'hez) for automatic text summarization.

This web application automates the writing of meeting minutes. 
To develop the IT solution we used the following technologies :

- Front-end : Svelte.js
- Back-end : Flask
- Speech To Text Engine: Rev.AI
- AI Summarizer Engine: 
**Camembert-base fine-tuned** for extractive summarization and **mBART'hez fine-tuned** for abstractive summarization 
- Database : MongoDB
- Web Server : NGINX

## Requirements

- Install docker (https://www.docker.com/products/docker-desktop)
- As the models' weights are over 2Go, we need you to download them : 
    * Log into https://s3.console.aws.amazon.com/s3/home?region=eu-west-1#
    * Go to aoc-innov-data-nlp > Data , you'll find the folders for the two models (mBARThez and CamemBERT)
    * Download the weights for each of them (pytorch_model.bin)
    * Place them in their corresponding folders in the project (engine/data/\{camembert, mbarthez\})
- Update the Rev.AI api key in the `docker-compose.yaml` file at line 7 (REV_AI_KEY)

Requirements on Aubay's computers :
* Set the `buildkit` feature to false ( Docker Client > Settings (next to Upgrade) > Docker Engine > json file).
* Set the proxy to http://proxy.aubay.com:3128 (Docker Client > Settings > Ressources > Proxies > Web Server (HTTP))

## Instructions


1. Build the images 

```docker-compose build --build-arg http_proxy="http://proxy.aubay.com:3128" --build-arg https_proxy="http://proxy.aubay.com:3128"``` on premices 

```docker-compose build``` at home   

2. Run the containers  
```docker-compose up```

3. Access the site  
- Front-end is located at `localhost:8080/`
- Back-end can be accessed at `localhost:8080/api` (test endpoint at `localhost:8080/api/test`, engine test endpoint at `localhost:8080/api/testengine`, database test endpoint at `localhost:8080/api/testdb`)


4. Stop the application
- Shutdown the containers  
 ```docker-compose down``` or Ctrl+C

- Remove the containers  
 ```docker-compose rm```



