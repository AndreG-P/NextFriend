__author__ = 'ansgar'
import urllib2
import xmltodict

bar_file = open("/home/ansgar/Schreibtisch/berlin_bars", "r")
bars = [(line.split(";")[0].strip(), line.split(";")[1].strip().replace(",", "").replace(" ", "+")) for line in bar_file.readlines()]
print(bars)


#    data = xmltodict.parse(data)
#    return render_to_response('my_template.html', {'data': data})

geocodeUrl = """http://geocoder.cit.api.here.com/6.2/geocode.xml
?app_id=HaEP7b8nG5SDZGZvbDyY
&app_code=JOYjBF5ccoacXdOIyhwYkA
&gen=8
&searchtext={}""".format(bars[0][1])

file = urllib2.urlopen(geocodeUrl)
data = file.read()
file.close()
print(data)


url = """http://legacy.matrix.route.cit.api.here.com/routing/6.2/calculatematrix.xml
?app_id=HaEP7b8nG5SDZGZvbDyY
&app_code=JOYjBF5ccoacXdOIyhwYkA
&matrixattributes=none,su
&summaryattributes=cf,di
&mode=fastest;pedestrian
&start0={}
&destination0=51.3248527,-0.2071309
&destination1=51.3438749,-0.2018845
&destination2=51.3241124,-0.1963806
&searchRange=10000""".format("52.530861,13.38469")


url_stripped = url.strip()

print(url_stripped)