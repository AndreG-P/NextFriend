# http://www.defuze.org/oss/ws4py/docs/servertutorial.html#cherrypy
import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import EchoWebSocket
from ws4py.websocket import WebSocket

import time

cherrypy.config.update({'server.socket_port': 80,'server.socket_host': 'ec2-52-28-160-147.eu-central-1.compute.amazonaws.com'})
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()


""" 
basic procedure
1) open server
2) accept clients - read name + latlong
if first client enters:
   start timer

3) if timer went on for 1 minute:
   send dict of all clients to magic_code
   retrieve final destination 

4) send over network to all clients
"""

clients_coords = {}
admin_name = ""

def parse_message(message):
    message = message.data;
    name = message.split("#")[0]
    latlong = message.split("#")[1]
    lat_ = latlong.split('/')[0]
    long_ = latlong.split('/')[1]
    latlong_ = lat_+','+long_
    return [name,lat_,long_]


class GPSSocketHandler(WebSocket):
    def received_message(self, m):
        global admin_name
        name,lat,long=parse_message(m)
        # first user gets admin
        if not admin_name: 
            admin_name = name       
            #print admin_name,'is now admin!'
        else:
            # if admin sends message again, end round
            if name==admin_name:
                # get response from ansgar
                response_message = 'Trinkhalle des heiligen Juhnkes#52.3/45.2'
                #print admin_name,'ended round'
                admin_name = ""
                clients_coords.clear()
                cherrypy.engine.publish('websocket-broadcast', response_message)
            else:   
                clients_coords[name]=lat+','+long
                #print 'updated client',name,'@pos',lat,',',long
                       
class Root(object):
    @cherrypy.expose
    def index(self):
        return 'some HTML with a websocket javascript connection'

    @cherrypy.expose
    def ws(self):
        # you can access the class instance through
        handler = cherrypy.request.ws_handler
      	cherrypy.log("Handler created: %s" % repr(cherrypy.request.ws_handler))

    @cherrypy.expose
    def received_message(self, m):
        recvStr = m.data.decode("utf-8")
        #print 'client sent:',recvStr

cherrypy.quickstart(Root(), '/', config={'/ws': {'tools.websocket.on': True,
                                                 'tools.websocket.handler_cls': GPSSocketHandler}})
