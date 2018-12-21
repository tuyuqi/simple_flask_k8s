#!/bin/bash

##clone the github repo of WebSite and Dockerfile
git clone https://3caa02e0948b68640d4b36521dc20ab8e63bafb2@github.com/tuyuqi/docker_flask.git /tmp/docker_flask

##save the dockerhub login infomation
cat /home/yuqi_tu/my_password.txt | docker login --username yuqitu --password-stdin

##build docker image
docker build -t yuqitu/flask-demo:simpleflaskwebsite /tmp/docker_flask/

##push the docker image to the dockerhub for further deployment
docker push yuqitu/flask-demo:simpleflaskwebsite

## remove the directory after pushed
rm -rf /tmp/docker_flask/
