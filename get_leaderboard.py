from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
import redis_dal
import constants

class GetLeaderBoard(Resource):
        def get(self):
                offset = int(request.args["offset"])
                leaderboard = redis_dal.get_leaderboard()
                total_user_count = len(leaderboard)
                leaderboard_with_rank = []
                previous_score = -1
                current_rank = 1
                counter = 1
                for player in leaderboard:
                        user_id = str(player[0])
                        user_score = int(player[1])
                        if user_score != previous_score:
                                current_rank = counter
                        user_rank = current_rank
                        counter += 1
                        previous_score = user_score
                        leaderboard_with_rank.append({
                                "user_id":user_id,
                                "user_score":user_score,
                                "user_rank": user_rank}
                                )
                leaderboard_page = leaderboard_with_rank[offset:min(offset+constants.PAGE_SIZE,total_user_count)]
                return jsonify(leaderboard_page)


