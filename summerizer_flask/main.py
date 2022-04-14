import argparse
import os
from flask import Flask
from views import summarize


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    app.register_blueprint(summarize.bp)
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-debugging", action="store_true")
    args = parser.parse_args()
    app = create_app({"TESTING": args.debugging})
    if args.debugging:
        port = 5000
    else:
        port = 80
    app.run(host="0.0.0.0", port=port)
