![AutomateForGood - Package with Docker](https://github.com/arunprakashpj/AutomateForGood/actions/workflows/dev-workflow.yml/badge.svg)
![Chef InSpec Testcases](https://github.com/arunprakashpj/AutomateForGood/actions/workflows/stag-workflow.yml/badge.svg)
# AutomateForGood :  eAuto - Automatically package and deploy the application to kubernetes with CI/CD Pipelines

# Overview

In this project eAuto, A sample web app called Automateforgood is used to exhibit the DevOps practices. Whenever a new commit is made to the GitHub repo, Github Actions automatically triggers an action to package the application as  Docker Image and push it to the Docker Hub enabling continuous integration. Another Github Actions trigger the system to execute Chef inSpec test cases as a part of continuous integration. 

The Kubernetes cluster is provisioned using K3s in a vagrant box where the application can be deployed. Once the docker image is available in the docker hub,  it is automatically deployed into Kubernetes. Kubernetes Manifest template is made using Helm Charts and input configuration files for Staging and prod environment are created. ArgoCD is used to enable Continuous Delivery on each deployment at the Staging/Prod Environment.

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
 
  ### How it meets the goal "Automate For Good"
  1. Code quality will be increased when CI/CD is in-place. Because Whenever code commit is made, automatically lint check will run to evaluate the code style. 
  2. Delivery and Deployment will be faster as there is almost nil review time involved. Whenever new changes made, automatically docker image is generated and deployed into the kubernetes cluster. No maual review involved anywhere. 
  3. The docker image is created with every commit. This ensures consistency with code and excution environment.
  4. Automation removes the possibilities for human errors. Once you commit the code, the build, deploy, test and delivery are completely automated in this project thus no possibility for human errors.
  5. Fault isolation is very easy. Even for a single line commit, the new docker build and deployment is triggered. Also test cases will be executed via Chef inSpec thus fault isolation is spot on.
  6. No more head ache with frequent update/maintanence. This project has two environments integrated. One is staging and other is prod. Easy maintanance and swap of images can be done between stag and prod environment.
  7. This automation project make the delivery faster, consistant and accurate. 
  
  ### Business use case viability & Scalability
  This project targets the cloud native environment where CI/CD assitance will be a big boosting factor. Kubernetes is used in the project to enable scalability. Also Helm charts are used in this project to make the kubernetes configuration even more simple.
  
  ### What next
  1. Explore the application of Prometheus and Grafana. Learn more about Observability. 
  2. Explore Chef Habitat. Already I built a sample application following offcial chef tutorials and exported it as docker image. You can see the execution here. I am looking forward to know more about the benifits of Chef Habitat
  3. Build CI/CD Pipelines in AWS and explore the world of Cloud Ops
  4. List Goes On...
        
        

  ## Demo 

  [![Demo](https://github.com/arunprakashpj/Deploying-CICD-Pipeline-in-Azure/blob/main/Screenshots/clickhere.png)](https://youtube.com)
