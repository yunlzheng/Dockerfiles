Dockerfiles
===========

> Common dockerfiles collections. Use fabric manage docker images

## Basic Env

### Install Fabric

```
pip install fabric
```



## HOW TO USE

### Build basic image __cloud/base__

```
fab build
```

### Build image by name

```
fab build_one:jenkins
```

> this command will build the image base the jenkins folder dockerfile define, the image name will be cloud/jeknins
