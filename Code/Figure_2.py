##############################################################################
################################   FIGURE 2  #################################
##############################################################################

#  Map of location of ArcLight observatory and glider transect path.


fig = plt.figure()
ax = plt.axes(projection=cartopy.crs.Mercator(central_longitude=0.0, min_latitude=-80.0, max_latitude=84.0
                                              , globe=None, latitude_true_scale=0.0))

ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE,linewidth=0.3)
ax.add_feature(cartopy.feature.BORDERS, linestyle=':',linewidth=0.3)
ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([0, 50, 69, 81])
plt.plot(1318251.59,14893162.75,marker='o',ms=15, markeredgecolor='black', markerfacecolor='firebrick')

# Glider Transect Point, in EPSG:3857 grid points
lats = np.linspace(12825582.50,13716975.14,1000)
lons = np.ones(len(lats))*3339584.72
plt.plot(lons,lats,linestyle='None',marker='o',color='midnightblue')
plt.annotate('', xy=(lons[0]+150000, lats[0]+200000),  xytext=(lons[0]+150000, lats[-1]-200000), 
            arrowprops=dict(arrowstyle="<|-",mutation_scale=25,
                                  connectionstyle="arc3,rad=-0", fc="k",linewidth=1.75,color='k'))
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle=':')
gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = True
gl.xlabel_style = {'color': 'black', 'weight': 'bold','size':18}
gl.ylabel_style = {'color': 'black', 'weight': 'bold','size':18}
plt.text(80000,14893162.75, 'ArcLight \nObservatory',size=17)
plt.text(lons[0]+250000,((lats[0]+200000 + lats[-1]-200000)/2)-115000, 'Glider',size=18)
ax.spines["bottom"].set_linewidth(5)