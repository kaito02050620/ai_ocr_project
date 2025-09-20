FROM eclipse-temurin:21-jdk

WORKDIR /app

# TODO: 固定pythonバージョンインストール処理は後でやる。おそらくwgetでダウンロードしてパスを通す？
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        wget \
        zip \
        unzip \
        git \
        vim \
        nano \
        libopencv-dev \
        nvidia-cuda-toolkit \
        libnvidia-compute-575 \
        fonts-noto-cjk \
        fonts-noto-cjk-extra \
        curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# tomcatダウンロード
RUN wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.109/bin/apache-tomcat-9.0.109.tar.gz \
    && tar -xzf apache-tomcat-9.0.109.tar.gz \
    && mv apache-tomcat-9.0.109 /app/tomcat \
    && rm apache-tomcat-9.0.109.tar.gz

# buildツールをダウンロード（gradle）
RUN wget https://services.gradle.org/distributions/gradle-9.1.0-rc-2-bin.zip -P /tmp && \
unzip -d /opt/gradle /tmp/gradle-9.1.0-rc-2-bin.zip && \
ln -s /opt/gradle/gradle-9.1.0-rc-2/bin/gradle /usr/bin/gradle
    
RUN fc-cache -fv

ENV TZ=Asia/Tokyo
ENV PYTHONPATH=/app/python
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$JAVA_HOME/bin:/app/tomcat/bin:$PATH

# Tomcat の自動デプロイ設定 削除しないとtomcatの初期画面が出る。
RUN rm -rf /app/tomcat/webapps/*

CMD ["/bin/bash"]