##############################################################################
################################   FIGURE 3   ################################
##############################################################################

#  Comparison of USSIMO and Modelled irradiances using Spitshcan et al., 2016 and Kollath et al., 2020 - clear sky and moon free conditions
#  Spitschan/Kollath data has been linearly interpolated for smooth and equally spaced bins.

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'						

#Specify file names for USSIMO data and Spitschan et al. data.

# Berge J, Grant S, Bjørgum R, Cohen JH, McKee D, Johnsen G, Zolich A, Kopec TP, Vogedes DL (2021) 
# USSIMO spectroradiometer raw data time series (2018) measured under the dome of a light observatory in the Arctic (Ny-Ålesund, Svalbard, Norway).
# Norstore. doi:10.11582/2021.00044		

# Spitschan, M., Aguirre, G., Brainard, D., & Sweeney, A. (2016). 
# Variation of outdoor illumination as a function of solar elevation and light pollution. Scientific Reports, 6(1). doi: 10.1038/srep26756

# Kolláth, Z., Cool, A., Jechow, A., Kolláth, K., Száz, D., & Tong, K. (2020). 
# Introducing the dark sky unit for multi-spectral measurement of the night sky quality with commercial digital cameras. 
# Journal Of Quantitative Spectroscopy And Radiative Transfer, 253, 107162. doi: 10.1016/j.jqsrt.2020.107162
	
# Name USSIMO data    
filename_USSIMO = '\Moon_Free_Cloud_Free_USSIMO_PAR_irrad'


# Load data from USSIMO - data from Berge et al. has been filtered for lunar illumination <0.3 and cloud cover <10%
# Filtered data included here but original dataset available from source listed above. 
USSIMO_Light = scipy.io.loadmat(path_to_data + filename_USSIMO)

# Load light and zenith values for USSIMO data.
# Cloud free USSIMO data in the range 400-700nm
USSIMO_PAR = USSIMO_Light['Cloud_moon_free_irrad']               
USSIMO_Zens = USSIMO_Light['Cloud_moon_free_zens']

# List indicies of zeniths in ascending order and sort accordingly
USSIMO_inds = USSIMO_Zens.argsort()
USSIMO_Zens_sorted = np.sort(USSIMO_Zens)
USSIMO_PAR_Sorted = np.squeeze( USSIMO_PAR[USSIMO_inds,:])


# Specify filename of  Spitschan/Kollath data - load linearly interpolated irradiance and define zenith angles
file = r'\Spitschan_Kollath_Diffuse_irrad.mat'
Model_Light = scipy.io.loadmat(path_to_data + file)['Modelled_Diffuse_irrad']
Model_zens = np.arange(88,121,1)


# Plot data
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
fig, axs = plt.subplots(3, 2 ,figsize=(20,15))
fig.text(0.5, 0.05, 'Solar Zenith [°]',size=20, ha='center',weight='bold')
fig.text(0.07, 0.5, 'E$_{D}$($\lambda$) [Wm$^{-2}$ nm$^{-1}$]',size=20, va='center', rotation='vertical',weight='bold')


axs[0,0].plot(Model_zens[0:19],Model_Light[0:19,0]
              ,linestyle='solid', linewidth = 2, color='k', label='Spitschan et al. 2016')
axs[0,0].plot(Model_zens[18:],Model_Light[18:,0]
              ,linestyle='dotted', linewidth = 2, color='k', label='Kolláth et al. 2020')
