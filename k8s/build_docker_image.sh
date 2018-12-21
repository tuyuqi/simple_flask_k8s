#!/bin/bash

git clone https://3caa02e0948b68640d4b36521dc20ab8e63bafb2@github.com/tuyuqi/docker_flask.git /tmp/docker_flask

cat /home/yuqi_tu/my_password.txt | docker login --username yuqitu --password-stdin

docker build -t yuqitu/flask-demo:simpleflaskwebsite /tmp/docker_flask/

docker push yuqitu/flask-demo:simpleflaskwebsite

rm -rf /tmp/docker_flask/
