###############################################################################
################################   FIGURE 11  #################################
###############################################################################

# Winter underwater gridded glider details and modelled PAR from Drake glider.

# Original data managed by Porter M.; Cottier F.R.; Dumont E.; Venables E.(2020b).
# Arctic PRIZE mission two near-real time glider dataset in the Barents Sea Winter 2018.
# British Oceanographic Data Centre, National Oceanography Centre, NERC, UK. doi:10/dmgm

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'
filename_bio_data = r'\Drake_Transect_3_Gridded_Bio_Optical_Data.mat'

# Load modelled gridded PAR data
filename = r'\DRAKE_Transect_3_Barnes_OUTPUT.mat'
Drake = scipy.io.loadmat(path_to_data + filename)
Bio_Data = scipy.io.loadmat(path_to_data + filename_bio_data)

Light = Drake['ZO']
Temp = Bio_Data['temp']
Sal = Bio_Data['sal']

# Plot results
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)


fig, axs = plt.subplots(3, 1,figsize=(16,8))
fig.text(0.07, 0.5, 'Depth [m]', va='center', rotation='vertical',size=20, weight='bold')
fig.text(0.45, 0.05, 'Latitude [°N]', va='center', rotation='horizontal',size=20, weight='bold')

interp_method = 'bilinear'

cmp =  cmo.thermal
im0 = axs[0].imshow(Temp, interpolation=interp_method, cmap=cmp, vmax=3, vmin=0.5)
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.892, 0.635, 0.04, 0.245])
cbar = fig.colorbar(im0, cax=cbar_ax, ticks=[ 1, 2,3] )
cbar = fig.colorbar(im0, cax=cbar_ax, ticks=[3,2,1,0]) #, ticks=[-8,-3,2]
axs[0].imshow(Temp, interpolation=interp_method, cmap=cmp, vmax=3, vmin=0.51)
axs[0].set_aspect("auto")
axs[0].set_yticks([-0.5 ,50])
axs[0].set_yticklabels(['0' ,'100'],rotation=0,size=20)
axs[0].set_xticks([0,15,31,47,62])
axs[0].set_xticklabels(['','','','',''])
axs[0].set_facecolor('dimgrey')
axs[0].annotate('', xy=(0.07, 1.1), xycoords='axes fraction', xytext=(0.93, 1.1), 
            arrowprops=dict(width=0.7, color='k',linewidth=3))
axs[0].text(0.02, 1.15, '13th FEB\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.98, 1.15, '7th FEB\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(1.182, 0.5, 'Temp [°C]', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.025, 0.8, 'a',  rotation='horizontal'
              , transform=axs[0].transAxes, size=24, weight='bold')


cmp =  cmo.haline
im1 = axs[1].imshow(Sal, interpolation=interp_method, cmap=cmp, vmax=35, vmin = 34.5)
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.892, 0.37, 0.04, 0.245])
cbar = fig.colorbar(im1, cax=cbar_ax,ticks=[35, 34.8, 34.6] ) #, ticks=[-8,-3,2]
axs[1].imshow(Sal, interpolation=interp_method, cmap=cmp, vmax=35, vmin=34.5)
axs[1].set_aspect("auto")
axs[1].set_yticks([-0.5 ,50])
axs[1].set_yticklabels(['0' ,'100'],rotation=0,size=20)
axs[1].set_xticks([0,15,31,47,63])
axs[1].set_xticklabels(['','','','',''])
axs[1].text(1.182, 0.5, 'Sal [psu]', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1].transAxes, size=20, weight='bold')
axs[1].text(0.025, 0.8, 'b',  rotation='horizontal'
              , transform=axs[1].transAxes, size=24, weight='bold')



cmp_PAR =  'YlGnBu_r'
im2 = axs[2].imshow(np.log10(Light), interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9)
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.892, 0.105, 0.04, 0.245])
cbar = fig.colorbar(im2, cax=cbar_ax ) #, ticks=[-8,-3,2]
axs[2].imshow(np.log10(Light), interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9)
axs[2].set_aspect("auto")
axs[2].set_yticks([-0.5 ,50])
axs[2].set_yticklabels(['0' ,'100'],rotation=0,size=20)
axs[2].set_xticks([0,15,31,47,63])
axs[2].set_xticklabels(['75.48','75.75','76.04','76.33', '76.61'],rotation=0,size=20)
axs[2].text(1.182, 0.5, 'E$_{D}$ $_{PAR}$ [$\mu$mol m$^{-2}$s$^{-1}$]', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[2].transAxes, size=18, weight='bold')
cbar = fig.colorbar(im2, cax=cbar_ax, ticks=[-8, -3, 2] )
cbar.ax.set_yticklabels(['10$^{-8}$','10$^{-3}$','10$^{2}$']) 
axs[2].text(0.025, 0.8, 'c',  rotation='horizontal'
              , transform=axs[2].transAxes, size=24, weight='bold')


        
# Calculate zeniths using datetime info from glider. 
# Requires solar zenith calculator from Reda, I., & Andreas, A. (2004). 

import sys
# Define path where solar zenith calculator is saved
path_2_module = r'C:\Users\...'
sys.path.append(path_2_module)

from Solar_Zenith_Calculator import zenith_calculator

# Load latitude and timestamp info from glider. Note we are assuming longitude of 30°E as constant.
datetime_file = r'\Drake_grid_lats_time.mat'
Drake_loc_time = scipy.io.loadmat(path + datetime_file)

Drake_Lat = Drake_loc_time['lats']
Drake_Time= Drake_loc_time['unix_time']

drake_zeniths = [zenith_calculator(Drake_Lat[0,i],30,str(int(Drake_Time[0,i]))) for i in range(64)]
drake_elev = [(90-x) for x in drake_zeniths]

ax3 = axs[2].twinx()
ax3.plot(drake_elev,linestyle='None',marker='o',color='darkred',ms=8)
ax3.plot(np.zeros(len(drake_zeniths)),linestyle='dashed',color='darkred')
ax3.set_yticks([0,-28])
ax3.tick_params(axis='y', colors='darkred')
ax3.set_yticklabels(['0','-28'],rotation=0,size=18,weight='bold')
axs[2].text(1.025, 0.5, 'Solar\nElevation', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[2].transAxes, size=20, weight='bold',color='darkred')

plt.subplots_adjust(wspace=0.02, hspace=0.07)