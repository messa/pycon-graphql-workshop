import asyncio
from graphene import Schema, ObjectType, Field, Mutation
from graphene import Int, String, DateTime, Boolean, List
from graphene.relay import Node as RelayNode, Connection, ConnectionField
from .. import model


# Documentation: https://docs.graphene-python.org/en/latest/types/schema/


class Node (RelayNode):

    @staticmethod
    def resolve_type(instance, info):
        if isinstance(instance, model.Poll):
            return Poll
        raise Exception(f'Unknown type: {instance!r}')


class PollChoice (ObjectType):

    key = Field(String)
    text = Field(String)

    def resolve_key(choice, info):
        return choice['key']

    def resolve_text(choice, info):
        return choice['text']


class Poll (ObjectType):

    class Meta:
        interfaces = (Node, )

    @classmethod
    async def get_node(cls, info, id):
        model = info.context['request'].app['model']
        return await model.get_poll(id)

    poll_id = Field(String)
    title = Field(String)
    choices = Field(List(PollChoice))

    def resolve_poll_id(poll, info):
        return poll.id


class PollConnection (Connection):

    class Meta:
        node = Poll


class Query (ObjectType):

    node = Node.Field()
    hello = Field(String, name=String(required=False))
    polls = ConnectionField(PollConnection)

    async def resolve_hello(root, info, name='World'):
        await asyncio.sleep(1)
        return f"Hello, {name}!"

    async def resolve_polls(root, info):
        model = info.context['request'].app['model']
        return await model.list_polls()


class CreatePoll (Mutation):

    class Arguments:
        title = String()
        choices = List(String)

    poll = Field(Poll)

    async def mutate(root, info, title, choices):
        model = info.context['request'].app['model']
        poll = await model.create_poll(title=title, choices=choices)
        return CreatePoll(poll=poll)


class Mutations (ObjectType):

    create_poll = CreatePoll.Field()


graphql_schema = Schema(query=Query, mutation=Mutations)
