#!/bin/bash


docker build -t designapp .
docker run -t -d -p 5050:5050 --name designrun designapp
docker ps -a