axs[0,0].plot(USSIMO_Zens_sorted[0,:19],USSIMO_PAR_Sorted[:19,0]
              ,linestyle='None', marker='o', ms=12 ,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k', label='USSIMO Instrument')
axs[0,0].set_yscale('log')
axs[0,0].grid(linestyle=':')
axs[0,0].text(0.91, 0.9, '405nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[0,0].transAxes, size=18, weight='bold')
axs[0,0].set_ylim(3e-10,4e-1)
axs[0,0].set_xticklabels([])
axs[0,0].legend(bbox_to_anchor=(1.7, 1.3),prop=dict(size=18), ncol=3)
axs[0,0].text(105,3e-4,'Irradiance Baseline',size=16,style='italic')
axs[0,0].annotate('', xy=(0.55, 0.60), xycoords='axes fraction', xytext=(0.55, 0.2), 
            arrowprops=dict(arrowstyle="<-", color='darkred',linewidth=2))

axs[0,1].plot(Model_zens[0:19],Model_Light[0:19,1]
              ,linestyle='solid', linewidth = 2, color='k')
axs[0,1].plot(Model_zens[18:],Model_Light[18:,1]
              ,linestyle='dotted', linewidth = 2, color='k')
axs[0,1].plot(USSIMO_Zens_sorted[0,:19],USSIMO_PAR_Sorted[:19,5]
              ,linestyle='None', marker='o', ms=12 ,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[0,1].set_yscale('log')
axs[0,1].grid(linestyle=':')
axs[0,1].text(0.91, 0.9, '455nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[0,1].transAxes, size=18, weight='bold')
axs[0,1].set_ylim(3e-10,4e-1)
axs[0,1].set_xticklabels([])
axs[0,1].set_yticklabels([])


axs[1,0].plot(Model_zens[0:19],Model_Light[0:19,2]
              ,linestyle='solid', linewidth = 2, color='k')
axs[1,0].plot(Model_zens[18:],Model_Light[18:,2]
              ,linestyle='dotted', linewidth = 2, color='k')
axs[1,0].plot(USSIMO_Zens_sorted[0,:19],USSIMO_PAR_Sorted[:19,10]
              ,linestyle='None', marker='o', ms=12 ,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[1,0].set_yscale('log')
axs[1,0].grid(linestyle=':')
axs[1,0].text(0.91, 0.9, '505nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[1,0].transAxes, size=18, weight='bold')
axs[1,0].set_ylim(3e-10,4e-1)
axs[1,0].set_xticklabels([])


axs[1,1].plot(Model_zens[0:19],Model_Light[0:19,3]
              ,linestyle='solid', linewidth = 2, color='k')
axs[1,1].plot(Model_zens[18:],Model_Light[18:,3]
              ,linestyle='dotted', linewidth = 2, color='k')
axs[1,1].plot(USSIMO_Zens_sorted[0,:19],USSIMO_PAR_Sorted[:19,15]
              ,linestyle='None', marker='o', ms=12 ,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[1,1].set_yscale('log')
axs[1,1].grid(linestyle=':')
axs[1,1].text(0.91, 0.9, '555nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[1,1].transAxes, size=18, weight='bold')
axs[1,1].set_ylim(3e-10,4e-1)
axs[1,1].set_xticklabels([])
axs[1,1].set_yticklabels([])



axs[2,0].plot(Model_zens[0:19],Model_Light[0:19,4]
              ,linestyle='solid', linewidth = 2, color='k')
axs[2,0].plot(Model_zens[18:],Model_Light[18:,4]
              ,linestyle='dotted', linewidth = 2, color='k')
axs[2,0].plot(USSIMO_Zens_sorted[0,:19],USSIMO_PAR_Sorted[:19,20]
              ,linestyle='None', marker='o', ms=12 ,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[2,0].set_yscale('log')
axs[2,0].grid(linestyle=':')
axs[2,0].text(0.91, 0.9, '605nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[2,0].transAxes, size=18, weight='bold')
axs[2,0].set_ylim(3e-10,4e-1)


axs[2,1].plot(Model_zens[0:19],Model_Light[0:19,5]
              ,linestyle='solid', linewidth = 2, color='k')
axs[2,1].plot(Model_zens[18:],Model_Light[18:,5]
              ,linestyle='dotted', linewidth = 2, color='k')
axs[2,1].plot(USSIMO_Zens_sorted[0,:19],USSIMO_PAR_Sorted[:19,25]
              ,linestyle='None', marker='o', ms=12 ,markerfacecolor='darkblue',
             markeredgewidth=1, markeredgecolor='k')
axs[2,1].set_yscale('log')
axs[2,1].grid(linestyle=':')
axs[2,1].text(0.91, 0.9, '655nm', horizontalalignment='center'
              , verticalalignment='center', transform=axs[2,1].transAxes, size=18, weight='bold')
axs[2,1].set_ylim(3e-10,4e-1)
axs[2,1].set_yticklabels([])

# Tight layout of plots
plt.subplots_adjust(wspace=0.05, hspace=0.05)

##############################################################################
