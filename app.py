from flask import Flask, request, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        x={"data": 'Helloworld'}
        y = x["data"]
        print(y)
        return y

class Video(Resource):
    def get(self):
        return render_template("index.html")

api.add_resource(Helloworld, "/helloworld")
api.add_resource(Video, "/")
if __name__ == '__main__':
    app.run(debug=True)