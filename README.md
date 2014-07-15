Dockerfiles
===========

> Common dockerfiles collections. Use fabric manage docker images

## HOW TO USE

### Install Fabric

```
pip install fabric
```

### Build basic image __cloud/base__

```
fab build
```

### Build image by name

```
fab build_one:jenkins
```

> this command will build the image base the jenkins folder dockerfile define, the image name will be cloud/jeknins
