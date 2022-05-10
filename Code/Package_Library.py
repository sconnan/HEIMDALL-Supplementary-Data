###############################################################################
############################# Required Packages ###############################
###############################################################################

# Packages required to generate images in files Figure_1.py to Figure_12.py.


import numpy as np
import scipy.io
from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import pandas as pd
from datetime import datetime
from matplotlib.colors import ListedColormap
import cmocean
import cmasher as cmr
import calendar
import cartopy.crs as ccrs
import cartopy
from cmocean import cm as cmo
import matplotlib.image as image
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error