FROM java:8

RUN echo '    StrictHostKeyChecking  no' >> /etc/ssh/ssh_config

RUN apt-get update && \
     apt-get install --no-install-recommends -y \
     git \
     curl && \
    apt-get autoremove -y

RUN curl -s -L https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 > /usr/bin/docker; chmod +x /usr/bin/docker
