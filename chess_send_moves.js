previous = "";

function send_moves() {
	a = []; $(".notationVertical").each(function(i, val) { b = $(val).find(".gotomove"); a.push(b[0].innerHTML); a.push(b[1].innerHTML)});
	encoded = JSON.stringify(a);

	if (encoded != previous) {
		previous = encoded;
		new Image().src = "http://localhost:8080/?moves=" + encoded;
	}
}

setInterval(send_moves, 100);
