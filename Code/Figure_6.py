##############################################################################
################################   FIGURE 6  #################################
##############################################################################

#  Comparison of Modelled PAR and Hydrolight PAR

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'	

# Load Modelled (SP) and Hydrolight values for each condition. Variable names relate to concentration and zenith angle, e.g. s30Z is surface max at 30° zenith.
Homog_Ed_30Z = r'\SP_Hydro_PAR_Ed_Homog_1mg_30Z'
Homog_Ed_60Z = r'\SP_Hydro_PAR_Ed_Homog_1mg_60Z'
Homog_Ed_80Z = r'\SP_Hydro_PAR_Ed_Homog_1mg_80Z'

Surface_Max_Ed_30Z = r'\SP_Hydro_PAR_Ed_Surface_MAX_30Z'
Surface_Max_Ed_60Z = r'\SP_Hydro_PAR_Ed_Surface_MAX_60Z'
Surface_Max_Ed_80Z = r'\SP_Hydro_PAR_Ed_Surface_MAX_80Z'

Sub_Surface_Max_Ed_30Z = r'\SP_Hydro_PAR_Ed_Sub_Surface_MAX_30Z'
Sub_Surface_Max_Ed_60Z = r'\SP_Hydro_PAR_Ed_Sub_Surface_MAX_60Z'
Sub_Surface_Max_Ed_80Z = r'\SP_Hydro_PAR_Ed_Sub_Surface_MAX_80Z'

h30Z = scipy.io.loadmat(path + Homog_Ed_30Z )
h60Z = scipy.io.loadmat(path + Homog_Ed_60Z )
h80Z = scipy.io.loadmat(path + Homog_Ed_80Z )

s30Z = scipy.io.loadmat(path + Surface_Max_Ed_30Z )
s60Z = scipy.io.loadmat(path + Surface_Max_Ed_60Z )
s80Z = scipy.io.loadmat(path + Surface_Max_Ed_80Z )

ss30Z = scipy.io.loadmat(path + Sub_Surface_Max_Ed_30Z )
ss60Z = scipy.io.loadmat(path + Sub_Surface_Max_Ed_60Z )
ss80Z = scipy.io.loadmat(path + Sub_Surface_Max_Ed_80Z )


# Define axes
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
fig, axs = plt.subplots(3, 3 ,figsize=(18,9))


# Defining custom 'xlim' and 'ylim' values.
custom_xlim = (1e-1, 5e3)
custom_ylim = (1e-1, 5e3)
leg_size=14
# Setting the values for all axes.
plt.setp(axs, xlim=custom_xlim, ylim=custom_ylim)

fig.text(0.5, 0.04, 'E$_{D}$ $_{PAR}$ $_{HYDROLIGHT}$ [$\mu$mol m$^{-2}$s$^{-1}$]',size=20, ha='center',weight='bold')
fig.text(0.07, 0.5, 'E$_{D}$ $_{PAR}$ $_{HEIMDALL}$ [$\mu$mol m$^{-2}$s$^{-1}$]',size=20, va='center', rotation='vertical',weight='bold')

z_eu1 =np.argmax(h30Z['Hydro_PAR_Cloud_0'][:,0]<h30Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(h30Z['Hydro_PAR_Cloud_100'][:,0]<h30Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 =np.argmax(h30Z['Hydro_PAR_Cloud_50'][:,0]<h30Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(h30Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], h30Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(h30Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], h30Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(h30Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], h30Z['SP_PAR_Cloud_50'][0:z_eu1,0])


axs[0,0].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[0,0].plot(h30Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],h30Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[0,0].plot(h30Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],h30Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label ='MAE '+ str(round(MAE2,2)))
axs[0,0].plot(h30Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],h30Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label ='MAE '+ str(round(MAE3,2)))
axs[0,0].set_yscale('log')
axs[0,0].set_xscale('log')
axs[0,0].grid(linestyle=':')
axs[0,0].set_xticklabels([])
handles,labels = axs[0,0].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[0,0].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[0,0].text(0.5, 1.05, 'Homogeneous Chl', horizontalalignment='center', verticalalignment='center', transform=axs[0,0].transAxes, size=16, weight='bold')
axs[0,0].text(0.9, 0.1, 'a', rotation='horizontal', transform=axs[0,0].transAxes,size=20, weight='bold')

