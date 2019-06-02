from aiohttp.web import Application, RouteTableDef, Response

routes = RouteTableDef()

@routes.get('/')
def index(request):
    return Response(text='Hello World! This is polls_backend.\n')

application = Application()
application.add_routes(routes)
