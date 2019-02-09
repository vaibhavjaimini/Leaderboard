from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
from get_user_rank import GetUserRank
from update_user_score import UpdateUserScore
from get_leaderboard import GetLeaderBoard

app = Flask(__name__)
api = Api(app)

api.add_resource(GetUserRank, '/get_user_rank/')
api.add_resource(GetLeaderBoard, '/get_leaderboard/')
api.add_resource(UpdateUserScore, '/update_user_score/<string:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
