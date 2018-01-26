from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    data = env['QUERY_STRING']
    message = 'Hello World!!!' + '\n' + data
    return ([bytes(message,'utf-8')])