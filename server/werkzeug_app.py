#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__=='__main__':
    from werkzeug.serving import run_simple  #this requires 3 arguments: 1. a hostname   2. a port   3. an application (this will be defined in a function somewhere in the file)
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )