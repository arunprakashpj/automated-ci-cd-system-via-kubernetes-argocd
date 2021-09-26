![AutomateForGood - Package with Docker](https://github.com/arunprakashpj/AutomateForGood/actions/workflows/dev-workflow.yml/badge.svg)
![Chef InSpec Testcases](https://github.com/arunprakashpj/AutomateForGood/actions/workflows/stag-workflow.yml/badge.svg)
# AutomateForGood :  Automatically package and deploy the application to kubernetes with CI/CD Pipelines

# Overview

A sample webapp called Automateforgood is used to exhibit the devop operations. The application is packaged with the help of Docker. Github Actions are used to enable continuous integration, thus automating the build and pushing the docker image to dockerhub. Github Actions also used to demo the application of Chef inSpec in automating testcases as a part of continuous integration. Kubernetes cluster is provisioned using K3s in a vagrant box where the application is deployed. Kubernetes Manifest template is made using Helm Charts and input configuration files for Staging and prod environment are made. ArgoCD is used to enable Continuous Delivery on each deployment at Staging/Prod Environment.

## Project Plan

* A link to a [Trello board](https://trello.com/b/7u7h4bK2/automateforgood) for the project
* A link to a [spreadsheet](https://docs.google.com/spreadsheets/d/14OYodH_OnKtR6owFtAEXYrLhqiKph24Uz_l4ORmVS_I/edit?usp=sharing) that includes the original and final project plan

### Getting Started

1. Clone this repository.
2. Install the dependencies.
3. Setup the Vagrant environment.
4. Package and Deploy the application of your choice.
5. Update this README to reflect how someone would use your code.

### Dependencies

1. Install [Git](https://git-scm.com/downloads)
2. Install [Python](https://www.python.org/downloads/)
3. Install [Node Js](https://nodejs.org/en/download/)
4. Install [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
5. Install [Chef Habitat](https://downloads.chef.io/tools/habitat)
6. Install [Chef InSpec](https://docs.chef.io/inspec/install/)
7. Install [Docker](https://docs.docker.com/get-docker/)
8. Install [Vagrant](https://www.vagrantup.com/downloads)
9. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
10. Install [ArgoCD](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd)

### Health End Points

The project has /healthinfo endpoint exposed at [app.py](https://github.com/arunprakashpj/AutomateForGood/blob/main/automateforgood/app.py) file

The project has /metrics endpoint exposed at [app.py](https://github.com/arunprakashpj/AutomateForGood/blob/main/automateforgood/app.py) file

The Logs have been enabled for the project.

### Instructions

1. Package the application using docker
    - Create a dockerfile to package the application. Keep the application of your choice in the project directory. Here I have a sample application called automateforgood.
    - Build the docker image. You can check the commands to build [here](https://github.com/arunprakashpj/AutomateForGood/blob/main/docker_commands) 
    - Test the docker image locally. Access the application on http://127.0.0.1:7111 . 

2. Continuous Integration with Github Actions to automate docker image build and push to hub
    - Aim of this step is to automate the packaging of the application using [Github Actions](https://github.com/marketplace/actions/build-and-push-docker-images).
    - Github Actions help us to build, tag and push the docker image of the application to dockerhub.
    - If not present, create .github/workflows directory. 
    - To automate the login into Docker Hub, the github actions use [Github Tokens](https://www.docker.com/blog/docker-hub-new-personal-access-tokens/) and [Github Encrypted Secrets](https://docs.github.com/en/actions/reference/encrypted-secrets).
    - Create and verify if the github actions execute on every new commit, thus pushing the latest docker image to the docker hub.

3. Continuous Integration with Github Actions to automate the execution of test cases via chef inSpec 
    - Aim of this step is to automate the testcase execution using [Chef InSpec](https://docs.chef.io/inspec/install/) and enable continuous integration via [Github Actions](https://github.com/arunprakashpj/AutomateForGood/blob/main/.github/workflows/stag-workflow.yml)
    - This [Github Actions](https://github.com/arunprakashpj/AutomateForGood/blob/main/.github/workflows/stag-workflow.yml) help us to trigger the test case execution whenever a new commit is made, thus enabling continuous integration.
    - Verify if the github actions execute the [Chef InSpec](https://docs.chef.io/inspec/install/) on every new commit, thus ensuring that nobody has broken the system.
 
4. Deploy a Kubernates Cluster using K3s
     - Aim of this step is to create a declarative kubernetes manifest and release the application to the sandbox environment
     - Use Vagrant environment and create kubernetes cluster with [k3s](https://k3s.io/). [vagrant file](https://github.com/arunprakashpj/AutomateForGood/blob/main/Vagrantfile) is attached for reference
     - To create a vagrant box, navigate to this [location](https://github.com/arunprakashpj/AutomateForGood/blob/main/Vagrantfile)  where vagrantfile is placed, Use the command ``vagrant up`` , then ``vagrant ssh``.
     - You can find the kubernetes declartive manifests [here](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/kubernetes-declarative-manifests.PNG).
     - Use the command ``kubectl apply -f yaml_file_name`` to deploy the application in k3s cluster.

4. Helm Charts Templating
     - The aim of this step is to parameterize the kubernetes manifests.
     - You can find the helm charts  [here](https://github.com/arunprakashpj/AutomateForGood/tree/main/helm).
     - The input values are built for [staging](https://github.com/arunprakashpj/AutomateForGood/tree/main/helm) and [production](https://github.com/arunprakashpj/AutomateForGood/tree/main/helm) environment seperately.
     
5. Continuous Delivery using ArgoCD
      - The aim of this step is to automatically deploy the application using ArgoCD, thus easy release to staging and production environment using the helm chart templates
      - Nodeport Service Yaml files can be found [here](https://github.com/arunprakashpj/AutomateForGood/tree/main/argocd)
      - Access the argoCD UI at https://192.168.50.4 : 300008 or http://192.168.50.4:30007
      - Login credentials can be retrieved using the steps [here](https://argoproj.github.io/argo-cd/getting_started/#4-login-using-the-cli)
      - Whenever you made a new commit, the application will be packed as a docker image and gets deployed after a quick test case verification.

  ###  Visualization of the entire process
  
  ## Fig 1 : Docker Run  
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/docker-run-app.PNG)
  
  ## Fig 2 : Docker Run Debug
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/docker-run-debug.PNG)
  
  ## Fig 3 : Accessing webapp from Docker Image  
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/docker-run-local.PNG)
 
  ## Fig 4 : CI Github Actions to build/push docker image to hub
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/ci-github-actions-docker-img.PNG)
  
  ## Fig 5 : CI Github Actions to automate the execution of test cases via chef inSpec 
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/ci-github-actions-chef-inSpec.PNG)
  
  ## Fig 6 : CI DockerHub
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/ci-dockerhub.PNG)
  
  ## Fig 7 : Vagrant Login
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/vagrant-login.PNG)
  
  ## Fig 8 : Kubernetes Pod Creation
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/k8s-pods-created.PNG)
  
  ## Fig 9 : Kubernetes Manifests
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/kubernetes-declarative-manifests.PNG)
  
  ## Fig 10 : ArgoCD Install and Start
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/argocd-install.PNG)
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/argocd-run.PNG)
  
  ## Fig 11 : ArgoCD Front Page
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/argo-login-page.PNG)
  
  ## Fig 12 : ArgoCD -Staging Environment
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/argocd-automatedforgood-stag.PNG)
  
  ## Fig 13 : ArgoCD - Prod Environment
  ![Screenshot](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/argocd-automatedforgood-prod.PNG)
  
  ## Fig 14 : Screenshots of all steps available at [here](https://github.com/arunprakashpj/AutomateForGood/tree/main/screenshots)
  
  ### Future Improvement

  ## Demo 

  [![Demo](https://github.com/arunprakashpj/Deploying-CICD-Pipeline-in-Azure/blob/main/Screenshots/clickhere.png)](https://youtu.be/krERbEe88GA)
