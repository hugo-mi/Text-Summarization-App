# AI Engine of the application

1. The engine is dockerized.
2. The bengine is implemented with Flask and served by with Gunicorn

## How to launch the engine only

**This proceudure is made for debugging purposes, please use the main README.md for full deployment**

From the /engine folder of the repository :

1. Build the image from the Dockerfile  
``` docker build -t engine .  ```
* where -t specifies the name of the docker's image (should not be changed) as its first arg and the files that should be loaded in it as its second arg ( ```.``` takes everything from the current directory)

2. Run the container from the image  
 ```docker run --rm --name engine_container -d -p 8082:80 engine    ```
* where ```-p```  specifies the local's port and the docker's port used ( local's:docker's)

3. To kill the container   
``` docker kill engine_container```

