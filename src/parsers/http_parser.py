def parse_http(http: str):
    request, *headers, _, body = http.split("\r\n")
    method, path, protocol = request.split(" ")
    headers = dict(line.split(":", maxsplit=1) for line in headers)
    return method, path, protocol, headers, body
