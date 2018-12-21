from constant import NAMESPACE, NAMESPACE_JSON
from k8s.base.base_resource import BaseResource
from k8s.exception.k8s_exception import K8sException

## write the CLASS for creating NameSpace
class NameSpace(BaseResource):
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
        obj = NameSpace()
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
        obj = NameSpace()
        try:
            response = obj.add_resource(namespace=NAMESPACE, resource_name="", resource_body=NAMESPACE_JSON)
            return dict(
                status_code=response["status_code"],
                status=response["status"]["phase"],
            )
        except K8sException as e:
            return dict(
                status_code=str(e.status_code),
                reason=e.reason,
                status=e.status,
                message=e.message
            )

    def patch(self):
        pass
