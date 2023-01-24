# G42-Test
##This is the assignment for SRE role at G42. 
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

Developing the app in Python,
Using Redis for database - cos its easier to setup and good support, documentations and tutorials available for easier setup. 

Endpoints:
- /health for health check
- /city to add or update the city population
- /city/<name> for getting the population of the given city.

