Forecast API
===================

TODO: Add usage documentation

### Checkout Flasgger API Docs

`http://localhost:5000/apidocs`

### Get Container Image

```
docker pull ireynaldo/forecastapi
```

### Run Docker Container

```
docker run -p 5000:5000 -d --name api ireynaldo/forecastapi
```

### Stop Container

```
docker stop api
```

### Remove Container

```
docker rm api
```

### Update Image

```
docker rmi ireynaldo/forecastapi
docker pull ireynaldo/forecastapi
```
