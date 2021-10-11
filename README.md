![AutomateForGood - Package with Docker](https://github.com/arunprakashpj/AutomateForGood/actions/workflows/dockerbuild-workflow.yml/badge.svg)
![Chef InSpec Testcases](https://github.com/arunprakashpj/AutomateForGood/actions/workflows/chef-Inspec-workflow.yml/badge.svg)


<h2 align="center">BrewOps.</h2>
<p align="center">Efficient CI/CD Automation System</p>

<p align="center">
  <a href="https://nodejs.org/en/download/">
    <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=whites" alt="Version">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Code Version">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white" alt="Code Version">
  </a>
    
  <a href="">
    <img src="https://img.shields.io/badge/-Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Code Version">
  </a>
    
    
  <a href="">
    <img src="https://img.shields.io/badge/chefInspec-1572B6?style=for-the-badge&logo=chefInspec&logoColor=white" alt="Code Version">
  </a>
   <a href="">
    <img src="https://img.shields.io/badge/-chefHabitat-%23Clojure?style=for-the-badge&logo=chef&logoColor=white" alt="Code Version">
  </a>

  <a href="">
    <img src="https://img.shields.io/badge/-vagrant-02569B?style=for-the-badge&logo=vagrant&logoColor=white" alt="Code Version">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/-kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Code Version">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/-helm-3655FF?style=for-the-badge&logo=helm&logoColor=white" alt="Code Version">
  </a>
    
   <a href="">
    <img src="https://img.shields.io/badge/-argoCD-E34F26?style=for-the-badge&logo=argoCD&logoColor=white" alt="Code Version">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/-slack-6933FF?style=for-the-badge&logo=slack&logoColor=white" alt="Code Version">
  </a>
  
  </a>
</p>
<br>



# AutomateForGood :  BrewOps - Automatically package and deploy the application to kubernetes with CI/CD Pipelines

# Overview

In this project BrewOps, A sample web app called Automateforgood is used to exhibit the DevOps practices. Whenever a new commit is made to the GitHub repo, [Github Actions](https://docs.github.com/en/actions) automatically triggers an [action](https://github.com/arunprakashpj/AutomateForGood/blob/main/.github/workflows/dockerbuild-workflow.yml) to package the application as  [docker](https://docs.docker.com/get-docker/) Image and push it to the [Docker hub](https://hub.docker.com/) enabling [continuous integration](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration). Another [Github Actions](https://github.com/arunprakashpj/AutomateForGood/blob/main/.github/workflows/chef-Inspec-workflow.yml) trigger the system to execute [Chef InSpec](https://docs.chef.io/inspec/install/) test cases as a part of [continuous integration](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration). 

The [Kubernetes](https://kubernetes.io/) cluster is provisioned using K3s in a [vagrant box](https://www.vagrantup.com/downloads) where the application can be deployed. Once the [docker](https://docs.docker.com/get-docker/) image is available in the [Docker hub](https://hub.docker.com/),  it is automatically deployed into [kubernetes](https://kubernetes.io/). Kubernetes Manifest template is made using [Helm](https://helm.sh/) Charts and input configuration files for Staging and prod environment are created. [ArgoCD](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd) is used to enable [Continuous Delivery](https://en.wikipedia.org/wiki/Continuous_delivery) on each deployment at the Staging/Prod Environment. In the end, I have also experimented creating [docker](https://docs.docker.com/get-docker/) image by exporting the artifacts created by [Chef Habitat](https://downloads.chef.io/tools/habitat). Its quiet handy when it comes to cross platform builds.

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
9. Install [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
10. Install [Helm](https://helm.sh/)
11. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
12. Install [ArgoCD](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd)

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

3. Continuous Integration with Github Actions to automate the execution of test cases via [Chef InSpec](https://docs.chef.io/inspec/install/) 
    - Aim of this step is to automate the testcase execution using [Chef InSpec](https://docs.chef.io/inspec/install/) and enable continuous integration via [Github Actions](https://github.com/arunprakashpj/AutomateForGood/blob/main/.github/workflows/stag-workflow.yml)
    - This [Github Actions](https://github.com/arunprakashpj/AutomateForGood/blob/main/.github/workflows/stag-workflow.yml) help us to trigger the test case execution whenever a new commit is made, thus enabling continuous integration.
    - Verify if the github actions execute the [Chef InSpec](https://docs.chef.io/inspec/install/) on every new commit, thus ensuring that nobody has broken the system.
 
4. Deploy a Kubernates Cluster using K3s
     - Aim of this step is to create a declarative kubernetes manifest and release the application to the sandbox environment
     - Use Vagrant environment and create kubernetes cluster with [k3s](https://k3s.io/). [vagrant file](https://github.com/arunprakashpj/AutomateForGood/blob/main/Vagrantfile) is attached for reference
     - To create a vagrant box, navigate to this [location](https://github.com/arunprakashpj/AutomateForGood/blob/main/Vagrantfile)  where vagrantfile is placed, Use the command ``vagrant up`` , then ``vagrant ssh``.
     - You can find the kubernetes declartive manifests [here](https://github.com/arunprakashpj/AutomateForGood/blob/main/screenshots/kubernetes-declarative-manifests.PNG).
     - Use the command ``kubectl apply -f yaml_file_name`` to deploy the application in k3s cluster. The commands I used aregiven below.
     - Execute ``kubectl apply -f namespace.yaml``.
     - Execute ``kubectl apply -f service.yaml``
     - Execute ``kubectl apply -f deploy.yaml`` 

4. Helm Charts Templating
     - The aim of this step is to parameterize the kubernetes manifests.
     - You can find the helm charts  [here](https://github.com/arunprakashpj/AutomateForGood/tree/main/helm).
     - The input values are built for [staging](https://github.com/arunprakashpj/AutomateForGood/tree/main/helm) and [production](https://github.com/arunprakashpj/AutomateForGood/tree/main/helm) environment seperately.
     
5. Continuous Delivery using ArgoCD
      - The aim of this step is to automatically deploy the application using ArgoCD, thus easy release to staging and production environment using the helm chart templates
      - Execute ``kubectl create namespace argocd`` to create the namespace.
      - Execute  `` kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/core-install.yaml``.
      - Execute ``kubectl apply -f argocd-nodeport.yaml``. Nodeport Service Yaml files can be found [here](https://github.com/arunprakashpj/AutomateForGood/tree/main/argocd).
      - Execute ``kubectl apply -f helm-automateforgood-staging.yaml``. You can find the yaml file [here](https://github.com/arunprakashpj/AutomateForGood/blob/main/argocd/helm-automateforgood-staging.yaml).
      - Execute ``kubectl apply -f helm-automateforgood-prod.yaml``. You can find the yaml file [here](https://github.com/arunprakashpj/AutomateForGood/blob/main/argocd/helm-automateforgood-prod.yaml)
      - Execute ``curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64``
      - Execute ``chmod +x /usr/local/bin/argocd``
      - Access the argoCD UI at https://192.168.50.4 : 300008 or http://192.168.50.4:30007
      - Login credentials can be retrieved using the steps [here](https://argoproj.github.io/argo-cd/getting_started/#4-login-using-the-cli)
      - Whenever you made a new commit, the application will be packed as a docker image and gets deployed after a quick test case verification.
      
6. Slack Support
     - The Issues, Pulls, commits,release, deployments releated to this project will be notified to the user via the slack channel.

``` /github subscribe owner/repo [feature] ```
``` /github unsubscribe owner/repo [feature] ```

Following features are enabled by default  and can be disabled with the `/github unsubscribe owner/repo [feature]` command:

- `issues` - Opened or closed issues
- `pulls` - New or merged pull requests, as well as draft pull requests marked "Ready for Review"
- `commits` - New commits on the default branch (usually `master`)
- `releases` - Published releases
- `deployments` - Deployment review notifications and Deployment status updates.

Following features  are disabled by default, and can be enabled with the `/github subscribe owner/repo [feature]` command:

- `reviews` - Pull request reviews
- `comments` - New comments on issues and pull requests
- `branches` - Created or deleted branches
- `commits:*` - All commits pushed to any branch
- `+label:"your label"` - Filter issues, pull-requests and comments based on their labels.

Know more about the integration from [here](https://slack.com/intl/en-se/help/articles/232289568-GitHub-for-Slack) to setup the integration

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
  
  ## Fig 14 : Screenshots of all steps available [here](https://github.com/arunprakashpj/AutomateForGood/tree/main/screenshots)
  
  ### DevOps practices followed
  1. Continuous Integration using Github Actions.
  2. Automated Testing via Chef inSpec & Github Actions.
  3. Configuration of Kubernetes clusters using Helm Charts.
  4. Continous Delivery using ArgoCD.


  ### Implementation and Use of Chef Software
  1. [Chef InSpec](https://docs.chef.io/inspec/install/) has been explored and employed in the automation of testcases.
        - [Chef InSpec](https://docs.chef.io/inspec/install/) has been integrated as a part of Continuous Integration via Github Actions.
        - The [Chef InSpec](https://docs.chef.io/inspec/install/) runs during new commit and chek if the kubernetes yaml contains all the mandatory keywords. That is, It helps in configuration verification.
        - The implementation shows a sample usecase to give a essence of the software. Other potential use case are detailed below
  2. [Chef Habitat](https://downloads.chef.io/tools/habitat) has been experimented as well to create artificats and later exported as docker image.
       - Post completion of the project, I experimented with the [Chef Habitat](https://downloads.chef.io/tools/habitat) to explore how it can be employed in artificat creation and how that can be exported as docker image. You can find my experiment here.
       - The implementation shows a sample usecase to give an essence of the software. This is much more than this use case and the same is detailed below

  ### Extended Use cases of Chef Inspec
   1.  Enable a testcase to ensure that web server is only listening on well-secured ports
   2.  Run test on remote host on SSH or  WinRM
   3.  Execute test on docker container
   4.  Execute a profile targetting AWS/Azure Environment
   5.  Make configuration verification like we did for Kubernetes 
   6.  More usecases [here](https://github.com/inspec/inspec/)
       
   ### Extended Use cases of Chef Habitat
   1. [Chef Habitat](https://downloads.chef.io/tools/habitat) Artificats
      - Major advantage of [Chef Habitat](https://downloads.chef.io/tools/habitat) is, we can deploy and run our habitat app in different infrastructure environments like bare metal, VM, containers, and PaaS.
      - [Chef Habitat](https://downloads.chef.io/tools/habitat) Artificats (.hart) supports cross platform builds, thus we can be easily export the app to docker, tarball, Apache Mesos and Cloud Foundary.
      - I gave a try on this, You can check the experiment [here]
  
  
  ### How it meets the goal "Automate For Good"
  1. Code quality will be increased when CI/CD is in-place. 
  2. Delivery and Deployment will be faster as there is almost nil review time involved. Whenever new changes made, automatically docker image is generated and deployed into the kubernetes cluster. No maual review involved anywhere. 
  3. The docker image is created with every commit. This ensures consistency with code and excution environment.
  4. Automation removes the possibilities for human errors. Once you commit the code, the build, deploy, test and delivery are completely automated in this project thus no possibility for human errors.
  5. Fault isolation is very easy. Even for a single line commit, the new docker build and deployment is triggered. Also test cases will be executed via [Chef InSpec](https://docs.chef.io/inspec/install/) thus fault isolation is spot on. Though [Chef InSpec](https://docs.chef.io/inspec/install/) has many use cases, here it is employed to find the kubernetes configuration errors. 
  6. No more head ache with frequent update/maintanence. This project has two environments integrated. One is staging and other is prod. Easy maintanance and swap of images can be done between stag and prod environment.
  7. This automation project make the delivery faster, consistant and accurate. 
  
  ### Business use case viability & Scalability
  This project targets the cloud native environment where CI/CD assitance will be a big boosting factor. Kubernetes is used in the project to enable scalability. Also Helm charts are used in this project to make the kubernetes configuration even more simple. Chef Inspec is an interesting addition to enable infrastructure configuration testing/ security complaince testing.
  
  ### What next
  1. Explore the application of [Prometheus](https://prometheus.io/) for monitering and [Grafana](https://grafana.com/) for Observability. 
  2. Explore [polaris](https://github.com/FairwindsOps/polaris) to ensure that Kubernetes pods and controllers are configured properly utlizing best practices.
  3. Explore [Chef Habitat](https://downloads.chef.io/tools/habitat). Already I built a sample application following offcial chef tutorials and exported it as docker image. You can see the execution here. I am looking forward to know more about the benifits of [Chef Habitat](https://downloads.chef.io/tools/habitat).
  4. Build CI/CD Pipelines in AWS/Azure and explore the world of Cloud Ops. I am consistantly self learning and you can find my CI/CD pipeline deployment over Azure project [here](https://github.com/arunprakashpj/Deploying-CICD-Pipeline-in-Azure). Looking forward to keep the momentum.
  5. List Goes On..
        
        

  ## Demo 

  [![Demo](https://github.com/arunprakashpj/Deploying-CICD-Pipeline-in-Azure/blob/main/Screenshots/clickhere.png)](https://youtube.com)
