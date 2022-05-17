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

## DEMO de l'application

[Voir la démo de l'app](https://drive.google.com/file/d/1WBJFsRIHyvj2NU9GSeJw_V-Kn6RT_aFS/view?usp=sharing)

## Application

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

## Instructions

1. Créer les images 

```docker-compose build```

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
- Fine-tuning of the ``OrangeSUM`` ``mBART'hez`` transform for the abstractive summarization task

Development of an end-to-end application for the automation of the writing of a meeting report in French:
- Integration of the two "fine-tuned" models (CamemBERT and mBART'hez) for automatic text summarization.

## DEMO

[See the demo of the app](https://drive.google.com/file/d/1WBJFsRIHyvj2NU9GSeJw_V-Kn6RT_aFS/view?usp=sharing)

## Web App

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

## Instructions


1. Build the images 

```docker-compose build```

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



