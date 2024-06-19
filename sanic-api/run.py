import os
from app import create_app

env = os.getenv('SANIC_ENV', 'development')
app = create_app(env)


if __name__ == '__main__':
    if env == 'production':
        app.run(host='127.0.0.1', port=5000)
    else:
        app.run(host='127.0.0.1', port=5000, debug=True)
