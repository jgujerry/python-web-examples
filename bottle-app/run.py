from bottle import run

from app import app


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True)
