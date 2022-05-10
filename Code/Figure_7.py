##############################################################################
################################   FIGURE 7  #################################
##############################################################################

#  Comparison of Modelled Spectral Ed and Hydrolight Spectral Ed - Z=1% Light


#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'

# Load modelled and Hydrolight spectral data 

SP_Homog = scipy.io.loadmat(path + '\S_P_1mg_Chl.mat')
SP_Suface = scipy.io.loadmat(path + '\S_P_Surface_MAX.mat')
SP_Sub_Surface = scipy.io.loadmat(path + '\S_P_Sub_Surface_MAX.mat')

Hydro_Homog = scipy.io.loadmat(path + '\Hydro_Ed_1mg_Homog_Manual_Run.mat')
Hydro_Suface = scipy.io.loadmat(path + '\Structured_Hydrolight_Ed_Surface_MAX.mat')
Hydro_Sub_Surface = scipy.io.loadmat(path + '\Structured_Hydrolight_Ed_Sub_Surface_MAX.mat')

# Plot data and MAE value for each aggregated condition from figure 6

matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
fig, axs = plt.subplots(3, 2 ,figsize=(20,15))
fig.text(0.5, 0.05, 'E$_{D}$($\lambda$) $_{HYDROLIGHT}$ [Wm$^{-2}$ nm$^{-1}$]',size=20, ha='center',weight='bold')
fig.text(0.07, 0.5, 'E$_{D}$($\lambda$) $_{HEIMDALL}$ [Wm$^{-2}$ nm$^{-1}$]',size=20, va='center', rotation='vertical',weight='bold')

# Defining custom 'xlim' and 'ylim' values.
custom_xlim = (1.8e-4, 3e0)
custom_ylim = (1.8e-4, 3e0)
leg_size=14
# Setting the values for all axes.
plt.setp(axs, xlim=custom_xlim, ylim=custom_ylim)

# WL is index for wavelength value of irradiance array. Arrays are of form (zenith, depth, WL index) - wavelengths are 405 - 695nm in 10nm steps.
WL=0

# Find Mean absolute error for each plot down to depth value where irradiance is 1% of surface light value.

MAE_1 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_2 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_3 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_4 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_5 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_6 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_7 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_8 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_9 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_10 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_11 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_12 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_13 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_14 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_15 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_16 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_17 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_18 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_19 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_20 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_21 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_22 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_23 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_24 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_25 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_26 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_27 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

# Average MAE value for all zeniths, clouds and profile conditions for wavelength value. 

average_MAE = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5 + MAE_6 + MAE_7 + MAE_8 + MAE_9 +
               MAE_10 + MAE_11 + MAE_12 + MAE_13 + MAE_14 + MAE_15 + MAE_16 + MAE_17 + MAE_18 +
               MAE_19 + MAE_20 + MAE_21 + MAE_22 + MAE_23 + MAE_24 + MAE_25 + MAE_26 + MAE_27)/27

