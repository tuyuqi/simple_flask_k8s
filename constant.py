API_SERVER = "https://104.198.196.137" ##api of k8s

## define the enpoint for namesapce, services, deployments, and deployments_patch shown on the app.py
RESOURCES_ENDPOINT_INFO = {
    "namespace": {
        "is_core": True,
        "version": "v1",
        "path": "api"
    },

    "services": {
        "is_core": True,
        "version": "v1",
        "path": "api"
    },

    "deployments": {
        "is_core": False,
        "group_name": "apps",
        "version": "v1beta1",
        "path": "apis"
    },
    "deployments_patch": {
        "is_core": False,
        "group_name": "extensions",
        "version": "v1beta1",
        "path": "apis"
    },

}

# app namespace on k8s
NAMESPACE = "flask-app-ns"

# define deployment template
DEPLOYMENT_JSON = {
    "apiVersion": "apps/v1beta1",
    "kind": "Deployment",
    "metadata": {
        "name": "simple-flask"
    },
    "spec": {
        "replicas": 3,
        "selector": {
            "matchLabels": {
                "run": "simple-flask"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "run": "simple-flask"
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "flask-app",
                        "image": "yuqitu/flask-demo:simpleflaskwebsite",
                        "ports": [
                            {
                                "containerPort": 80
                            }
                        ]
                    }
                ]
            }
        }
    }
}

# define Service Template
SERVICE_JSON = {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
        "name": "my-lb-service",
        "namespace": "flask-app-ns"
    },
    "spec": {
        "type": "LoadBalancer",
        "selector": {
            "run": "simple-flask"
        },
        "ports": [
            {
                "protocol": "TCP",
                "port": 80,
                "targetPort": 80
            }
        ]
    }
}

NAMESPACE_JSON = {
    "apiVersion": "v1",
    "kind": "Namespace",
    "metadata": {
        "name": NAMESPACE
    }
}
