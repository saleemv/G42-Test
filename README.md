# G42-Test
### This is the assignment for SRE role at G42. 
```
Create an application in any programing language (Python preferred), which
maintains a list of cities and their population and exposes the following
endpoints:
- a health endpoint which returns OK
- an endpoint for inserting or updating a city and its population
- an endpoint for retrieving the population of a city
The data must be stored in a database (any database is accepted, Elasticsearch
preferred).
The application must be containerized, and packaged for deployment to
Kubernetes(Helm chart preferred).
Instructions for deploying the application (including the database) must also be
provided.
The solution must be shared back as a zip archive or the URL to a Github
repository.
```

Python Flask app, using Redis.

#### Docker/image details: 

| Details    | Details                                                                 |
|------------|-------------------------------------------------------------------------|
| Repo       | [saleemv](https://hub.docker.com/repository/docker/saleemv/g42/general) |
| Image      | g42                                                                     |
| Latest tag | latest                                                                  | 

#### Endpoints:
- _/health_  **[GET]** for health check
- _/city_ **[POST]** to add or update the city population
- _/city/\<name>_ **[POST]** for getting the population of the given city.

#### Deployment using K8

The k8 directory contains
1. Deployment yaml for application
2. Deployment yaml for redis
3. Persistent volume
4. Service - Nodeport (port 30003) for the app. (Optional - For setup before nginx ingress)
5. Service - ClusterIP for app. (Used by the nginx-ingress controller)
6. Service - ClusterIp for redis.
7. Ingress config files. Controller need to be installed using helm. We use this [ingress](https://kubernetes.github.io/ingress-nginx/deploy/#quick-start)

NOTE: The app accessible on port 30003 since I'm using NodePort service. Will be available on 80 after I set up Ingress

To deploy using K8 - 
` helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace `

`cd k8 && kubectl apply -f . ` 

#### Helm chart
All helm files in city-helm directory. But we need a storage for our redis, and we have the PVC yaml file K8 directory.
To create the pvc goto the k8 dir and `kubectl apply -f pvc.yaml`

To deploy:
```commandline
Goto city-helm dir
helm install city-helm .
```
