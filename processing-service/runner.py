import os

from app import create_app


if __name__ == "__main__":
    app = create_app()
    host = os.getenv("HOST", "localhost")
    app.run(host=host)
