import requests
import json
import abc
from config import GKE_TOKEN
from constant import RESOURCES_ENDPOINT_INFO, API_SERVER
from http import HTTPStatus
from k8s.exception.k8s_exception import K8sException


class BaseResource:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def post(self):
        pass

    @abc.abstractmethod
    def patch(self):
        pass

    @classmethod
    def get_object_type(cls):
        return cls.__name__

    def get_resource(self, namespace):
        try:
            obj_type = self.__class__.get_object_type().lower()
            path = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["path"]
            version = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["version"]
            if RESOURCES_ENDPOINT_INFO[obj_type]["is_core"]:
                url = API_SERVER + path + version + "/namespaces/" + namespace + '/' + obj_type
            else:
                group_name = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["group_name"]
                url = API_SERVER + path + group_name + version + "/namespaces/" + namespace + '/' + obj_type
            print(url)
            headers = {'Content-Type': 'application/json', 'Authorization': GKE_TOKEN}
            response = requests.get(url, headers=headers, verify=False)
            response_json = response.json()
            print(response_json)
            if response.status_code < HTTPStatus.BAD_REQUEST:
                raise K8sException(response.status_code, response_json["reason"], response_json["status"], response_json["message"])
            else:
                return response_json
        except Exception as e:
            print(e)
            raise e

    def add_resource(self, namespace, resource_name, resource_body):
        try:
            obj_type = self.__class__.get_object_type().lower()
            path = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["path"]
            version = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["version"]
            payload = json.dumps(resource_body)
            if RESOURCES_ENDPOINT_INFO[obj_type]["is_core"]:
                if obj_type == "namespace":
                    url = API_SERVER + path + version + "/namespaces"
                else:
                    url = API_SERVER + path + version + "/namespaces/" + namespace + '/' + obj_type
            else:
                group_name = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["group_name"]
                url = API_SERVER + path + group_name + version + "/namespaces/" + namespace + '/' + obj_type
            print(url)
            headers = {'Content-Type': 'application/json', 'Authorization': GKE_TOKEN}
            response = requests.post(url, headers=headers, data=payload, verify=False)
            response_json = response.json()
            print(response_json)
            if response.status_code >= HTTPStatus.BAD_REQUEST:
                raise K8sException(response.status_code, response_json["message"], response_json["status"], response_json["reason"])
            else:
                response_json["status_code"] = response.status_code
                return response_json
        except Exception as e:
            print(e)
            raise e

    def patch_resource(self, namespace, resource_name, resource_body):
        try:
            obj_type = self.__class__.get_object_type().lower()
            path = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["path"]
            version = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["version"]
            payload = json.dumps(resource_body)
            if RESOURCES_ENDPOINT_INFO[obj_type]["is_core"]:
                if obj_type == "namespace":
                    url = API_SERVER + path + version + "/namespaces"
                else:
                    url = API_SERVER + path + version + "/namespaces/" + namespace + '/' + obj_type + "/" + resource_name
            else:
                if obj_type == "deployments":
                    group_name = "/" + RESOURCES_ENDPOINT_INFO["deployments_patch"]["group_name"]
                    version = "/" + RESOURCES_ENDPOINT_INFO["deployments_patch"]["version"]
                else:
                    group_name = "/" + RESOURCES_ENDPOINT_INFO[obj_type]["group_name"]
                url = API_SERVER + path + group_name + version + "/namespaces/" + namespace + '/' + obj_type + "/" + resource_name
            print(url)
            headers = {'Content-Type': 'application/merge-patch+json', 'Authorization': GKE_TOKEN}
            response = requests.patch(url, headers=headers, data=payload, verify=False)
            response_json = response.json()
            print(response_json)
            if response.status_code >= HTTPStatus.BAD_REQUEST:
                raise K8sException(response.status_code, response_json["message"], response_json["status"], response_json["reason"])
            else:
                response_json["status_code"] = response.status_code
                return response_json
        except Exception as e:
            print(e)
            raise e