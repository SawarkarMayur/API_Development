from flask import Flask
from flask_restful import Resource,Api


app= Flask(__name__)

api = Api(app)

class Hi(Resource):
    def get(self):
        return {'Hello':'World'}

api.add_resource(Hi,'/')

if __name__ == "__main__":
    app.run(debug=True)
