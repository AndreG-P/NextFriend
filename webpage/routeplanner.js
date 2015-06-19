
/**
 * Calculates and displays a walking route from the St Paul's Cathedral in London
 * to the Tate Modern on the south bank of the River Thames
 *
 * A full list of available request parameters can be found in the Routing API documentation.
 * see:  http://developer.here.com/rest-apis/documentation/routing/topics/resource-calculate-route.html
 *
 * @param   {H.service.Platform} platform    A stub class to access HERE services
 */

function calculateRouteFromAtoB (platform, pointA, pointB_lat, pointB_lng) {
  var router = platform.getRoutingService(),
    routeRequestParams = {
      mode: 'shortest;pedestrian',
      representation: 'display',
      waypoint0: pointA.latitude+','+pointA.longitude, // St Paul's Cathedral
      waypoint1: pointB_lat+','+pointB_lng,  // Tate Modern
      routeattributes: 'waypoints,summary,shape,legs',
      maneuverattributes: 'direction,action'
    };

	router.calculateRoute(
    routeRequestParams,
    onSuccess,
    onError
  );
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

  addWaypointsToPanel(route.waypoint);
  addManueversToPanel(route);
  addSummaryToPanel(route.summary);
  // ... etc.
}

/**
 * This function will be called if a communication error occurs during the JSON-P request
 * @param  {Object} error  The error message received.
 */
function onError(error) {
  alert('Error on get a route!');
}