from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from algorithm import Astar

app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app,resources={
    r"/*" : {
        "origins" : "*"
    }
})

grid_data_parser = reqparse.RequestParser()
grid_data_parser.add_argument("grid_size",type=list)
grid_data_parser.add_argument("start_pos",type=list)
grid_data_parser.add_argument("end_pos",type=list)
grid_data_parser.add_argument("wall_list",type=list)

class alg_api(Resource):
    def post(self):
        args = grid_data_parser.parse_args()
        grid_size = args["grid_size"]
        start_pos = args["start_pos"]
        end_pos = args["end_pos"]
        wall_list = args["wall_list"]

        astar = Astar()
        finder = astar.PathFinding(grid_size,start_pos,end_pos,wall_list)
        path,visited = finder.run()
        return {"path":path,"visited":visited}

api.add_resource(alg_api,'/')

if __name__ == "__main__":
    app.run(debug=True)