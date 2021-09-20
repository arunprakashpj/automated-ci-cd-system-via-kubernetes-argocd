# AutomateForGood :  Export a docker image via Chef Habitat and deploy the application to kubernetes enabling Continuous Delivery via ArgoCD

# Introduction

### Getting Started

### Dependencies

### Instructions

1. Build the application using Chef Habitat

2. Export the app as docker image to docker hub 

3. Deploy a Kubernates Cluster using K3s
     - Aim of this step is to create a declarative kubernetes manifest and release the application to the sandbox environment

4. Helm Charts Templating
     - The aim of this step is to parameterize the kubernetes manifests.
     
5. Continuous Delivery using ArgoCD
    - The aim of this step is to automatically deploy the application using ArgoCD, thus easy release to staging and production environment using the helm chart templates
