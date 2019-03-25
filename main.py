# this script generates the HTML file that contains the google map with the heatmap

import pandas as pd
import numpy as np


# Read data 
df = pd.read_csv('./accident.csv')

# Creating an HTML Header file
headV="""
<!DOCTYPE html>
<html>
  <head>
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Crashes Heatmap</title>
    <style>
      html, body {
      height: 100%;
      salam
      khodafez
      margin: 0;
      padding: 0;
      }
      #map {
      height: 100%;
      }
    </style>
  </head>
  <body> <!--  DataCanary_s fix -->
      <div id="map" class="main-container"></div>
    <script>
    var map, heatmap;
      function initMap() {
      map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: {lat: 33.915013, lng: -117.80},
      mapTypeId: google.maps.MapTypeId.HYBRID
      });

      heatmap = new google.maps.visualization.HeatmapLayer({
          data: getPoints(),
          map: map
        });

      heatmap.set('radius',  25);
      heatmap.set('opacity', 0.5);
      }

      function getPoints(){
        var points = []
        for (var i = 0; i < crashes.length; i++) {
          var crash = crashes[i]
          points.push(new google.maps.LatLng(crash[0], crash[1]))
      }
      return points;
    }
"""

tailV="""
      </script>

        <script async defer
            src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCR2Qp3o5fgCFd4WtF68x4j7yeSJ8oUhlY&libraries=visualization&callback=initMap"></script>

  </body>
</html> 
""" 

s=' var crashes = [\n'



# Removing crashes with missing lat/lon
df.fillna(0, inplace=True)
df=df[(df.LONGITUD != 0 ) | (df.LATITUDE != 0 )]

# extract data points related to Los Angeles and Orange County area
df =df[(df.LATITUDE>=33.4003) & (df.LATITUDE<=34.3274) & (df.LONGITUD>-118.6482) & (df.LONGITUD<-116.9138)]

lat=df.LATITUDE.tolist()
lng=df.LONGITUD.tolist()


for i in range(len(lat)):
    s+="[ %s, %s],\n" % (lat[i],lng[i])


s+='];'

# Write out 
f=open('output.html','w')
f.write(headV)
f.write(s)
f.write(tailV)
f.close()
