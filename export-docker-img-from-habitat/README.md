# hab-two-tier

This Habitat project illustrates a basic Apache web application (`webapp`) and HAProxy load balancer (`haproxy`).

The Docker Compose file brings up HAProxy and two load-balanced webapp instances.

## Build and Export the packages (inside the studio)

```
$ hab studio enter
$ build webapp
# Grab the built artifact, i.e. "Artifact: /src/results/learn-chef-webapp-0.2.0-20180105200724-x86_64-linux.hart"
$ hab pkg export docker results/learn-chef-webapp-0.2.0-20180105200724-x86_64-linux.hart
$ build haproxy
# Grab the built artifact, i.e. "Artifact: /src/results/learn-chef-haproxy-1.6.11-20180105200724-x86_64-linux.hart"
$ hab pkg export docker results/learn-chef-haproxy-1.6.11-20180105200724-x86_64-linux.hart
```

## Build and Export the packages (outside the studio)

```
$ hab pkg build webapp
# Grab the built artifact, i.e. "Artifact: results/learn-chef-webapp-0.2.0-20180105200724-x86_64-linux.hart"
$ hab pkg export docker results/learn-chef-webapp-0.2.0-20180105200724-x86_64-linux.hart

$ hab pkg build haproxy
# Grab the built artifact, i.e. "Artifact: results/learn-chef-haproxy-1.6.11-20180105200724-x86_64-linux.hart"
$ hab pkg export docker results/learn-chef-haproxy-1.6.11-20180105200724-x86_64-linux.hart
```

## Run

```
$ HAB_LICENSE=accept-no-persist docker-compose up -d
$ curl localhost:8000/cgi-bin/hello-world
$ docker-compose down
```
  ###  Visualization of the entire process
  
  ## Fig 1 : Build Webapp
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/habitatbuild.PNG)

  ## Fig 2 : .hart files
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/hartfiles.PNG)
  
  ## Fig 3 : Run export
 ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/runexport.PNG)
 
  ## Fig 4 : Docker images
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/docker_images.PNG)
  
  ## Fig 5 : Launching the cluster
  
 ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/docker-compose.PNG)
 ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/docker_ps.PNG)
 ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/docker_network.PNG)
 
  ## Fig 6 : Launching the Application
  
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/apprunning.PNG)
  
  ## Fig 7 : Running Curl to see the result
    ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/curl_result.PNG)
    
 ## Exporting the docker image to the dockerhub
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/export-docker-img-from-habitat/screenshots/webapp_in_dockerhub.PNG)


 
This hab-two-tier sample  originated from the repo [learn-chef/hab-two-tier](https://github.com/learn-chef/hab-two-tier)
