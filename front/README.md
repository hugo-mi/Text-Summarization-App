# **FRANCAIS**

# Front-end de l'application

1. Le front-end est dockerisé.
2. Le serveur statique de NGINX est utilisé pour l'application svelte. **(le projet doit être dans le dossier ```/svelte```)**
3. Le proxy inversé de NGINX est utilisé pour rediriger les requêtes de ```/api``` sur le back-end.

-----------------

## Utiliser le front-end dans un environnement de développemment

Pour utiliser l'environnement de développement du front-end, vous devez installer node.js et npm.

Une fois configuré, allez dans le dossier `front/svelte` et installez les dépendances avec la commande `npm install`.

Vous pouvez maintenant lancer l'environnement de développement avec la commande `npm run dev`.

-----------------

## Comment lancer le front-end uniquement.

Depuis le dossier ```/front``` du projet :

1. Créer l'image depuis le fichier Dockerfile avec la commande suivante :
``` docker build -t front .  ```
* où -t indiques en premier argument le nom de l'image docker (ne doit pas être changé) et en second argument le(s) fichier(s) à charger (le ```.``` prend tous les fichiers du dossier ouvert).

2. Lancer le container docker depuis l'image :
 ```docker run --rm --name front_container -d -p 8081:80 front    ```
 * où ```-p``` indiques le port local et le port du docker utilisé (sous format portlocal:portdocker).

3. Supprimer le container :
``` docker kill front_container```


-----------------------------------------------------------------------------------

# **ENGLISH**

# Front-end of the application

1. The front-end is dockerized.
2. NGINX's static server is used to serve the svelte app **(the project has to be in the ```/svelte``` directory)**
3. NGINX's reverse proxy is used to redirect requests on ```/api```  to the back-end 

-----------------

## Use the front-end in a development environment

To use the front-end dev environment, you need to have node.js and npm installed.  

Once configured, navigate to `front/svelte` directory, then install the dependancies with `npm install`.  

You can run the development server with `npm run dev`

-----------------

## How to launch the front-end only

From the ```/front``` folder of the repository :

1. Build the image from the Dockerfile  
``` docker build -t front .  ```
* where -t specifies the name of the docker's image (should not be changed) as its first arg and the files that should be loaded in it as its second arg ( ```.``` takes everything from the current directory)

2. Run the container from the image  
 ```docker run --rm --name front_container -d -p 8080:80 front    ```
* where ```-p```  specifies the local's port and the docker's port used ( local's:docker's)

3. To kill the container   
``` docker kill front_container```
