FROM cloud/java7

RUN apt-get update && apt-get clean
ADD http://mirrors.jenkins-ci.org/war/1.572/jenkins.war /opt/jenkins.war
RUN chmod 644 /opt/jenkins.war
ENV JENKINS_HOME /jenkins

ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]
EXPOSE 8080
CMD [""]
