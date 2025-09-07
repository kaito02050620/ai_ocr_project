FROM eclipse-temurin:21-jdk

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        wget \
        zip \
        unzip \
        git \
        vim \
        nano \
        curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# tomcatダウンロード
RUN wget https://archive.apache.org/dist/tomcat/tomcat-10/v10.1.9/bin/apache-tomcat-10.1.9.tar.gz \
    && tar -xzf apache-tomcat-10.1.9.tar.gz \
    && mv apache-tomcat-10.1.9 /app/tomcat \
    && rm apache-tomcat-10.1.9.tar.gz

# buildツールをダウンロード（gradle）
RUN wget https://services.gradle.org/distributions/gradle-9.1.0-rc-2-bin.zip -P /tmp && \
unzip -d /opt/gradle /tmp/gradle-9.1.0-rc-2-bin.zip && \
ln -s /opt/gradle/gradle-9.1.0-rc-2/bin/gradle /usr/bin/gradle
    
RUN mkdir -p /app/python

ENV TZ=Asia/Tokyo
ENV PYTHONPATH=/app/python
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$JAVA_HOME/bin:/app/tomcat/bin:$PATH

# Tomcat の自動デプロイ設定 削除しないとtomcatの初期画面が出る。
RUN rm -rf /app/tomcat/webapps/*

CMD ["/bin/bash"]