# **FRANCAIS**

# Back-end de l'application

1. Le back-end est dockerisé.
2. Le back-end est implémenté avec Flask et Gunicorn.

## API Reference

--------
`GET /api/summary/<id:int>`  
Renvoie le résumé comportant l'id passé dans l'adresse sous la forme d'un fichier json

---------
`GET /api/summaries/list`  
Retourne une liste JSON comportant l'id, auteur, date des résumés ...

---------

`POST /api/summary/{ext, abs}/<int:summary_id>`  
Remet à zéro les modifications effectuées sur un CR abstractif/extractif pour celui d'identifiant `summary_id`

---------

`POST /api/createCR/text`
Envoie une nouvelle requête pour créer un résumé à partir de texte.  
Le contenu du POST doit contenir un JSOn de la forme suivante :   

```
{ 
    "id": 0, 
    "title": "AINV_NLP_2021_CR_21_MAI", 
    "projectGroup": "NLP", 
    "date": "21/05/2021", 
    "generatorName": "lgermain", 
    "attendees": ["lgermain", "sabadou", "eremilleret"], 
    "meetingProgram": "Présentation de la maquette", 
    "transcript": "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMake"
    }
```


-----

`POST /api/createCR/audio`  
Envoie une nouvelle requête pour créer un résumé à partir de texte.  
Le contenu du POST doit être sous la forme d'un formulaire dont le champ `data` contient une JSON de la forme suivante :  

```
{ 
    "id": 0, 
    "title": "AINV_NLP_2021_CR_21_MAI", 
    "projectGroup": "NLP", 
    "date": "21/05/2021", 
    "generatorName": "lgermain", 
    "attendees": ["lgermain", "sabadou", "eremilleret"], 
    "meetingProgram": "Présentation de la maquette"
}
```

Et le champ `file` contient le fichier audio.


-------

`POST /api/summary/<int:id>/update`  
Met à jour la base de données avec le fichier JSON fourni:  

```
{ 
    "id": 0, 
    "title": "AINV_NLP_2021_CR_21_MAI", 
    "projectGroup": "NLP", 
    "date": "21/05/2021", 
    "generatorName": "lgermain", 
    "attendees": ["lgermain", "sabadou", "eremilleret"], 
    "meetingProgram": "Présentation de la maquette", 
    "transcript": "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMake", 
    "summary": { 
        "extractive": { 
            "raw": "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié.", 
            "edited": "Laurem solor sit amet",
            "html": "<h1>Laurem solor sit amet</h1>"
        }, 
        "abstractive": { 
            "raw": "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte."
        } 
    },
    "status" : "done"
    }
```
**Attention, tout champ laissé vide supprimera l'entrée en base de données**

## Comment lancer le back-end uniquement :

**Cette documentation n'est valable que pour du débuggage, pour déployer l'application merci de vous référer au README.md principal.**

Depuis le dossier /back du projet :

1. Créer l'image depuis le fichier Dockerfile avec la commande suivante :
``` docker build -t back .  ```
* où -t indiques en premier argument le nom de l'image docker (ne doit pas être changé) et en second argument le(s) fichier(s) à charger (le ```.``` prend tous les fichiers du dossier ouvert).

2. Lancer le container docker depuis l'image :
 ```docker run --rm --name back_container -d -p 8081:80 back    ```
 * où ```-p``` indiques le port local et le port du docker utilisé (sous format portlocal:portdocker).

3. Supprimer le container :
``` docker kill back_container```

-----------------------------------------------------------------------------------
# **ENGLISH**

# Back-end of the application

1. The back-end is dockerized.
2. The back-end is implemented with Flask and served by with Gunicorn

## How to launch the back-end only

**This proceudure is made for debugging purposes, please use the main README.md for full deployment**

From the /back folder of the repository :

1. Build the image from the Dockerfile  
``` docker build -t back .  ```
* where -t specifies the name of the docker's image (should not be changed) as its first arg and the files that should be loaded in it as its second arg ( ```.``` takes everything from the current directory)

2. Run the container from the image  
 ```docker run --rm --name back_container -d -p 8081:80 back    ```
* where ```-p```  specifies the local's port and the docker's port used ( local's:docker's)

3. To kill the container   
``` docker kill back_container```

