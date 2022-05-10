##############################################################################
################################   FIGURE 10  ################################
##############################################################################

#  Comparison of Open Water Glider PAR and Modelled PAR

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'
Model_Glider_Data = scipy.io.loadmat(path_to_data + '\Gridded_PAR_Model_Glider.mat')

# Load in data
Model_Light = Model_Glider_Data['PAR_Grid_Model'][:,:]
Glider_Light = Model_Glider_Data['PAR_Grid_Glider'][:,:]

# Define equally spaced lats and depths used in gridding process
lats = Model_Glider_Data['xgrid']
depths= Model_Glider_Data['ygrid']

# Plot results
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)


fig, axs = plt.subplots(2, 1,figsize=(16,8))
fig.text(0.07, 0.5, 'Depth [m]', va='center', rotation='vertical',size=20, weight='bold')
fig.text(0.45, 0.05, 'Latitude [°N]', va='center', rotation='horizontal',size=20, weight='bold')

interp_method = 'bilinear'
# For quality control, set illogical values as negative. (e.g. last two columns show increasing light as depth increases)
Glider_Light[30:,84:]=-1
# Mask data below 1e-2
Glider_Light = np.ma.masked_where((1e-2> Glider_Light), Glider_Light)
# Colourmap scheme
cmp_PAR =  'YlGnBu_r'

axs[0].imshow(np.log10(Glider_Light), interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9)
axs[0].set_aspect("auto")
axs[0].set_yticks([-0.5 ,50])
axs[0].set_yticklabels(['0' ,'100'],rotation=0,size=20)
axs[0].set_xticks([11,33,55, 77,99])
axs[0].set_xticklabels(['','','','',''])
axs[0].set_facecolor('dimgrey')
axs[0].text(1.02, 0.5, 'GLIDER', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].annotate('', xy=(0.93, 1.1), xycoords='axes fraction', xytext=(0.07, 1.1), 
            arrowprops=dict(width=0.7, color='k',linewidth=3))
axs[0].text(0.02, 1.15, '27th APR\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.98, 1.15, '12th MAY\n2018', horizontalalignment='center', rotation='horizontal'
              , verticalalignment='center', transform=axs[0].transAxes, size=20, weight='bold')
axs[0].text(0.025, 0.85, 'a',  rotation='horizontal'
              , transform=axs[0].transAxes, size=24, weight='bold')

im1 = axs[1].imshow(np.log10(Model_Light), interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9)
axs[1].imshow(np.log10(Model_Light), interpolation=interp_method, cmap=cmp_PAR, vmax=3, vmin=-9)
axs[1].set_aspect("auto")

axs[1].set_yticks([-0.5 ,50])
axs[1].set_yticklabels(['0' ,'100'],rotation=0,size=20)
axs[1].set_xticks([11,33,55, 77,99])
axs[1].set_xticklabels(['74.95','75.35','75.75', '76.15',
                        '76.55'],rotation=0,size=20)
axs[1].set_facecolor('dimgrey')
axs[1].text(1.02, 0.5, 'HEIMDALL', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1].transAxes, size=20, weight='bold')
axs[1].text(0.025, 0.85, 'b',  rotation='horizontal'
              , transform=axs[1].transAxes, size=24, weight='bold')
              
# add space for colour bar
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.04, 0.7])
cbar = fig.colorbar(im1, cax=cbar_ax, ticks=[-8,-3,2] )
cbar.ax.set_yticklabels(['10$^{-8}$','10$^{-3}$','10$^{2}$'],size=20) 
cbar.set_label(label='E$_{D}$ $_{PAR}$ [$\mu$mol m$^{-2}$s$^{-1}$]',weight='bold',size=20)

plt.subplots_adjust(wspace=0.02, hspace=0.07)
