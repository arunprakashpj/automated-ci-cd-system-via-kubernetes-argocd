# AutomateForGood :  Export a docker image via Chef Habitat and deploy the application to kubernetes enabling Continuous Delivery via ArgoCD

# Introduction

### Getting Started

1. Clone this repository.
2. Install the dependencies.
3. Setup the Vagrant environment.
4. Package and Deploy the application of your choice.
5. Update this README to reflect how someone would use your code.

### Dependencies

1. Install [Git](https://git-scm.com/downloads)
2. Install [Node Js](https://nodejs.org/en/download/)
4. Install [Chef Habitat](https://downloads.chef.io/tools/habitat)
5. Install [Docker](https://docs.docker.com/get-docker/)
6. Install [Vagrant](https://www.vagrantup.com/downloads)
7. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
8. Install [ArgoCD](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd)

### Instructions

1. Build the application using Chef Habitat

2. Export the app as docker image to docker hub 

3. Deploy a Kubernates Cluster using K3s
     - Aim of this step is to create a declarative kubernetes manifest and release the application to the sandbox environment

4. Helm Charts Templating
     - The aim of this step is to parameterize the kubernetes manifests.
     
5. Continuous Delivery using ArgoCD
    - The aim of this step is to automatically deploy the application using ArgoCD, thus easy release to staging and production environment using the helm chart templates
