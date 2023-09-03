### Demo for webapp

About

Small web app that displays the visitor IP in reverse.



## Docker steps:

Build image:

```
docker build --tag webapp-docker .
```

Run container (default port for Flask app is 5000):

```
docker run -d -p 80:5000 webapp-docker
```

## Helm steps:

```
helm install webapp-chart helmchart/webapp/ --values helmchart/webapp/values.yaml
```

## Github actions::

There is one action that will build the Docker container image and push it as Github package
