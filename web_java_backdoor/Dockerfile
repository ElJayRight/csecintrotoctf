FROM fabric8/tomcat-7
# Change default pwd
USER root
RUN echo "CSEC{J4v4_0n3L1n3r5_4r3_w31rD}" > /root/flag.txt
RUN chmod 400 /root/flag.txt
RUN echo 'root:unguessablepassword' | chpasswd
RUN echo 'root password : unguessablepassword' > /note.md
RUN rm /usr/bin/curl
RUN chown jboss:jboss /note.md
# Add file
USER jboss
RUN echo 'root password : unguessablepassword' > /note.md
RUN rm /opt/apache-tomcat-7.0.90/conf/tomcat-users.xml
RUN  mkdir /opt/apache-tomcat-7.0.90/webapps/development
COPY ./src/index.jsp /opt/apache-tomcat-7.0.90/webapps/development/

EXPOSE 9001
EXPOSE 8080
# run the application
RUN /bin/sh -c /opt/tomcat/bin/startup.sh
