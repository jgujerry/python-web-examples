from sanic.response import json


async def hello_world(request):
    """This is a hello world API example in Sanic

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return json({'message': 'Hello, world!'})
