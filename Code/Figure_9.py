##############################################################################
################################   FIGURE 9  #################################
##############################################################################

#  Comparison of Open Water Glider PAR and Modelled PAR - Individual Profiles

#18, 291, 67, 144, Profile numbers from ungridded glider data - chosen by pseudo-random number generator


#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'

# Assign filename to modelled data
filename = r'\Individual_Profiles_Model_Data.mat'
plot_dict = scipy.io.loadmat(path_to_data+filename)

# Plot comparisons
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15)
fig, axs = plt.subplots(4, 1,figsize=(9,16))

custom_xlim = (1e-4, 6e2)
custom_ylim = (-5, 105)

# Setting custom axes.
plt.setp(axs, xlim=custom_xlim, ylim=custom_ylim)

fig.text(0.5, 0.92, 'E$_{D}$ $_{PAR}$ [$\mu$mol m$^{-2}$s$^{-1}$]', ha='center',size=18,weight='bold')
fig.text(0.04, 0.5, 'Depth [m]', va='center', rotation='vertical',size=18,weight='bold')


prof=18
ci1 = plot_dict['ci1_'+str(prof)][0,:]
ci2 = plot_dict['ci2_'+str(prof)][0,:]
axs[0].plot(plot_dict['glider_par_'+str(prof)][0,:],plot_dict['glider_depths_'+str(prof)][0,:], linestyle='None',marker='o',ms=10,markerfacecolor='silver',
             markeredgewidth=1, markeredgecolor='k',label='Glider' )
axs[0].plot(plot_dict['model_par_'+str(prof)][0,:],plot_dict['model_depths_'+str(prof)][0,:] , linestyle='None',marker='^',ms=10,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k',label='HEIMDALL')
axs[0].fill_betweenx(plot_dict['model_depths_'+str(prof)][0,:],(ci2), (ci1), color='b', alpha=.1,label='Cloud Range')
axs[0].plot(np.ones(120)*1e-2, np.arange(-10,110,1),linestyle='dashed',color='k',linewidth=2)
axs[0].set_xscale('log')
axs[0].grid(linestyle=':')
axs[0].invert_yaxis()
axs[0].xaxis.tick_top()
axs[0].set_yticks([0,50,100])
axs[0].text(0.1, 0.8, '74.83°N\n26-04-18\n04:17', horizontalalignment='center'
              , verticalalignment='center', transform=axs[0].transAxes, size=14, weight='bold')
axs[0].text(0.9, 0.1, 'a', rotation='horizontal', transform=axs[0].transAxes,size=20, weight='bold')


prof=291
ci1 = plot_dict['ci1_'+str(prof)][0,:]
ci2 = plot_dict['ci2_'+str(prof)][0,:]
axs[1].plot(plot_dict['glider_par_'+str(prof)][0,:],plot_dict['glider_depths_'+str(prof)][0,:], linestyle='None',marker='o',ms=10,markerfacecolor='silver',
             markeredgewidth=1, markeredgecolor='k', )
axs[1].plot(plot_dict['model_par_'+str(prof)][0,:],plot_dict['model_depths_'+str(prof)][0,:] , linestyle='None',marker='^',ms=10,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[1].fill_betweenx(plot_dict['model_depths_'+str(prof)][0,:],(ci2), (ci1), color='b', alpha=.1,label='Uncertainty')
axs[1].plot(np.ones(120)*1e-2, np.arange(-10,110,1),linestyle='dashed',color='k',linewidth=2)
axs[1].set_xscale('log')
axs[1].grid(linestyle=':')
axs[1].invert_yaxis()
axs[1].xaxis.tick_top()
axs[1].set_xticklabels([])
axs[1].set_yticks([0,50,100])
axs[1].text(0.1, 0.8, '76.16°N\n08-05-18\n00:54', horizontalalignment='center'
              , verticalalignment='center', transform=axs[1].transAxes, size=14, weight='bold')
axs[1].text(0.9, 0.1, 'b', rotation='horizontal', transform=axs[1].transAxes,size=20, weight='bold')

prof=67
ci1 = plot_dict['ci1_'+str(prof)][0,:]
ci2 = plot_dict['ci2_'+str(prof)][0,:]
axs[2].plot(plot_dict['glider_par_'+str(prof)][0,:],plot_dict['glider_depths_'+str(prof)][0,:], linestyle='None',marker='o',ms=10,markerfacecolor='silver',
             markeredgewidth=1, markeredgecolor='k', )
axs[2].plot(plot_dict['model_par_'+str(prof)][0,:],plot_dict['model_depths_'+str(prof)][0,:] , linestyle='None',marker='^',ms=10,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[2].fill_betweenx(plot_dict['model_depths_'+str(prof)][0,:],(ci2), (ci1), color='b', alpha=.1,label='Uncertainty')
axs[2].plot(np.ones(120)*1e-2, np.arange(-10,110,1),linestyle='dashed',color='k',linewidth=2)
axs[2].set_xscale('log')
axs[2].grid(linestyle=':')
axs[2].invert_yaxis()
axs[2].xaxis.tick_top()
axs[2].set_xticklabels([])
axs[2].set_yticks([0,50,100])
axs[2].text(0.1, 0.8, '75.02°N\n29-04-18\n20:31', horizontalalignment='center'
              , verticalalignment='center', transform=axs[2].transAxes, size=14, weight='bold')
axs[2].text(0.9, 0.1, 'c', rotation='horizontal', transform=axs[2].transAxes,size=20, weight='bold')

prof=144
ci1 = plot_dict['ci1_'+str(prof)][0,:]
ci2 = plot_dict['ci2_'+str(prof)][0,:]
axs[3].plot(plot_dict['glider_par_'+str(prof)][0,:],plot_dict['glider_depths_'+str(prof)][0,:], linestyle='None',marker='o',ms=10,markerfacecolor='silver',
             markeredgewidth=1, markeredgecolor='k',label='Glider' )
axs[3].plot(plot_dict['model_par_'+str(prof)][0,:],plot_dict['model_depths_'+str(prof)][0,:] , linestyle='None',marker='^',ms=10,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k',label='HEIMDALL')
axs[3].fill_betweenx(plot_dict['model_depths_'+str(prof)][0,:],(ci2), (ci1), color='b', alpha=.1,label='Cloud Range')
axs[3].plot(np.ones(120)*1e-2, np.arange(-10,110,1),linestyle='dashed',color='k',linewidth=2)
axs[3].set_xscale('log')
axs[3].grid(linestyle=':')
axs[3].invert_yaxis()
axs[3].xaxis.tick_top()
axs[3].set_xticklabels([])
axs[3].set_yticks([0,50,100])
axs[3].legend(bbox_to_anchor=(0.88, -0.01),prop=dict(size=15), ncol=3)

axs[3].text(0.1, 0.8, '75.41°N\n02-05-18\n17:19', horizontalalignment='center'
              , verticalalignment='center', transform=axs[3].transAxes, size=14, weight='bold')
axs[3].text(0.9, 0.1, 'd', rotation='horizontal', transform=axs[3].transAxes,size=20, weight='bold')

plt.subplots_adjust(wspace=0.05, hspace=0.05)