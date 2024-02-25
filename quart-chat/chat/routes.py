import asyncio
from quart import Blueprint, render_template, websocket

from chat.broker import Broker

blueprint = Blueprint("app", __name__)
broker = Broker()


@blueprint.route("/")
async def index():
    return await render_template("index.html")


async def _receive() -> None:
    while True:
        message = await websocket.receive()
        await broker.publish(message)


@blueprint.websocket("/ws")
async def ws() -> None:
    try:
        task = asyncio.create_task(_receive())
        async for message in broker.subscribe():
            await websocket.send(message)
    finally:
        task.cancel()
        await task
