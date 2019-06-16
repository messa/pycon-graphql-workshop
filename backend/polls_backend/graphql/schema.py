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
        raise Exception('Unknown type: {!r}'.format(instance))


class PollChoice (ObjectType):

    key = Field(String)
    text = Field(String)
    vote_count = Field(Int)

    def resolve_key(choice, info):
        return choice['key']

    def resolve_text(choice, info):
        return choice['text']

    async def resolve_vote_count(choice, info):
        #return 42
        #print("XXX choice:", choice)
        model = info.context['request'].app['model']
        count = await model.get_vote_count(choice['poll_id'], choice['key'])
        return count


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
        return "Hello, {name}!".format(name=name)

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


class Vote (Mutation):

    class Arguments:
        poll_id = String(required=True)
        choice_key = String(required=True)

    poll = Field(Poll)

    async def mutate(root, info, poll_id, choice_key):
        model = info.context['request'].app['model']
        await model.create_vote(poll_id=poll_id, choice_key=choice_key)
        poll = await model.get_poll(poll_id)
        return Vote(poll=poll)


class Mutations (ObjectType):

    create_poll = CreatePoll.Field()
    vote = Vote.Field()


graphql_schema = Schema(query=Query, mutation=Mutations)











#
