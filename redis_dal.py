from redis import Redis
import constants

def get_leaderboard():	
	redis_client = Redis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=0)
	leaderboard = redis_client.zrevrangebyscore("leaderboard", 100, 0, withscores=True)
	return leaderboard


def get_user_score(user_id):
	redis_client = Redis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=0)
	print(user_id)
	user_score = int(redis_client.get(user_id))	
	print(user_score)
	return int(user_score)

def get_score_counter(score):
	redis_client = Redis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=0)
	counter = redis_client.zscore(constants.SCORE_COUNTER_REDIS_KEY, score)
	if counter is None:
		counter = 0
	return counter

def update_user_score(user_id, user_score):
	redis_client = Redis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=0)
	if(redis_client.exists(user_id)):
		previous_score = redis_client.get(user_id)
		redis_client.zincrby(constants.SCORE_COUNTER_REDIS_KEY, previous_score, -1)

	redis_client.set(user_id, user_score)
	redis_client.zincrby(constants.SCORE_COUNTER_REDIS_KEY, user_score, 1)

	redis_client.zadd(constants.LEADERBOARD_REDIS_KEY, user_id, user_score)


def update_leaderboard():
	redis_client = Redis(host=constants.REDIS_HOST, port=constants.REDIS_PORT, db=0)
	leaderboard_count = redis_client.zcard(constants.LEADERBOARD_REDIS_KEY)
	if(leaderboard_count > constants.LEADERBOARD_LIMIT):
		redis_client.zremrangebyrank(constants.LEADERBOARD_REDIS_KEY, 0, leaderboard_count-constants.LEADERBOARD_LIMIT-1)
