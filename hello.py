from flask import Flask
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Hello Github'

map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
              resolution='l', area_thresh=1000.0)
 
map.drawcoastlines()
 
plt.show()