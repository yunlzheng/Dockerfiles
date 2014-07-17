FROM cloud/base

RUN apt-get update

ENV TOMCAT_VERSION 7.0.53
ENV CATALINA_HOME /opt/tomcat7

RUN wget http://archive.apache.org/dist/tomcat/tomcat-7/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O tomcat.tar.gz
RUN tar zxf tomcat.tar.gz && rm tomcat.tar.gz && mv apache-tomcat* ${CATALINA_HOME}
ADD ./run.sh /usr/local/bin/run_tomcat7
EXPOSE 8080
CMD ["/bin/sh", "-e", "/usr/local/bin/run_tomcat7"]
