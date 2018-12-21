from constant import NAMESPACE, DEPLOYMENT_JSON
from k8s.base.base_resource import BaseResource
from k8s.exception.k8s_exception import K8sException
import datetime

## write the CLASS for performing deployments

class Deployments(BaseResource):
    def __init__(self):
        BaseResource.__init__(self)
        self._name = ""

    @property
    def name(self):
        try:
            return self.name
        except Exception as e:
            raise e

    @classmethod
    def get(cls):
        obj = Deployments()
        try:
            response = obj.get_resource(namespace=NAMESPACE)
            return dict(
                status_code=response["status_code"],
                status="success",
            )
        except K8sException as e:
            return dict(
                status_code=e.status_code,
                reason=e.reason,
                status=e.status,
                message=e.message,
            )

    @classmethod
    def post(cls):
        obj = Deployments()
        resource_name = DEPLOYMENT_JSON["metadata"]["name"]
        try:
            response = obj.add_resource(namespace=NAMESPACE, resource_name=resource_name, resource_body=DEPLOYMENT_JSON)
            return dict(
                status_code=response["status_code"],
                status="success",
            )
        except K8sException as e:
            return dict(
                status_code=str(e.status_code),
                reason=e.reason,
                status=e.status,
                message=e.message
            )

    @classmethod
    def patch(cls):
        obj = Deployments()
        resource_name = DEPLOYMENT_JSON["metadata"]["name"]
        try:
            response = obj.patch_resource(namespace=NAMESPACE, resource_name=resource_name, resource_body=obj.get_patch_payload())
            return dict(
                status_code=response["status_code"],
                status="success",
            )
        except K8sException as e:
            return dict(
                status_code=str(e.status_code),
                reason=e.reason,
                status=e.status,
                message=e.message
            )

    @staticmethod
    def get_patch_payload():
        payload = {
            "spec": {
                "template": {
                    "metadata": {
                        "labels": {
                            "date": str(datetime.datetime.now().timestamp())
                        }
                    }
                }
            }
        }
        return payload
