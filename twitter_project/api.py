
import asyncio
import aiohttp
from guillotina import configure
from guillotina.interfaces import IResource
from guillotina.api.service import Service
from aiohttp import ClientError

@configure.service(name='@twitter', method='POST', content=IResource,
                    permission='guillotina.AccessContent')
class MyService(Service):
    @staticmethod
    def get_twitter_url():
        # TODO that should go into configuration file
        return 'https://api.twitter.com/1.1/statuses/update.json'

    @staticmethod
    async def authenticate():
        # TODO authentication against twitter api
        return "this must be done"

    @staticmethod
    async def make_tweet(status, token):
        parameters ={}

        parameters["status"] = status
        headers={}
        # TODO use the token in the headers to build authorization
        async with aiohttp.ClientSession() as session:
            resp = await session.post(MyService.get_twitter_url(), params=parameters, headers=headers)
            text = await resp.json()
        return text

    async def __call__(self):
        input_data = await self.get_data()
        if "status" not in input_data:
            # TODO raise builtin exception that can convert on a bad request
            raise Exception("400")
        status = input_data["status"]
        try:
            token = await self.authenticate()
            r = await self.make_tweet(status, token)
        except ClientError as e:
            # ToDO raise builtin exception that can convert into connection error or alike
            raise Exception(503)
        return r
