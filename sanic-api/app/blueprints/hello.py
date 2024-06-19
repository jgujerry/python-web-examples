from sanic.response import json
from sanic import Blueprint


bp = Blueprint('hello')


@bp.route('/hello', methods=['GET'])
async def hello(request):
    return json({'message': 'Hello world!'})
