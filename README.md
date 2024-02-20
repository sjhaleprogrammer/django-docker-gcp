# CSCI 4170 Cloud Computing Project

Welcome to the CSCI 4170 Cloud Computing Project repository! This project is a Dockerized Django application designed for deployment on Google Cloud Platform (GCP). As part of CSCI 4170, we explore the fundamentals of cloud computing, containerization, and orchestration to demonstrate the seamless deployment of a scalable and maintainable web application.

## Introduction

In the rapidly evolving landscape of cloud computing, understanding how to deploy and manage applications efficiently is crucial. This project serves as a practical exploration of cloud-native development practices, emphasizing the utilization of containers and orchestration tools for streamlined deployment and scaling.

### Key Concepts

- **Dockerization:** We containerize the Django application using Docker to encapsulate dependencies, ensuring consistency across development and production environments.

- **Google Cloud Platform (GCP):** Leveraging the power of GCP, we demonstrate the deployment of our Dockerized application on Google Kubernetes Engine (GKE), showcasing the scalability and robustness of container orchestration.

- **DevOps Practices:** The project incorporates DevOps principles, emphasizing automation, continuous integration, and continuous deployment, to facilitate collaborative and agile development.

## Features

Our Dockerized Django app comes equipped with features that highlight the benefits of cloud-native development:

- **Scalability:** Easily scale your application horizontally by leveraging the container orchestration capabilities of GKE.

- **Portability:** Docker containers ensure that your application runs consistently across various environments, from local development to the cloud.

- **Ease of Deployment:** GCP provides a seamless environment for deploying, managing, and monitoring containerized applications, reducing deployment complexities.

This project aims to provide a hands-on experience in applying cloud computing concepts, allowing students to gain practical insights into the tools and practices essential for modern software development and deployment.

## Running Locally
#### Create virtual environment (venv)
Navigate to the docker-gcp directory and create a virtual environment and activate it with the following commands
```
cd django-docker-gcp/
python3 -m venv venv
source venv/bin/activate
```

#### Install modules
Type the following command in the project directory to install required modules
```
pip3 install -r requirements.txt
```

#### Set API Variable
In the venv terminal type
```
export OPEN_WEATHER_API='apikey'
```


#### Run Server

Run this command to start the web server.

```
python3 manage.py runserver
```

Now navigate to http://127.0.0.1:8080/ in your browser.


## Running in Docker

#### Build image 
```
docker build -t my-python-app .  
```

#### Run Image
```
sudo docker run -p 8000:8000 -e OPEN_WEATHER_API='api here' my-python-app