z_eu1 = np.argmax(s30Z['Hydro_PAR_Cloud_0'][:,0]<s30Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(s30Z['Hydro_PAR_Cloud_100'][:,0]<s30Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(s30Z['Hydro_PAR_Cloud_50'][:,0]<s30Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(s30Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], s30Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(s30Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], s30Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(s30Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], s30Z['SP_PAR_Cloud_50'][0:z_eu1,0])


axs[0,1].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[0,1].plot(s30Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],s30Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[0,1].plot(s30Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],s30Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label ='MAE '+ str(round(MAE2,2)))
axs[0,1].plot(s30Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],s30Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label ='MAE '+ str(round(MAE3,2)))
axs[0,1].set_yscale('log')
axs[0,1].set_xscale('log')
axs[0,1].grid(linestyle=':')
axs[0,1].set_xticklabels([])
axs[0,1].set_yticklabels([])
handles,labels = axs[0,1].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[0,1].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[0,1].text(0.5, 1.05, 'Surface Max Chl', horizontalalignment='center', verticalalignment='center', transform=axs[0,1].transAxes, size=16, weight='bold')
axs[0,1].text(0.9, 0.1, 'b', rotation='horizontal', transform=axs[0,1].transAxes,size=20, weight='bold')


z_eu1 = np.argmax(ss30Z['Hydro_PAR_Cloud_0'][:,0]<ss30Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(ss30Z['Hydro_PAR_Cloud_100'][:,0]<ss30Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(ss30Z['Hydro_PAR_Cloud_50'][:,0]<ss30Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(ss30Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], ss30Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(ss30Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], ss30Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(ss30Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], ss30Z['SP_PAR_Cloud_50'][0:z_eu1,0])


axs[0,2].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[0,2].plot(ss30Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],ss30Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[0,2].plot(ss30Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],ss30Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label ='MAE '+ str(round(MAE2,2)))
axs[0,2].plot(ss30Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],ss30Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label ='MAE '+ str(round(MAE3,2)))
axs[0,2].set_yscale('log')
axs[0,2].set_xscale('log')
axs[0,2].grid(linestyle=':')
axs[0,2].set_xticklabels([])
axs[0,2].set_yticklabels([])
handles,labels = axs[0,2].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[0,2].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[0,2].text(0.5, 1.05, 'Sub-Surface Max Chl', horizontalalignment='center', verticalalignment='center', transform=axs[0,2].transAxes, size=16, weight='bold')
axs[0,2].text(1.05, 0.5, r'$\theta$=30°', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0,2].transAxes, size=16, weight='bold')
axs[0,2].text(0.9, 0.1, 'c', rotation='horizontal', transform=axs[0,2].transAxes,size=20, weight='bold')



z_eu1 = np.argmax(h60Z['Hydro_PAR_Cloud_0'][:,0]<h60Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(h60Z['Hydro_PAR_Cloud_100'][:,0]<h60Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(h60Z['Hydro_PAR_Cloud_50'][:,0]<h60Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(h60Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], h60Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(h60Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], h60Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(h60Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], h60Z['SP_PAR_Cloud_50'][0:z_eu1,0])


axs[1,0].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[1,0].plot(h60Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],h60Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[1,0].plot(h60Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],h60Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE2,2)))
axs[1,0].plot(h60Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],h60Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE3,2)))
axs[1,0].set_yscale('log')
axs[1,0].set_xscale('log')
axs[1,0].grid(linestyle=':')
axs[1,0].set_xticklabels([])
handles,labels = axs[1,0].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[1,0].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[1,0].text(0.9, 0.1, 'd', rotation='horizontal', transform=axs[1,0].transAxes,size=20, weight='bold')


