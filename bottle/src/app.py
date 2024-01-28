from bottle import Bottle, run
from routes.home import home_router

app = Bottle()

# Mount route handlers
app.mount("/a", home_router)


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True)
