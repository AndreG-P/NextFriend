var socket = 0;
var socketOpen = 0;
function init(){
	var url = "ws://ec2-52-28-160-147.eu-central-1.compute.amazonaws.com:80/ws";
	socket = new WebSocket( url );
	socket.onopen = function(){
		socketOpen = 1;
	};
	socket.onmessage = function(evt) { 
	    alert("received "+evt.data) 
	};
	
}

function submitted(){
	var field = document.getElementById("name");
	socket.send(field.value);
}