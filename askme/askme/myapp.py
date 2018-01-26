def app(environ, start_response):
    info = bytes("Hello World\n", 'utf-8')
    if environ.get("REQUEST_METHOD") == 'GET' and environ["QUERY_STRING"]:
        print("Method: GET", '\n', environ["QUERY_STRING"] + '\n')
        info += bytes(environ["QUERY_STRING"] + '\n', 'utf-8')
    if environ["REQUEST_METHOD"] == 'POST' and environ["wsgi.input"]:
        print("Method: POST", '\n', environ["wsgi.input"].read() + '\n')
        info += bytes(environ["wsgi.input"].read() + '\n', 'utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)	
    return iter([info])