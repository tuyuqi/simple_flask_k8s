from flask import Flask
from k8s.resource.namspace import NameSpace
from k8s.resource.deployment import Deployments
from k8s.resource.service import Services
from flask import Response
import json
import subprocess

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# create new namespace
@app.route('/namespace')
def create_namespace():
    return Response(json.dumps(NameSpace().post()), mimetype="application/json")


# create new deployment
@app.route('/deployment')
def create_deployment():
    return Response(json.dumps(Deployments().post()), mimetype="application/json")


# auto update deployment
@app.route('/patch_deployment', methods=['GET', 'POST']) ##  call for deployment
def patch_deployment():
    return Response(json.dumps(Deployments().patch()), mimetype="application/json")


# create new service
@app.route('/service')
def create_service():
    return Response(json.dumps(Services().post()), mimetype="application/json")


@app.route('/build_docker_image', methods=['GET', 'POST']) ## pull updates from github and build image
def build_docker_iamge():
    subprocess.call(['/home/yuqi_tu/simple_flask_k8s/k8s/build_docker_image.sh']) ##
    data = {"status":"received"}
    return Response(json.dumps(data), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)
