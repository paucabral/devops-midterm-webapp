#!/bin/bash


docker build -t designapp .
docker run -t -d -p 8080:8080 --name designrun designapp
docker ps -a