z_eu1 = np.argmax(s60Z['Hydro_PAR_Cloud_0'][:,0]<s60Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(s60Z['Hydro_PAR_Cloud_100'][:,0]<s60Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(s60Z['Hydro_PAR_Cloud_50'][:,0]<s60Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(s60Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], s60Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(s60Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], s60Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(s60Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], s60Z['SP_PAR_Cloud_50'][0:z_eu1,0])


axs[1,1].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[1,1].plot(s60Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],s60Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[1,1].plot(s60Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],s60Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE2,2)))
axs[1,1].plot(s60Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],s60Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE3,2)))
axs[1,1].set_yscale('log')
axs[1,1].set_xscale('log')
axs[1,1].grid(linestyle=':')
axs[1,1].set_xticklabels([])
axs[1,1].set_yticklabels([])
handles,labels = axs[1,1].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[1,1].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[1,1].text(0.9, 0.1, 'e', rotation='horizontal', transform=axs[1,1].transAxes,size=20, weight='bold')



z_eu1 = np.argmax(ss60Z['Hydro_PAR_Cloud_0'][:,0]<ss60Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(ss60Z['Hydro_PAR_Cloud_100'][:,0]<ss60Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(ss60Z['Hydro_PAR_Cloud_50'][:,0]<ss60Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(ss60Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], ss60Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(ss60Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], ss60Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(ss60Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], ss60Z['SP_PAR_Cloud_50'][0:z_eu1,0])

axs[1,2].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[1,2].plot(ss60Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],ss60Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[1,2].plot(ss60Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],ss60Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE2,2)))
axs[1,2].plot(ss60Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],ss60Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE3,2)))
axs[1,2].set_yscale('log')
axs[1,2].set_xscale('log')
axs[1,2].grid(linestyle=':')
axs[1,2].set_xticklabels([])
axs[1,2].set_yticklabels([])
handles,labels = axs[1,2].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[1,2].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[1,2].text(1.05, 0.5, r'$\theta$=60°', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1,2].transAxes, size=16, weight='bold')
axs[1,2].text(0.9, 0.1, 'f', rotation='horizontal', transform=axs[1,2].transAxes,size=20, weight='bold')


z_eu1 = np.argmax(h80Z['Hydro_PAR_Cloud_0'][:,0]<h80Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(h80Z['Hydro_PAR_Cloud_100'][:,0]<h80Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(h80Z['Hydro_PAR_Cloud_50'][:,0]<h80Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(h80Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], h80Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(h80Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], h80Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(h80Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], h80Z['SP_PAR_Cloud_50'][0:z_eu1,0])


axs[2,0].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[2,0].plot(h80Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],h80Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[2,0].plot(h80Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],h80Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE2,2)))
axs[2,0].plot(h80Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],h80Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE3,2)))
axs[2,0].set_yscale('log')
axs[2,0].set_xscale('log')
axs[2,0].grid(linestyle=':')
handles,labels = axs[2,0].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[2,0].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[2,0].text(0.9, 0.1, 'g', rotation='horizontal', transform=axs[2,0].transAxes,size=20, weight='bold')


z_eu1 = np.argmax(s80Z['Hydro_PAR_Cloud_0'][:,0]<s80Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(s80Z['Hydro_PAR_Cloud_100'][:,0]<s80Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(s80Z['Hydro_PAR_Cloud_50'][:,0]<s80Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(s80Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], s80Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(s80Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], s80Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(s80Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], s80Z['SP_PAR_Cloud_50'][0:z_eu1,0])

axs[2,1].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[2,1].plot(s80Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],s80Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[2,1].plot(s80Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],s80Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE2,2)))
axs[2,1].plot(s80Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],s80Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE3,2)))
axs[2,1].set_yscale('log')
axs[2,1].set_xscale('log')
axs[2,1].grid(linestyle=':')
axs[2,1].set_yticklabels([])
handles,labels = axs[2,1].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[2,1].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[2,1].text(0.9, 0.1, 'h', rotation='horizontal', transform=axs[2,1].transAxes,size=20, weight='bold')

