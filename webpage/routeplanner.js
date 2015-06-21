

var publicTransport = false;
//var  = 52.55;
//var  = 13.5;

function get_Pedestrian_Route(Point_lat,Point_lng){
		if(Point_lat && Point_lng){
			addMarkersToMap(map, Point_lat, Point_lng);
			if(userlocation){
				addMarkersToMap(map, userlocation.latitude, userlocation.longitude);			
				if(publicTransport)calculateRouteFromAtoB (platform, userlocation, Point_lat, Point_lng, 'fastest;publicTransport');
				else calculateRouteFromAtoB (platform, userlocation, Point_lat, Point_lng, 'shortest;pedestrian');
			}
			else alert("No Userlocation found");									
		}else alert("No destinationlocation found");									
}													

 /**
 * This function will be called once the Routing REST API provides a response
 * @param  {Object} result          A JSONP object representing the calculated route
 *
 * see: http://developer.here.com/rest-apis/documentation/routing/topics/resource-type-calculate-route.html
 */
function onSuccess(result) {
  var route = result.response.route[0];
 /*
  * The styling of the route response on the map is entirely under the developer's control.
  * A representitive styling can be found the full JS + HTML code of this example
  * in the functions below:
  */
  addRouteShapeToMap(route);
  addManueversToMap(route);

 // addWaypointsToPanel(route.waypoint);
 // addManueversToPanel(route);
 // addSummaryToPanel(route.summary);

 alert( 'Distance: ' + route.summary.distance  + ' Travel Time: ' + route.summary.travelTime.toMMSS());
  // ... etc.
}

/**
 * This function will be called if a communication error occurs during the JSON-P request
 * @param  {Object} error  The error message received.
 */
function onError(error) {
  alert('Error on get a route!');
}

/**
 * Calculates and displays a walking route from the St Paul's Cathedral in London
 * to the Tate Modern on the south bank of the River Thames
 *
 * A full list of available request parameters can be found in the Routing API documentation.
 * see:  http://developer.here.com/rest-apis/documentation/routing/topics/resource-calculate-route.html
 *
 * @param   {H.service.Platform} platform    A stub class to access HERE services
 */

function calculateRouteFromAtoB (platform, pointA, pointB_lat, pointB_lng, mode) {
  var router = platform.getRoutingService(),
    routeRequestParams = {
      mode: mode, 
      representation: 'display',
      waypoint0: pointA.latitude+','+pointA.longitude, 
      waypoint1: pointB_lat+','+pointB_lng,  
      routeattributes: 'waypoints,summary,shape,legs',
      maneuverattributes: 'direction,action'
    };
	
	router.calculateRoute(
    routeRequestParams,
    onSuccess,
    onError
  );
}
 



