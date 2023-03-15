from io import StringIO


class HTTPRequest:
    def __init__(self, **kwargs) -> None:
        self.method: str = kwargs.get("method", "")
        self.path: str = kwargs.get("path", "")
        self.protocol: str = kwargs.get("protocol", "")
        self.headers: dict[str] = kwargs.get("headers", {})
        self.body: str = kwargs.get("body", "")

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

    def to_string(self) -> str:
        if self.method == "" or self.path == "" or self.protocol == "":
            return "None"
        request_string = f"{self.method} {self.path} {self.protocol}\r\n"
        for header, value in self.headers.items():
            request_string += f"{header}: {value}\r\n"
        request_string += f"\r\n{self.body}"
        return request_string

    def _format_headers(self):
        formatted_headers = {
            "HTTP_" + key.replace("-", "_"): value
            for key, value in self.headers.items()
        }
        return formatted_headers
