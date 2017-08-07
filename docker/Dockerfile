FROM java:8

RUN echo '    StrictHostKeyChecking  no' >> /etc/ssh/ssh_config

RUN apt-get update && \
     apt-get install --no-install-recommends -y \
     git \
     curl && \
    apt-get autoremove -y

# Install Docker Client
RUN curl -s -L https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 > /usr/bin/docker; chmod +x /usr/bin/docker

# Install Sonar Scanner
ADD http://of9tskapv.bkt.clouddn.com/sonar-scanner-2.8.zip /usr/local
RUN cd /usr/local/ && unzip sonar-scanner-2.8.zip && rm *.zip

# Install Docker Compose
RUN curl -L "http://of9tskapv.bkt.clouddn.com/docker-compose-Linux-x86_64" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Install Rancher Compose
ADD http://of9tskapv.bkt.clouddn.com/rancher-compose-linux-amd64-v0.8.6.tar.gz /usr/local
ADD http://of9tskapv.bkt.clouddn.com/US_export_policy.jar /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security
ADD http://of9tskapv.bkt.clouddn.com/local_policy.jar /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security

RUN cd /usr/local/ && tar -xzvf rancher-compose-linux-amd64-v0.8.6.tar.gz && mv /usr/local/rancher-compose-v0.8.6/rancher-compose /usr/local/bin/ && rm -rf *.gz