z_eu1 = np.argmax(ss80Z['Hydro_PAR_Cloud_0'][:,0]<ss80Z['Hydro_PAR_Cloud_0'][0,0]*0.01)
z_eu2 = np.argmax(ss80Z['Hydro_PAR_Cloud_100'][:,0]<ss80Z['Hydro_PAR_Cloud_100'][0,0]*0.01)
z_eu3 = np.argmax(ss80Z['Hydro_PAR_Cloud_50'][:,0]<ss80Z['Hydro_PAR_Cloud_50'][0,0]*0.01)

MAE1 = mean_absolute_error(ss80Z['Hydro_PAR_Cloud_0'][0:z_eu1,0], ss80Z['SP_PAR_Cloud_0'][0:z_eu1,0])
MAE2 = mean_absolute_error(ss80Z['Hydro_PAR_Cloud_100'][0:z_eu1,0], ss80Z['SP_PAR_Cloud_100'][0:z_eu1,0])
MAE3 = mean_absolute_error(ss80Z['Hydro_PAR_Cloud_50'][0:z_eu1,0], ss80Z['SP_PAR_Cloud_50'][0:z_eu1,0])

axs[2,2].plot(np.arange(custom_xlim[0],custom_xlim[1]+1,100),np.arange(custom_xlim[0],custom_xlim[1]+1,100),
              color='k',linewidth=1.5)
axs[2,2].plot(ss80Z['Hydro_PAR_Cloud_0'][0:z_eu1,0],ss80Z['SP_PAR_Cloud_0'][0:z_eu1,0],
              linestyle='None',marker='o',ms=10,markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE1,2)))
axs[2,2].plot(ss80Z['Hydro_PAR_Cloud_100'][0:z_eu2,0],ss80Z['SP_PAR_Cloud_100'][0:z_eu2,0],
              linestyle='None',marker='^',ms=10,markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE2,2)))
axs[2,2].plot(ss80Z['Hydro_PAR_Cloud_50'][0:z_eu3,0],ss80Z['SP_PAR_Cloud_50'][0:z_eu3,0],
              linestyle='None',marker='v',ms=10,markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(MAE3,2)))
axs[2,2].set_yscale('log')
axs[2,2].set_xscale('log')
axs[2,2].grid(linestyle=':')
axs[2,2].set_yticklabels([])
handles,labels = axs[2,2].get_legend_handles_labels()
handles = [handles[0], handles[2], handles[1]]
labels = [labels[0], labels[2], labels[1]]
axs[2,2].legend(handles,labels, loc='best', prop={'size': leg_size})
axs[2,2].text(1.05, 0.5, r'$\theta$=80°', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[2,2].transAxes, size=16, weight='bold')
axs[2,2].text(0.9, 0.1, 'i', rotation='horizontal', transform=axs[2,2].transAxes,size=20, weight='bold')


plt.subplots_adjust(wspace=0.05, hspace=0.05)

# Directory to save image to. Saved image will be reloaded and have custom legend for cloud cover added.

path_2_save =  r'C:\Users\s...'
plt.savefig(path_2_save + '\Figure_C.png')

img = plt.imread(path_2_save + '\Figure_C.png')
fig, ax = plt.subplots(figsize=(18,9))
ax.imshow(img)


plt.plot([],[],marker='o',ms=14,linestyle='None',markerfacecolor='midnightblue',
             markeredgewidth=1, markeredgecolor='k',label ='Cloud:0%')
plt.plot([],[],marker='v',ms=14,linestyle='None',markerfacecolor='forestgreen',
             markeredgewidth=1, markeredgecolor='k',label ='Cloud:50%')
plt.plot([],[],marker='^',ms=14,linestyle='None',markerfacecolor='lightgrey',
             markeredgewidth=1, markeredgecolor='k',label ='Cloud:100%')
plt.legend(loc='best', bbox_to_anchor=(0.75,1),ncol=3, prop={'size': 18})
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])