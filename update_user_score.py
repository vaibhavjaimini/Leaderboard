from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
import redis_dal

class UpdateUserScore(Resource):
	def post(self, user_id):
		user_score = request.form["score"]
		redis_dal.update_user_score(user_id, user_score)
		redis_dal.update_leaderboard()
		result = {"user_id": user_id, "score":user_score}
		return jsonify(result);
