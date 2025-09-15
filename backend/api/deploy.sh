#!/bin/bash

set -e

BUILD_SRC="/app/api/build/libs/ROOT.war"
DEPLOY_PATH="/app/tomcat/webapps"

# echo "===================== stop tomcat ====================="
./stop_tomcat.sh


# echo "===================== build java ====================="
gradle build


# echo "===================== remove tomcat file ====================="
rm -rf "$DEPLOY_PATH"/* || { echo "Failed to remove $DEPLOY_PATH"; exit 1; }


# echo "===================== copy build file ====================="
mkdir -p "$DEPLOY_PATH"
cp -r "$BUILD_SRC" "$DEPLOY_PATH" || { echo "Failed to copy build files"; exit 1; }


# echo "===================== start tomcat ====================="
./start_tomcat.sh || { echo "Failed to start Tomcat"; exit 1; }