from io import StringIO


class HTTP_Request:
    def __init__(self, **kwargs) -> None:
        self.method = kwargs.get("method")
        self.path = kwargs.get("path")
        self.protocol = kwargs.get("protocol")
        self.headers = kwargs.get("headers")
        self.body = kwargs.get("body")

    def to_environ(self) -> dict[str]:
        return {
            "REQUEST_METHOD": self.method,
            "PATH_INFO": self.path,
            "SERVER_PROTOCOL": self.protocol,
            "wsgi.input": StringIO(self.body),
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            # "wsgi.url_scheme": ,
            **self._format_headers(),
        }

    def _format_headers(self):
        formatted_headers = {
            "HTTP_" + key.replace("-", "_"): value
            for key, value in self.headers.items()
        }
        return formatted_headers
