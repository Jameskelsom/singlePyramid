from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon') #add template
    config.add_route('home', '/')
    config.add_route('hello', '/howdy/{first}/{last}')
    config.add_route('redirect', '/goto')
    config.add_route('exception', '/problem')
    config.scan('views')  # read views
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
