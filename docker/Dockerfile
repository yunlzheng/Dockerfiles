FROM java:8

RUN echo '    StrictHostKeyChecking  no' >> /etc/ssh/ssh_config

RUN apt-get update && \
     apt-get install --no-install-recommends -y \
     git \
     curl && \
    apt-get autoremove -y
RUN curl -s http://stedolan.github.io/jq/download/linux64/jq > /usr/bin/jq; chmod +x /usr/bin/jq
RUN curl -s -L https://get.docker.com/builds/Linux/x86_64/docker-1.6.0 > /usr/bin/docker; chmod +x /usr/bin/docker
RUN curl -s -L https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 > /usr/bin/docker-1.9; chmod +x /usr/bin/docker-1.9

RUN cd /usr/local/ && tar -xzvf -C rancher-compose rancher-compose-linux-amd64-v0.8.6.tar.gz && rm -rf *.gz
