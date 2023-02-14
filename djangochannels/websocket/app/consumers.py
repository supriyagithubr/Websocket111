from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected...', event)
        self.send({
            'type':'websocket.accept',
        })

    def websocket_recieve(self, event):
        print('message recieved from client', event)
        print(event['text'])
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(1)


    def websocket_disconnect(self,event):
        print('websocket disconnected..', event)
        raise StopConsumer


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket Connected....', event)
        await self.send ({
            'type':'websocket.send'

        })
        await asyncio.sleep(1)


    async def websocket_disconnect(self, event):
        print('websocket disconnected..', event)
        raise StopConsumer()