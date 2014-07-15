Jenkins Dockerfile
=================

## How to use

1, build base image

Go to __../base__

```
docker build -t base/java7 .
``

2, build jenkins image

Go to __../jenkins__


```
docker build -t base/jenkins .
```

3, run jenkins container

```
docker run -d 0.0.0.0:8080:8080 base/jenkins
```
