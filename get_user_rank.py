from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
import redis_dal

class GetUserRank(Resource):
	def get(self):
		user_id = request.args["id"]
		user_score = redis_dal.get_user_score(user_id)
		rank = 1
		for score in range(100, user_score, -1):
			rank += redis_dal.get_score_counter(score)

		result = {"user_id": user_id, "rank": rank, "score": user_score}
		return jsonify(result)

