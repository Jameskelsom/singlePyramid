import cgi

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


# First view, available at http://localhost:8080/
@view_config(route_name='home')
def hello_world(request):
    body = '<h1>Hi %(first)s %(last)s!</h1>' % request.matchdict
    return Response(body)


# /howdy?name=alice which links to the next view
@view_config(route_name='hello')
def hello_view(request):
    name = request.params.get('name', 'No Name')
    body = '<p>Hi %s, this <a href="/goto">redirects</a></p>'
    # cgi.escape to prevent Cross-Site Scripting (XSS) [CWE 79]
    return Response(body % cgi.escape(name))


# /goto which issues HTTP redirect to the last view
@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")


# /problem which causes a site error
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()