## ## write the CLASS for checking the information of k8s deployment

class K8sException(Exception):
    _reason = ""
    _status = ""
    _message = ""
    _status_code = 0

    def __init__(self, status_code=0, reason="", status="", message=""):
        self._reason = reason
        self._status = status
        self._message = message
        self._status_code = status_code

    @property
    def status_code(self):
        return self._status_code

    @property
    def message(self):
        return self._message

    @property
    def reason(self):
        return self._reason

    @property
    def status(self):
        return self._status
