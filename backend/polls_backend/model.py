from secrets import token_hex


class Model:

    def __init__(self, db):
        self.db = db

    async def list_polls(self):
        poll_docs = await self.db['polls'].find().to_list(None)
        return [Poll(doc) for doc in poll_docs]

    async def get_poll(self, poll_id):
        return Poll(await self.db['polls'].find_one({'_id': poll_id}))

    async def create_poll(self, title):
        doc = {
            '_id': token_hex(4),
            'title': title,
        }
        await self.db['polls'].insert_one(doc)
        return Poll(doc)


class Poll:

    def __init__(self, doc):
        self.id = doc['_id']
        self.title = doc['title']
