###############################################################################
################################   FIGURE 12  #################################
###############################################################################

#  Comparison of RGB and PAR to depth - Transect 1 Zephyr.


#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'

# Load in gridded RGB values
filename = r'\ZEPHYR_RGB_Model_Bands_Transect_1_Barnes_Output.mat'
RGB_Data = scipy.io.loadmat(path_to_data+filename)

# Load Gridded PAR
Model_PAR = scipy.io.loadmat(path_to_data + '\\Gridded_PAR_Model_Glider.mat')
Model_Light = np.log10(Model_PAR['PAR_Grid_Model'])

# Convert Spectral Ed to PAR units using central wavelengths, 455,555,655nm etc.
# energy values. Then to umol photons. 

R_Band = (RGB_Data['Gridded_R_Band']/4.37e-19)/6.022e17
G_Band = (RGB_Data['Gridded_G_Band']/3.58e-19)/6.022e17
B_Band = (RGB_Data['Gridded_B_Band']/3.03e-19)/6.022e17


R_Band = np.log10(RGB_Data['Gridded_R_Band'])
G_Band = np.log10(RGB_Data['Gridded_G_Band'])
B_Band = np.log10(RGB_Data['Gridded_B_Band'])

# Below is creating custom colourmaps to represent RGB bands.
# make 100 linearly spaced RGB values for each band
r_band_list = [(0+((1/256)*i)**2,0,0) for i in range(256)]
g_band_list = [(0,0+((1/256)*i)**2,0) for i in range(256)]
b_band_list = [(0,0,0+((1/256)*i)**2) for i in range(256)]

# make the custom RGB color maps:
cmp_R = ListedColormap(r_band_list)

cmp_G = ListedColormap(g_band_list) 

cmp_B = ListedColormap(b_band_list) 

cmp_PAR =  'YlGnBu_r'

# Plot results
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)

fig, axs = plt.subplots(4, 1,figsize=(20,10))
fig.text(0.07, 0.5, 'Depth [m]', va='center', rotation='vertical',size=20, weight='bold')
fig.text(0.965, 0.5, '[$\mu$mol m$^{-2}$s$^{-1}$]', va='center', rotation='vertical',size=20, weight='bold')
fig.text(0.45, 0.05, 'Latitude [°N]', va='center', rotation='horizontal',size=20, weight='bold')

interp_method = 'bilinear'

im0 = axs[0].imshow(R_Band, interpolation=interp_method, cmap=cmp_R, vmax=2, vmin=-10) 

axs[0].imshow(R_Band, interpolation=interp_method, cmap=cmp_R, vmax=2, vmin=-10) 
axs[0].set_aspect("auto")
axs[0].set_yticks([-0.5,50])
axs[0].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[0].set_xticks([11,33,55, 77,99])
axs[0].set_xticklabels(['','','','',''])
axs[0].set_facecolor('dimgrey')
axs[0].text(1.02, 0.5, 'R BAND', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.6966, 0.04, 0.1825])
cbar = fig.colorbar(im0, cax=cbar_ax,orientation="vertical" )
cbar = fig.colorbar(im0, cax=cbar_ax, ticks=[-9,-4 ,1] )
cbar.ax.set_yticklabels(['10$^{-9}$','10$^{-4}$','10$^{1}$'],size=20) 

axs[0].annotate('', xy=(0.93, 1.1), xycoords='axes fraction', xytext=(0.07, 1.1), 
            arrowprops=dict(width=0.7, color='k',linewidth=3))
axs[0].text(0.02, 1.19, '27th APR\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.98, 1.19, '12th MAY\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.025, 0.1, 'a',  rotation='horizontal'
              , transform=axs[0].transAxes, size=24, weight='bold',color='white')

im1 = axs[1].imshow(G_Band, interpolation=interp_method, cmap=cmp_G, vmax=2, vmin=-10) 

axs[1].imshow(G_Band, interpolation=interp_method, cmap=cmp_G, vmax=2, vmin=-10) 
axs[1].set_aspect("auto")
axs[1].set_yticks([-0.5,50])
axs[1].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[1].set_xticks([11,33,55, 77,99])
axs[1].set_xticklabels(['','','','',''])
axs[1].text(1.02, 0.5, 'G BAND', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1].transAxes, size=20, weight='bold')
cbar_ax = fig.add_axes([0.88, 0.5011, 0.04, 0.1825])
cbar = fig.colorbar(im1, cax=cbar_ax, ticks=[-9,-4,1] )
cbar.ax.set_yticklabels(['10$^{-9}$','10$^{-4}$','10$^{1}$']) 
axs[1].text(0.025, 0.1, 'b',  rotation='horizontal'
              , transform=axs[1].transAxes, size=24, weight='bold',color='white')

im2 = axs[2].imshow(B_Band, interpolation=interp_method, cmap=cmp_B, vmax=2, vmin=-10) 

axs[2].imshow(B_Band, interpolation=interp_method, cmap=cmp_B, vmax=2, vmin=-10) 
axs[2].set_aspect("auto")
axs[2].set_yticks([-0.5,50])
axs[2].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[2].set_xticks([11,33,55, 77,99])
axs[2].set_xticklabels(['','','','',''])

axs[2].text(1.02, 0.5, 'B BAND', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[2].transAxes, size=20, weight='bold')
cbar_ax = fig.add_axes([0.88, 0.3056, 0.04, 0.1825])
cbar = fig.colorbar(im2, cax=cbar_ax, ticks=[-9,-4,1 ] )
cbar.ax.set_yticklabels(['10$^{-9}$','10$^{-4}$','10$^{1}$'],size=20) 
axs[2].text(0.025, 0.1, 'c',  rotation='horizontal'
              , transform=axs[2].transAxes, size=24, weight='bold',color='white')

im3 = axs[3].imshow(Model_Light, interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9) 

axs[3].imshow(Model_Light, interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9) 
axs[3].set_aspect("auto")
axs[3].set_yticks([-0.5,50])
axs[3].set_yticklabels(['0' ,'100' ],rotation=0,size=20)
axs[3].set_xticks([11,33,55, 77,99])
axs[3].set_xticklabels(['','','','',''])
axs[3].set_facecolor('dimgrey')
axs[3].set_xticks([11,33,55, 77,99])
axs[3].set_xticklabels(['74.95','75.35','75.75', '76.15',
                        '76.55'],rotation=0,size=20)
axs[3].text(1.02, 0.5, 'E$_{D}$ $_{PAR}$', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[3].transAxes, size=20, weight='bold')
cbar_ax = fig.add_axes([0.88, 0.1095, 0.04, 0.1825])
cbar = fig.colorbar(im3, cax=cbar_ax, ticks=[-8, -3, 2] )
cbar.ax.set_yticklabels(['10$^{-8}$','10$^{-3}$','10$^{2}$'],size=20) 
axs[3].text(0.025, 0.1, 'd',  rotation='horizontal'
              , transform=axs[3].transAxes, size=24, weight='bold',color='white')

plt.subplots_adjust(wspace=0.02, hspace=0.07)