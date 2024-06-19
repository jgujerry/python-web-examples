from sanic.response import json
from sanic import Blueprint


bp = Blueprint('auth')


@bp.route('/login', methods=['POST'])
async def login(request):
    return json({'message': 'User does not exist'})

