import asyncio
from graphene import Schema, ObjectType, Field
from graphene import Int, String, DateTime, Boolean, List
from graphene.relay import Node, Connection, ConnectionField


class Query (ObjectType):

    node = Node.Field()
    hello = Field(String, name=String(required=False))

    async def resolve_hello(info, root, name='World'):
        await asyncio.sleep(1)
        return f"Hello, {name}!"


graphql_schema = Schema(query=Query)
