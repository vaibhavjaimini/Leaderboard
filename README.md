Run redis on port 6379

To run:
pip install -r requirements.txt
python3 apis.py

To seed initial data run:
python3 input_data.py

add rows to input file to add more initial data

Endpoints
localhost:9090/get_leaderboard?offset=<>

localhost:9090/get_user_rank?id=<>

localhost:9090/update_user_score/<id>
body: score=<score>

