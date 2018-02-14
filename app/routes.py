from flask import render_template, request, Response, jsonify
from app import app
from app.forms import LoginForm

import datetime, json

@app.route('/ttt/', methods=['GET','POST'])
def ttt():
	form = LoginForm()
	if form.validate_on_submit():
			print("Logged in!")
			name = form.name.data
			now = datetime.datetime.now()
			date_str = now.strftime("%Y-%m-%d %H:%M")
			return render_template('home.html', title="Play", name=name, date=date_str)
	return render_template('home.html', title='Sign In', form=form)


'''
Functions below are for tic tac toe game play
'''
@app.route('/ttt/play/', methods=['POST', 'GET'])
def play():
	req = request.get_json()
	print("Request: ", req)
	grid = req['grid']

	return make_response(grid)
	

def make_response(grid):
	resp_grid = grid
	resp_winner = get_winner(grid)


	# If winner not found, check again if computer is winner	
	if not resp_winner:
		resp_grid = make_move(grid)
		resp_winner = get_winner(resp_grid)

	resp_dict = {
		"grid": resp_grid,
		"winner": resp_winner
	}

	json_str = json.dumps(resp_dict)

	print("Response: ", json_str)
	return Response(json_str, status=200, mimetype='application/json')

def make_move(grid):
	for i in range(0, len(grid)):
		if grid[i] == '':
			grid[i] = 'O'
			return grid
	return grid

def get_winner(grid):
	# Check horizontal
	for i in range(0, len(grid), 3):
		if grid[i] != "" and grid[i] == grid[i+1] and grid[i] == grid[i+2]:
			return grid[i]

	# Check vertical
	for i in range(0, 3):
		if grid[i] != "" and grid[i] == grid[i+3] and grid[i] == grid[i+6]:
			return grid[i]

	# Check diagonals
	if grid[0] != "" and grid[0] == grid[4] and grid[0] == grid[8]:
		return grid[0]
	if grid[2] != "" and grid[2] == grid[4] and grid[2] == grid[6]:
		return grid[2]
		
	return ""