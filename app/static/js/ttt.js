var req_addr = "http://130.245.171.50/ttt/play/";
var xhr = new XMLHttpRequest();
var winner = "";

$(document).ready(function() {
	$('#grid td').click(function(e) {
		console.log(e);
		e.target.innerHTML = 'X';

		grid = getCurrentGrid();

		var game = new Object();
		game.winner = winner;
		game.grid = grid;

		var jsonGame = JSON.stringify(game);
		checkWinner(jsonGame);
		processMove(jsonGame);
	});
});

function processMove(jsonGame) {
	xhr.open('POST', req_addr, true)
	xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-9');
	xhr.send(jsonGame);
	console.log("Sent: " + jsonGame);
	xhr.onreadystatechange = function()	{
		if(xhr.readyState == 4 && xhr.status == 200) {
			var json = xhr.responseText;
			console.log("Resp: " + json);
			updateBoard(json);
			checkWinner(json);
		}
	}
}

function getCurrentGrid() {
	var gridData = $('#grid').find('td');
	var grid = [];
	for(var i = 0; i < gridData.length; i++){
		grid[i] = gridData[i].innerHTML;
	}
	return grid;
}

/* Places marker for AI's turn */
function updateBoard(json) {
	var state_obj = JSON.parse(json);
	var grid = state_obj.grid;

	var grid_elem = $('#grid td');
	for(var i = 0; i < grid_elem.length; i++){
		grid_elem[i].innerHTML = grid[i];
	}
}

function checkWinner(json) {
	var state_obj = JSON.parse(json);
	var winner = state_obj.winner;

	if(winner != ""){
		alert(winner + " wins!");
	}
}
