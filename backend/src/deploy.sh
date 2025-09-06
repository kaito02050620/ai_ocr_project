#!/bin/bash

set -e

BUILD_SRC="/app/src/html/index.html"
REMOVE_PATH="/app/tomcat/webapps"
DEPLOY_PATH="/app/tomcat/webapps/ROOT"

echo "===================== stop tomcat ====================="
catalina.sh stop

echo "===================== build java ====================="
mkdir -p "/app/build"
# ここに Java ビルド処理がある場合は追加してください
# 例: javac -d ./../build $(find $BUILD_SRC -name "*.java") || exit 1

echo "===================== remove tomcat file ====================="
rm -rf "$REMOVE_PATH" || { echo "Failed to remove $REMOVE_PATH"; exit 1; }

echo "===================== copy build file ====================="
mkdir -p "$DEPLOY_PATH"
cp -r "$BUILD_SRC" "$DEPLOY_PATH" || { echo "Failed to copy build files"; exit 1; }

echo "===================== start tomcat ====================="
catalina.sh start || { echo "Failed to start Tomcat"; exit 1; }