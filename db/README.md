# FRANCAIS

# Base de données de l'application

1. Nous avons utilisé une base de données gérée par MongoDB (base de données orientée documents)
2. La base de données se trouve dans un container docker (voir `docker-compose.yaml`)

## Accès à la base de données

Un exemple d'accès à la base de données peut être trouvé dans le fichier `app.py` situé dans le backend. Vous y verrez comment récupérer des informations avec la fonction `testdb`.

Assurez-vous d'avoir accès à la collection **summaries**.

Si vous souhaitez débugger la base de données, une interface graphique est disponible sur `localhost:8080/dbviewer`.

## Données par défaut

La base de donnée a été initialisée avec le contenu du fichier `seed.json`.

## Structure de la base de données

La base de données est construite selon la structure suivante :

    { 
        "id": 0, // L'id du CR
        "title": "AINV_NLP_2021_CR_21_MAI", // Le titre du CR
        "projectGroup": "NLP", // Le projet associé à la réunion
        "date": "21/05/2021", // La date de la réunion
        "generatorName": "lgermain", // Le nom de la personne générant le CR
        "attendees": ["lgermain", "sabadou", "rporchette", "hmichel", "camsallem", "eremilleret"], // La liste des participants
        "meetingProgram": "Présentation de la maquette", // L'ordre du jour de la réunion
        "transcript": "", // La transcription de l'audio par la solution Speech-To-Text
        "summary": { 
            "extractive": { 
                "raw": " Laurem solor sit amet ", // Le résumé brut généré par CamemBERT
                "edited": " Laurem solor sit amet ", // Le résumé généré par CamemBERT et modifié par un utilisateur sans mise en page
                "html": "<h1>Laurem solor sit amet</h1>", // Le résumé généré par CamemBERT et modifié par un utilisateur avec mise en page
                "lastUpdate": "22/05/2021 12:05:22", // date et heure de la dernière modification
            }, 
            "abstractive": { 
                "raw": " Laurem solor sit amet ", // Le résumé brut généré par BART'hez
                "edited": " Laurem solor sit amet ", // Le résumé généré par BART'hez et modifié par un utilisateur sans mise en page
                "html": "<h1>Laurem solor sit amet</h1>", // Le résumé généré par BART'hez et modifié par un utilisateur avec mise en page 
                "lastUpdate": "22/05/2021 12:05:22", // date et heure de la dernière modification
            } 
        },
        "status" : "done", // Le statut de la génération du CR ("processing" ou "done")  
    },

# ENGLISH

# Database of the application

1. We used a document oriented database named MongoDB
1. We containerized the database (see `docker-compose.yaml`)

## Accessing the database

An example can be found in the `app.py` file located in the backend. You'll see how to retreive information in the `testdb` function.   

Make sure to access the **summaries** collection.

If you want to debug the database, an GUI is available at `localhost:8080/dbviewer`.

## Default data

The database has been seeded with the content of `seed.json`.


## Database structure

The database contains a table with the following structure

    { 
        "id": 0, // ID 
        "title": "AINV_NLP_2021_CR_21_MAI", // CR title
        "projectGroup": "NLP", // Project group associated with the meeting
        "date": "21/05/2021", // Date of the meeting
        "generatorName": "lgermain", // Name of the writer
        "attendees": ["lgermain", "sabadou", "rporchette", "hmichel", "camsallem", "eremilleret"], // List of participants
        "meetingProgram": "Présentation de la maquette", // Agenda of the meeting
        "transcript": "", // Voice to text transcriptions generated by the S2T solution
        "summary": { 
            "extractive": { 
                "raw": " Laurem solor sit amet ", // raw summary generated by CamemBERT
                "edited": " Laurem solor sit amet ", // user modified summary without any CSS style
                "html": "<h1>Laurem solor sit amet</h1>", // summary modified by the user with the CSS style
                "lastUpdate": "22/05/2021 12:05:22", // date and time of last modification 
            }, 
            "abstractive": { 
                "raw": " Laurem solor sit amet ", // raw summary generated by BART'hez
                "edited": " Laurem solor sit amet ", // user modified summary without any CSS style
                "html": "<h1>Laurem solor sit amet</h1>", // summary modified by the user with the CSS style 
                "lastUpdate": "22/05/2021 12:05:22", // date and time of last modification 
            } 
        },
        "status" : "done", // status of CR generation (processing/done)  
    },