color='midnightblue'
axs[0,0].text(0.91, 0.1, '405nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[0,0].transAxes, size=18,weight='bold')
axs[0,0].plot(np.linspace(custom_xlim[0],custom_xlim[1]+1,100),np.linspace(custom_xlim[0],custom_xlim[1]+1,100),linestyle='solid',
              color='k',linewidth=1.5)

axs[0,0].plot(SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(average_MAE,5)))
axs[0,0].plot(SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[0,0].plot(SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[0,0].plot(SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[0,0].plot(SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[0,0].plot(SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[0,0].plot(SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[0,0].plot(SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[0,0].plot(SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[0,0].plot(SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,0].plot(SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[0,0].set_yscale('log')
axs[0,0].set_xscale('log')
axs[0,0].grid(linestyle=':')
axs[0,0].set_xticklabels([])
axs[0,0].legend(loc=2, prop={'size': 18})


WL=5

MAE_1 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_2 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_3 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_4 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_5 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_6 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_7 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_8 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_9 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_10 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_11 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_12 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_13 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_14 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_15 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_16 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_17 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_18 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_19 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_20 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_21 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_22 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_23 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_24 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_25 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_26 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_27 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL])


average_MAE = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5 + MAE_6 + MAE_7 + MAE_8 + MAE_9 +
               MAE_10 + MAE_11 + MAE_12 + MAE_13 + MAE_14 + MAE_15 + MAE_16 + MAE_17 + MAE_18 +
               MAE_19 + MAE_20 + MAE_21 + MAE_22 + MAE_23 + MAE_24 + MAE_25 + MAE_26 + MAE_27)/27

color='cornflowerblue'
axs[0,1].text(0.91, 0.1, '455nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[0,1].transAxes, size=18,weight='bold')
axs[0,1].plot(np.linspace(custom_xlim[0],custom_xlim[1]+1,100),np.linspace(custom_xlim[0],custom_xlim[1]+1,100),linestyle='solid',
              color='k',linewidth=1.5)

axs[0,1].plot(SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(average_MAE,5)))
axs[0,1].plot(SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[0,1].plot(SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[0,1].plot(SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[0,1].plot(SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[0,1].plot(SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[0,1].plot(SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[0,1].plot(SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[0,1].plot(SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[0,1].plot(SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].plot(SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[0,1].set_yscale('log')
axs[0,1].set_xscale('log')
axs[0,1].grid(linestyle=':')
axs[0,1].set_xticklabels([])
axs[0,1].set_yticklabels([])
axs[0,1].legend(loc=2, prop={'size': 18})

WL=10

MAE_1 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_2 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_3 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_4 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_5 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_6 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_7 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_8 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_9 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_10 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_11 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_12 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_13 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_14 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_15 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_16 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_17 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_18 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_19 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_20 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_21 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_22 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_23 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_24 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_25 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_26 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_27 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL])


average_MAE = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5 + MAE_6 + MAE_7 + MAE_8 + MAE_9 +
               MAE_10 + MAE_11 + MAE_12 + MAE_13 + MAE_14 + MAE_15 + MAE_16 + MAE_17 + MAE_18 +
               MAE_19 + MAE_20 + MAE_21 + MAE_22 + MAE_23 + MAE_24 + MAE_25 + MAE_26 + MAE_27)/27

color='forestgreen'
axs[1,0].text(0.91, 0.1, '505nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[1,0].transAxes, size=18,weight='bold')
axs[1,0].plot(np.linspace(custom_xlim[0],custom_xlim[1]+1,100),np.linspace(custom_xlim[0],custom_xlim[1]+1,100),linestyle='solid',
              color='k',linewidth=1.5)

axs[1,0].plot(SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(average_MAE,5)))
axs[1,0].plot(SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[1,0].plot(SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[1,0].plot(SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[1,0].plot(SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[1,0].plot(SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[1,0].plot(SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[1,0].plot(SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[1,0].plot(SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[1,0].plot(SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].plot(SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[1,0].set_yscale('log')
axs[1,0].set_xscale('log')
axs[1,0].grid(linestyle=':')
axs[1,0].set_xticklabels([])
axs[1,0].legend(loc=2, prop={'size': 18})

WL=15

MAE_1 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_2 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_3 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_4 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_5 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_6 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_7 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_8 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_9 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_10 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_11 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_12 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_13 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_14 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_15 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_16 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_17 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_18 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_19 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_20 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_21 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_22 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_23 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_24 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_25 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_26 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_27 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL])


average_MAE = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5 + MAE_6 + MAE_7 + MAE_8 + MAE_9 +
               MAE_10 + MAE_11 + MAE_12 + MAE_13 + MAE_14 + MAE_15 + MAE_16 + MAE_17 + MAE_18 +
               MAE_19 + MAE_20 + MAE_21 + MAE_22 + MAE_23 + MAE_24 + MAE_25 + MAE_26 + MAE_27)/27

color='darkseagreen'
axs[1,1].text(0.91, 0.1, '555nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[1,1].transAxes, size=18,weight='bold')
axs[1,1].plot(np.linspace(custom_xlim[0],custom_xlim[1]+1,100),np.linspace(custom_xlim[0],custom_xlim[1]+1,100),linestyle='solid',
              color='k',linewidth=1.5)

axs[1,1].plot(SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(average_MAE,5)))
axs[1,1].plot(SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[1,1].plot(SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[1,1].plot(SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[1,1].plot(SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[1,1].plot(SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[1,1].plot(SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[1,1].plot(SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[1,1].plot(SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[1,1].plot(SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].plot(SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[1,1].set_yscale('log')
axs[1,1].set_xscale('log')
axs[1,1].grid(linestyle=':')
axs[1,1].set_xticklabels([])
axs[1,1].set_yticklabels([])
axs[1,1].legend(loc=2, prop={'size': 18})

WL=20

MAE_1 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_2 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_3 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_4 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_5 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_6 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_7 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_8 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_9 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_10 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_11 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_12 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_13 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_14 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_15 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_16 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_17 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_18 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_19 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_20 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_21 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_22 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_23 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_24 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_25 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_26 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_27 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL])


average_MAE = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5 + MAE_6 + MAE_7 + MAE_8 + MAE_9 +
               MAE_10 + MAE_11 + MAE_12 + MAE_13 + MAE_14 + MAE_15 + MAE_16 + MAE_17 + MAE_18 +
               MAE_19 + MAE_20 + MAE_21 + MAE_22 + MAE_23 + MAE_24 + MAE_25 + MAE_26 + MAE_27)/27

color='darkred'
axs[2,0].text(0.91, 0.1, '605nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[2,0].transAxes, size=18,weight='bold')
axs[2,0].plot(np.linspace(custom_xlim[0],custom_xlim[1]+1,100),np.linspace(custom_xlim[0],custom_xlim[1]+1,100),linestyle='solid',
              color='k',linewidth=1.5)

axs[2,0].plot(SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(average_MAE,5)))
axs[2,0].plot(SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[2,0].plot(SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[2,0].plot(SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[2,0].plot(SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[2,0].plot(SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[2,0].plot(SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[2,0].plot(SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[2,0].plot(SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[2,0].plot(SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].plot(SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[2,0].set_yscale('log')
axs[2,0].set_xscale('log')
axs[2,0].grid(linestyle=':')
axs[2,0].legend(loc=2, prop={'size': 18})

WL=25

MAE_1 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_2 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_3 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_4 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_5 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_6 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_7 = mean_absolute_error(Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_8 = mean_absolute_error(Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_9 = mean_absolute_error(Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_10 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_11 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_12 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_13 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_14 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_15 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_16 = mean_absolute_error(Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_17 = mean_absolute_error(Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_18 = mean_absolute_error(Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL])

MAE_19 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL] )
MAE_20 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL])
MAE_21 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL])

MAE_22 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL] )
MAE_23 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL])
MAE_24 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL])

MAE_25 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL] )
MAE_26 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
            SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL])
MAE_27 = mean_absolute_error(Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL])


average_MAE = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5 + MAE_6 + MAE_7 + MAE_8 + MAE_9 +
               MAE_10 + MAE_11 + MAE_12 + MAE_13 + MAE_14 + MAE_15 + MAE_16 + MAE_17 + MAE_18 +
               MAE_19 + MAE_20 + MAE_21 + MAE_22 + MAE_23 + MAE_24 + MAE_25 + MAE_26 + MAE_27)/27

color='coral'
axs[2,1].text(0.91, 0.1, '655nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[2,1].transAxes, size=18,weight='bold')
axs[2,1].plot(np.linspace(custom_xlim[0],custom_xlim[1]+1,100),np.linspace(custom_xlim[0],custom_xlim[1]+1,100),linestyle='solid',
              color='k',linewidth=1.5)

axs[2,1].plot(SP_Homog['Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Homog['Ed_0_Cloud'][3,:,WL]<SP_Homog['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Homog['Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Homog['Ed_50_Cloud'][3,:,WL]<SP_Homog['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Homog['Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Homog['Ed_100_Cloud'][3,:,WL]<SP_Homog['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k',label = 'MAE '+str(round(average_MAE,5)))

axs[2,1].plot(SP_Homog['Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][6,0:np.argmax(SP_Homog['Ed_0_Cloud'][6,:,WL]<SP_Homog['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Homog['Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][6,0:np.argmax(SP_Homog['Ed_50_Cloud'][6,:,WL]<SP_Homog['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Homog['Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][6,0:np.argmax(SP_Homog['Ed_100_Cloud'][6,:,WL]<SP_Homog['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[2,1].plot(SP_Homog['Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_0_Cloud'][8,0:np.argmax(SP_Homog['Ed_0_Cloud'][8,:,WL]<SP_Homog['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Homog['Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_50_Cloud'][8,0:np.argmax(SP_Homog['Ed_50_Cloud'][8,:,WL]<SP_Homog['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Homog['Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Homog['Hydro_Ed_100_Cloud'][8,0:np.argmax(SP_Homog['Ed_100_Cloud'][8,:,WL]<SP_Homog['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')


axs[2,1].plot(SP_Suface['Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Suface['Ed_0_Cloud'][3,:,WL]<SP_Suface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Suface['Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Suface['Ed_50_Cloud'][3,:,WL]<SP_Suface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Suface['Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Suface['Ed_100_Cloud'][3,:,WL]<SP_Suface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[2,1].plot(SP_Suface['Ed_0_Cloud'][6,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Suface['Ed_0_Cloud'][6,:,WL]<SP_Suface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Suface['Ed_50_Cloud'][6,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Suface['Ed_50_Cloud'][6,:,WL]<SP_Suface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Suface['Ed_100_Cloud'][6,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Suface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Suface['Ed_100_Cloud'][6,:,WL]<SP_Suface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[2,1].plot(SP_Suface['Ed_0_Cloud'][8,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Suface['Ed_0_Cloud'][8,:,WL]<SP_Suface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Suface['Ed_50_Cloud'][8,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Suface['Ed_50_Cloud'][8,:,WL]<SP_Suface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Suface['Ed_100_Cloud'][8,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Suface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Suface['Ed_100_Cloud'][8,:,WL]<SP_Suface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[2,1].plot(SP_Sub_Surface['Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][3,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Sub_Surface['Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Sub_Surface['Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][1,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][3,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][3,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')

axs[2,1].plot(SP_Sub_Surface['Ed_0_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][6,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Sub_Surface['Ed_50_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Sub_Surface['Ed_100_Cloud'][6,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
            Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][2,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][6,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][6,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
              markeredgewidth=1, markeredgecolor='k')


axs[2,1].plot(SP_Sub_Surface['Ed_0_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_0_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_0_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_0_Cloud'][8,0,WL]*0.01),WL],
           linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Sub_Surface['Ed_50_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_50_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_50_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_50_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].plot(SP_Sub_Surface['Ed_100_Cloud'][8,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
           Hydro_Sub_Surface['Hydro_Ed_100_Cloud'][3,0:np.argmax(SP_Sub_Surface['Ed_100_Cloud'][8,:,WL]<SP_Sub_Surface['Ed_100_Cloud'][8,0,WL]*0.01),WL],
          linestyle='None',marker='o',ms=10,markerfacecolor=color,
             markeredgewidth=1, markeredgecolor='k')

axs[2,1].set_yscale('log')
axs[2,1].set_xscale('log')
axs[2,1].grid(linestyle=':')
axs[2,1].set_yticklabels([])
axs[2,1].legend(loc=2, prop={'size': 18})

plt.subplots_adjust(wspace=0.05, hspace=0.05)

