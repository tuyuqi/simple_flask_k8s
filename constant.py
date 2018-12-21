API_SERVER = "https://104.198.196.137"

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

# app namespace
NAMESPACE = "flask-app-ns"

# deployment template
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

# Service Template
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
