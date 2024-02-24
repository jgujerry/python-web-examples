from quart_schema import QuartSchema
from api.app import create_app

app = create_app()
QuartSchema(app)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True, use_reloader=True)
