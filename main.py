from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return "---"


api.add_resource(Hello, "/test")

if __name__ == "__main__":
    app.run(debug=True)
