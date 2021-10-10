# About

The project hab-two-tier is a sample project that intends to build a basic Apache web application (`webapp`) and HAProxy load balancer (`haproxy`). Post my hackathon project, I have explored the application of chef habitat by learning from the official site. I have followed some official tutorials from [chef website](https://learn.chef.io/courses/course-v1:chef+Habitat101+Perpetual/course/) and I was able to build a docker image which i have manually exported to my docker hub. I undersatnd that docker habitat helps us in making cross platform builds, thus exploring further utilizing the scafolding given by official chef website.  This sample scafolding to tryout chef habitat originated from the  repo [learn-chef/hab-two-tier](https://github.com/learn-chef/hab-two-tier)


## Build and Export the packages (inside the studio)

```
$ hab studio enter
$ build webapp
$ hab pkg export docker results/arunprakashpj-haproxy-1.6.11-20210919225910-x86_64-linux.hart
$ build haproxy
$ hab pkg export docker results/arunprakashpj-webapp-0.2.0-20210919225930-x86_64-linux.hart
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
