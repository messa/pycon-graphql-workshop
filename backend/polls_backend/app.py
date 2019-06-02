from aiohttp.web import Application, RouteTableDef, Response
from aiohttp_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor
from motor.motor_asyncio import AsyncIOMotorClient
import os
from .graphql import graphql_schema
from .model import Model

routes = RouteTableDef()

@routes.get('/')
def index(request):
    return Response(text='Hello World! This is polls_backend.\n')

application = Application()
application.add_routes(routes)
GraphQLView.attach(application, schema=graphql_schema, graphiql=True, executor=AsyncioExecutor())

# example how the full connection (MONGO_URI) string looks like:
# "mongodb+srv://user0:PaSsWoRd@cluster0-zzj1c.mongodb.net/test?retryWrites=true&w=majority"

client = AsyncIOMotorClient(os.environ['MONGO_URI'])
db_name = os.environ.get('MONGO_DB_NAME') or 'poll_app'
db = client[db_name]

application['model'] = Model(db)
