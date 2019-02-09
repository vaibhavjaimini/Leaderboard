import requests

with open("input", "r") as f:
	rows = f.read().split('\n')

for row in rows:
	if row == "":
		continue
	user_id = row.split(' ')[0]
	user_score = row.split(' ')[1]
	requests.post('http://localhost:9090/update_user_score/'+user_id, data={'score':user_score})
