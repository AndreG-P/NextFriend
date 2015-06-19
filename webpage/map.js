  
/**
 * Moves the map to display over Berlin
 *
 * @param  {H.Map} map      A HERE Map instance within the application
 */
function moveMapToBerlin(map ){
  map.setCenter({lat:52.5159, lng:13.3777});
  map.setZoom(14);
}

/* Moving the map to special point geting from gps signal */
function moveMapToPoint(map, lat, lng, zoom ){
  map.setCenter({lat:+lat, lng:+lng});
  map.setZoom(zoom);
}


function positionError(){
	alert("Error by geting position");
}

function foundUserLocation(location){		
	alert("location: "+ location.coords.lng);	// is undefinde
}


function determineLocation(){
	//var foundUserLocation, positionError;
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(foundUserLocation, positionError);
		
	}else{
		alert("Error in determinelocation");
	}
}

function addMarkersToMap(map, lat, lng) {
	  var newMarker = new H.map.Marker({lat:+lat, lng:+lng});
	  map.addObject(newMarker);  
}

/**
 * Boilerplate map initialization code starts below:
 */
function init(){
	//Step 1: initialize communication with the platform
	var platform = new H.service.Platform({
	  app_id: 'eAj5kHCKYcWnfIcHfPJf',
	  app_code: 'belhuu93pAdVRzaRV_nI0A',
	  useCIT: true,
	  useHTTPS: true
	});
	var defaultLayers = platform.createDefaultLayers();

	//Step 2: initialize a map  - not specificing a location will give a whole world view.
	var map = new H.Map(document.getElementById('map'),
	  defaultLayers.normal.map);

	//Step 3: make the map interactive
	// MapEvents enables the event system
	// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
	var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

	// Create the default UI components
	var ui = H.ui.UI.createDefault(map, defaultLayers);


	// Now use the map as required...
	//moveMapToBerlin(map);
	determineLocation();
	moveMapToPoint(map, 52.53, 13.39, 14 ); // todo geting user location
	addMarkersToMap(map, 52.53, 13.39);
}