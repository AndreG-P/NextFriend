var socket = 0;
var socketOpen = 0;
function init(){
	var url = "ws://ec2-52-28-160-147.eu-central-1.compute.amazonaws.com:80/ws";
	socket = new WebSocket( url );
	socket.onopen = function(){
		socketOpen = 1;
	};
	socket.onmessage = function(evt) { 
	    var name = getNameFromMessage(evt.data);
	    var latitude = getLatitudeFromMessage(evt.data);
	    var longitude = getLongitudeFromMessage(evt.data);

	    // here call to start navigation
	    alert('name='+name+',lat='+latitude+',lng='+longitude);
	};
	
}

function getNameFromMessage(m){
	var name = m.split('#')[0];
	return name;
}

function getLatitudeFromMessage(m){
	var latlong = m.split('#')[1];
	var lat = latlong.split('/')[0];
	return lat;
}

function getLongitudeFromMessage(m){
	var latlong = m.split('#')[1];
	var lng = latlong.split('/')[1];
	return lng;
}


function submitted(){
	var field = document.getElementById("name");
	var m = field.value+"#"+"12.3"+"/"+"4.56"
	socket.send(m);
}