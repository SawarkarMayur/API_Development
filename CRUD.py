from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

#{'name':'Amaze'}
cars = []

class CarNames(Resource):

    def get(self,name):
        for car in cars:
            if car['name'] == name:
                return car
        return {'name':None}, 404


    def post(self,name):
        car = {'name':name}
        cars.append(car)
        return car

    def delete(self,name):

        for indx,car in enumerate(cars):
            if car ['name'] == name:
                deleted_car = cars.pop(indx)
                print(deleted_car)
                return {'note':'Delete Sucess'}

class AllNames(Resource):

    def get(self):
        return {'cars':cars}

api.add_resource(CarNames,'/car/<string:name>')
api.add_resource(AllNames,'/cars')

if __name__ == '__main__':
    app.run(debug=True)