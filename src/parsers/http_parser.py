def parse_http(http: str):
    request, *headers, _, body = http.split("\r\n")
    method, path, protocol = request.split(" ")
    headers = {
        line.split(":", maxsplit=1)[0].strip(): line.split(":", maxsplit=1)[1].strip()
        for line in headers
    }
    return {
        "method": method,
        "path": path,
        "protocol": protocol,
        "headers": headers,
        "body": body,
    }
