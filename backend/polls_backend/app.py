from aiohttp.web import Application, RouteTableDef, Response
from aiohttp_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor
from .graphql import graphql_schema

routes = RouteTableDef()

@routes.get('/')
def index(request):
    return Response(text='Hello World! This is polls_backend.\n')

application = Application()
application.add_routes(routes)
GraphQLView.attach(application, schema=graphql_schema, graphiql=True, executor=AsyncioExecutor())
