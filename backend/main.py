__author__ = 'ansgar'
import urllib.request
import xml.etree.ElementTree as ET
import unicodedata


friends = {"a": "52.4,13.6", "b": "52.5,13.5", "c": "52.4,13.4"}

bar_file = open("/home/ansgar/Schreibtisch/berlin_bars", "r")
bars = [(line.split(";")[0].strip(), line.split(";")[1].strip().replace(",", "").replace(" ", "+")) for line in bar_file.readlines()]
bar_c = open("/home/ansgar/Schreibtisch/bars_coord", "r")
b = [x.replace(" ", "").strip() for x in bar_c.readlines()]
coll = zip(bars, b)
dest_list = ["&destination"+str(i)+"="+x for i, x in enumerate(b) ]
print(dest_list)
#print({ b: x for a, b in list(coll) for x in a })
dest_string = "&destination0=52.5004082,13.4226398&destination1=52.5220108,13.4085703&destination2=52.5169296,13.4433498&destination3=52.5376282,13.4087&destination4=52.4644699,13.3236799&destination5=52.5114288,13.4569197&destination6=52.4913216,13.4347897&destination7=52.4581108,13.3292303&destination8=52.5063515,13.3228703&destination9=52.4467697,13.6265898&destination10=52.5305901,13.4019499&destination11=52.5342293,13.4174995&destination12=52.5057106,13.3236103&destination13=52.5638695,13.3284502&destination14=52.5016594,13.3104401&destination15=52.5011,13.2977499&destination16=52.5372696,13.4174004&destination17=52.5236816,13.4022799&destination18=52.4933891,13.29949&destination19=52.5134201,13.3913298&destination20=52.5175781,13.4641304&destination21=52.5255013,13.3875103&destination22=52.4930687,13.41465&destination23=52.5520515,13.4194698&destination24=52.5112801,13.3355904&destination25=47.9912605,11.3643999&destination26=52.4772186,13.3203001&destination27=52.5157814,13.3915195&destination28=52.5475311,13.4113798&destination29=52.4610596,13.3181496&destination30=52.6150513,13.4851599&destination31=52.506691,13.4682703&destination32=52.4884186,13.3506498&destination33=52.5175781,13.4641304&destination34=52.5311012,13.4001102"

#    data = xmltodict.parse(data)
#    return render_to_response('my_template.html', {'data': data})
"""
bar_coord = []
for i in range(len(bars)):
    search = str(unicodedata.normalize("NFKD", bars[i][1]).encode("ascii", "ignore"))
    geocodeUrl = "http://geocoder.cit.api.here.com/6.2/geocode.xml?app_id=HaEP7b8nG5SDZGZvbDyY&app_code=JOYjBF5ccoacXdOIyhwYkA&gen=8&searchtext={}".format(search)

    print(geocodeUrl)
    #print(geocodeUrl)

    root = ET.fromstring(urllib.request.urlopen(geocodeUrl).read())


    for key in root.iter():
        if key.tag == "NavigationPosition":
            print((child.text for child in list(key)))
            bar_coord.append((child.text for child in list(key)))
            break

bar_file = open("/home/ansgar/Schreibtisch/bars_coord", "w")
bar_file.writelines("\n".join((", ".join(x) for x in bar_coord)))
bar_file.close()
"""

print()
dist = [{} for f in friends]
for i, f in enumerate(friends.values()):
    url ="""http://legacy.matrix.route.cit.api.here.com/routing/6.2/calculatematrix.xml?app_id=HaEP7b8nG5SDZGZvbDyY&app_code=JOYjBF5ccoacXdOIyhwYkA&matrixattributes=none,su&summaryattributes=cf,di&mode=fastest;publicTransport&start0={}{}&searchRange=10000""".format(f, dest_string)
    print(url)
    root = ET.fromstring(urllib.request.urlopen(url).read())
    print(root)
    for key in root.iter():
        if key.tag == "MatrixEntry":
            ind = 0
            currentDist = 0
            for child in key.iter():
                if child.tag == "DestinationIndex":
                    ind = int(child.text)
                    continue
                if child.tag == "Distance":
                    currentDist = child.text

            print(ind, currentDist)
            #print([child.tag for child in list(key)])
            dist[i][ind] = float(currentDist)

shortest = (float("inf"), 0)
for x in dist[0].keys():
    length = max([dist[i][x] for i in range(2)])
    if length < shortest[0]:
        shortest = (length, x)


print(dist)
print(shortest)


