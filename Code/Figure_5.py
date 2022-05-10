##############################################################################
################################   FIGURE 5  #################################
############################################################################## 

# Plot of chlorophyll profiles used in figures 6 and 7

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'	
filename = r'\glider_transect_1_grid_data.mat'

# Glider original data managed by Porter M.; Cottier F.R.; Dumont E.; Venables E.(2020b). 
# Arctic PRIZE mission two near-real time glider dataset in the Barents Sea Winter 2018.
# British Oceanographic Data Centre, National Oceanography Centre, NERC, UK. doi:10/dmgm

glider_data= scipy.io.loadmat(path2data+filename)

# Define homogeneous column of chlorophyll profiles at concentration 1mgmg^-3, surface max profile and sub-surface max profile

glider_homog = np.ones(99)
glider_s = glider_data['grid_chl'][:,49]
glider_ss = glider_data['grid_chl'][:,81]

# Define depths
depths = glider_data['grid_pressure'][:,0]

# Plot profiles
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
fig, axs = plt.subplots(1, 3 ,figsize=(18,9))
fig.text(0.07, 0.5, 'Depth [m]', va='center', rotation='vertical',size=20,weight='bold')
fig.text(0.47, 0.945, 'Chl a [mg m$^{-3}$]', va='center',size=20,weight='bold')

fig.text(0.18, 0.07, 'Homogeneous', va='center', rotation='horizontal',size=18, weight='bold')
fig.text(0.46, 0.07, 'Surface Max', va='center', rotation='horizontal',size=18, weight='bold')
fig.text(0.72, 0.07, 'Sub-Surface Max', va='center', rotation='horizontal',size=18, weight='bold')

axs[0].plot(glider_homog,depths,linewidth=2, color='k')
axs[0].set_xscale('log')
axs[0].invert_yaxis() 
axs[0].grid(linestyle=':')
axs[0].xaxis.tick_top()
axs[0].set_xlim([5e-2, 5e1])

axs[1].plot(glider_s,depths,linewidth=2, color='k')
axs[1].set_xscale('log')
axs[1].invert_yaxis() 
axs[1].grid(linestyle=':')
axs[1].xaxis.tick_top()
axs[1].set_xlim([5e-2, 5e1])
axs[1].set_yticklabels([])

axs[2].plot(glider_ss,depths,linewidth=2, color='k')
axs[2].set_xscale('log')
axs[2].invert_yaxis() 
axs[2].grid(linestyle=':')
axs[2].xaxis.tick_top()
axs[2].set_xlim([5e-2, 5e1])
axs[2].set_yticklabels([])

# Tight layout
plt.subplots_adjust(wspace=0.05, hspace=0.03)