import os, mimetypes

BASE_DIR = os.path.dirname(__file__)

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/').lstrip('/')
    if not path:
        path = 'index.html'
    file_path = os.path.join(BASE_DIR, path)
    if os.path.isfile(file_path):
        mime, _ = mimetypes.guess_type(file_path)
        with open(file_path, 'rb') as f:
            body = f.read()
        start_response('200 OK', [
            ('Content-Type', mime or 'application/octet-stream'),
            ('Content-Length', str(len(body)))
        ])
        return [body]
    with open(os.path.join(BASE_DIR, 'index.html'), 'rb') as f:
        body = f.read()
    start_response('404 Not Found', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ])
    return [body]
