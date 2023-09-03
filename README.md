### Demo for webapp

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

