#!/bin/bash

set -e

BUILD_SRC="/app/api/build/libs/ROOT.war"
DEPLOY_PATH="/app/tomcat/webapps"

# echo "===================== stop tomcat ====================="
catalina.sh stop


# echo "===================== build java ====================="
gradle build


# echo "===================== remove tomcat file ====================="
rm -rf "$DEPLOY_PATH"/* || { echo "Failed to remove $DEPLOY_PATH"; exit 1; }


# echo "===================== copy build file ====================="
mkdir -p "$DEPLOY_PATH"
cp -r "$BUILD_SRC" "$DEPLOY_PATH" || { echo "Failed to copy build files"; exit 1; }


# echo "===================== start tomcat ====================="
catalina.sh start || { echo "Failed to start Tomcat"; exit 1; }