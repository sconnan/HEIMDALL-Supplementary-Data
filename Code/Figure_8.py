###############################################################################
################################   FIGURE 8  ##################################
###############################################################################
#  Plot of gridded bio-optical data for model - Transect 1 Zephyr.

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'
filename= r'\Gridded_Bio_Optical_Data.mat'
filename_temp = r'\Gridded_Bio_Optical_Temp.mat'

Grid_Data = scipy.io.loadmat(path_to_data+filename)
Temp_Data = scipy.io.loadmat(path_to_data+filename_temp)


Chl = Grid_Data['bkst_chl']
Sal = Grid_Data['sal']
Bkst = Grid_Data['bkst']
Temp = Temp_Data['Temp']


# Note that loaded chlorophyll has been corrected for photoinhibition using the method of Kostakis et al., (2020). 
# Development of a bio-optical model for the Barents Sea to quantitatively link glider and satellite observations. 
# Philosophical Transactions Of The Royal Society A: Mathematical, Physical And Engineering Sciences, 378(2181), 20190367. doi: 10.1098/rsta.2019.0367.
# See manual for more details. WET Labs Inc. 2013 Scattering meter, ECO BB-9, User’s Guide, Revision L. p. 9–10.


matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)

fig, axs = plt.subplots(3, 1,figsize=(20,10))
fig.text(0.07, 0.5, 'Depth [m]', va='center', rotation='vertical',size=20, weight='bold')
fig.text(0.45, 0.05, 'Latitude [°N]', va='center', rotation='horizontal',size=20, weight='bold')
interp_method = 'bilinear'

im0 = axs[0].imshow(Temp, interpolation=interp_method, cmap=cmo.thermal, vmax=3, vmin=-.95) 
axs[0].imshow(Temp, interpolation=interp_method, cmap=cmo.thermal, vmax=3, vmin=-.95) 
axs[0].set_aspect("auto")
axs[0].set_yticks([-0.5,50])
axs[0].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[0].set_xticks([11,33,55, 77,99])
axs[0].set_xticklabels(['','','','',''])
cbar_ax = fig.add_axes([0.88, 0.635, 0.04, 0.245])
cbar = fig.colorbar(im0, cax=cbar_ax,orientation="vertical" )
cbar = fig.colorbar(im0, cax=cbar_ax, ticks=[0, 1, 2,3] )
axs[0].text(1.17, 0.5, 'Temp [°C]', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.025, 0.85, 'a',  rotation='horizontal'
              , transform=axs[0].transAxes, size=24, weight='bold')

axs[0].annotate('', xy=(0.93, 1.1), xycoords='axes fraction', xytext=(0.07, 1.1), 
            arrowprops=dict(width=0.7, color='k',linewidth=3))
axs[0].text(0.02, 1.18, '27th APR\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.98, 1.18, '12th MAY\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')

im1 = axs[1].imshow(Sal, interpolation=interp_method, cmap=cmo.haline, vmax=35, vmin=34) 
axs[1].imshow(Sal, interpolation=interp_method, cmap=cmo.haline, vmax=35, vmin=34) 
axs[1].set_aspect("auto")
axs[1].set_yticks([-0.5,50])
axs[1].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[1].set_xticks([11,33,55, 77,99])
axs[1].set_xticklabels(['','','','',''])
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.37, 0.04, 0.245])
cbar = fig.colorbar(im1, cax=cbar_ax,orientation="vertical" )
cbar = fig.colorbar(im1, cax=cbar_ax, ticks=[34.2, 34.6,35] )
axs[1].text(1.17, 0.5, 'Sal [psu]', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1].transAxes, size=20, weight='bold')
axs[1].text(0.025, 0.85, 'b',  rotation='horizontal'
              , transform=axs[1].transAxes, size=24, weight='bold')

im2 = axs[2].imshow(Chl, interpolation=interp_method, cmap=cmo.algae, vmax=16, vmin=0) 
axs[2].imshow(Chl, interpolation=interp_method, cmap=cmo.algae, vmax=16, vmin=0) 
axs[2].set_aspect("auto")
axs[2].set_yticks([-0.5,50])
axs[2].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[2].set_xticks([11,33,55, 77,99])
axs[2].set_xticklabels(['','','','',''])
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.105, 0.04, 0.245])
cbar = fig.colorbar(im2, cax=cbar_ax,orientation="vertical" )
cbar = fig.colorbar(im2, cax=cbar_ax, ticks=[4,8, 12,16] )
axs[2].set_xticks([11,33,55, 77,99])
axs[2].set_xticklabels(['74.95','75.35','75.75', '76.15',
                        '76.55'],rotation=0,size=20)
axs[2].text(1.17, 0.5, 'Chl a [mgm$^{-3}$]', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[2].transAxes, size=20, weight='bold')
axs[2].text(0.025, 0.85, 'c',  rotation='horizontal'
              , transform=axs[2].transAxes, size=24, weight='bold')
plt.subplots_adjust(wspace=0.02, hspace=0.07)