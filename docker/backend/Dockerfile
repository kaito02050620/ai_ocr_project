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

RUN wget https://archive.apache.org/dist/tomcat/tomcat-11/v11.0.9/bin/apache-tomcat-11.0.9.tar.gz \
    && tar -xzf apache-tomcat-11.0.9.tar.gz \
    && mv apache-tomcat-11.0.9 /opt/tomcat \
    && rm apache-tomcat-11.0.9.tar.gz

# buildツールをダウンロード（gradle）
RUN wget https://services.gradle.org/distributions/gradle-9.1.0-rc-2-bin.zip -P /tmp && \
unzip -d /opt/gradle /tmp/gradle-9.1.0-rc-2-bin.zip && \
ln -s /opt/gradle/gradle-9.1.0-rc-2/bin/gradle /usr/bin/gradle
    
RUN mkdir -p /app/logs /app/build /app/python

ENV TZ=Asia/Tokyo
ENV PYTHONPATH=/app/python
ENV JAVA_HOME=/usr/local/openjdk-26
ENV PATH=/opt/tomcat/bin:$PATH

# Tomcat の自動デプロイ設定 削除しないとtomcatの初期画面が出る。
RUN rm -rf /usr/local/tomcat/webapps/*

CMD ["/bin/bash"]