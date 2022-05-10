##############################################################################
################################   FIGURE 4  #################################
##############################################################################

#  Comparison of Camera PAR measured at ArcLight, Ny Alesund and Modelled PAR from HEIMDALL

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'		

# name files containing modelled data from HEIMDALL for location of ARCLight Observatory and local lunar zenith angles.
# Lunar zenith angles determined via Rhodes, B. 2019 
# Skyfield: High Precision Research-Grade Positions for Planets and Earth Satellites Generator (Astrophysics Source Code Library) (record ascl:1907.024) Feb 2019.

filename_Model_Jan = r'\Modelled_Irrad_Ny_Alesund_Jan_2018.mat'
filename_Model_Apr = r'\Modelled_Irrad_Ny_Alesund_April_2018.mat'
filename_Model_Jul = r'\Modelled_Irrad_Ny_Alesund_July_2018.mat'
filename_zeniths = r'\Camera_Lunar_Zeniths.mat'

# Name camera irradiance data file.
# Johnsen G, Grant S, Bjørgum R, Cohen JH, McKee D, Kopec TP, Vogedes DL, Berge J, Zolich A (2021b)
# Time series (2018) of irradiance in the PAR (photosynthetically active radiation) region measured under the dome of a light observatory in the Arctic (Ny-Ålesund, Svalbard, Norway)
# derived from SLR camera. Norstore. doi:10.11582/2021.00048 

# Note data is measured in UTC+1 
filename_Camera = r'\2018__mat_021-03-05.csv'

# Load files to plot representing lunar phase
im1 = image.imread('Half_1_Moon.png')
im2 = image.imread('New_Moon.png')
im3 = image.imread('Full_Moon.png')
im4 = image.imread('Half_2_Moon.png')

# Load in modelled data
Jan_Model_Data = scipy.io.loadmat(path_to_Model_data + filename_Model_Jan)
Apr_Model_Data = scipy.io.loadmat(path_to_Model_data + filename_Model_Apr)
Jul_Model_Data = scipy.io.loadmat(path_to_Model_data + filename_Model_Jul)
Zens_Data = scipy.io.loadmat(path_to_Model_data + filename_zeniths)

# Load in measured camera data
Camera_Light = np.array(pd.read_csv(path_to_Camera_data + filename_Camera) ['PAR [W m-2]'])   

Jan_Model_Light = Jan_Model_Data['Spectarl_Ed']
Apr_Model_Light = Apr_Model_Data['Spectral_Ed']
Jul_Model_Light = Jul_Model_Data['Spectral_Ed']

Jan_lunar_zen = Zens_Data['Jan_lunar_zenith']
Apr_lunar_zen = Zens_Data['Apr_lunar_zenith']
Jul_lunar_zen = Zens_Data['Jul_lunar_zenith']


Jan_Model_Cloud = Jan_Model_Data['Cloud']
Apr_Model_Cloud = Apr_Model_Data['Cloud']
Jul_Model_Cloud = Jul_Model_Data['Cloud']

# Load in measured timestamps
Jan_Timestamps = Jan_Model_Data['time_stamps'][:,0:718]
Apr_Timestamps = Apr_Model_Data['timestamps']
Jul_Timestamps = Jul_Model_Data['timestamps']

# Convert modelled spectral irradiance to broadband Ed

Jan_Modelled_PAR = np.zeros((len(Jan_Model_Light[0:718,0]),1))
Apr_Modelled_PAR = np.zeros((len(Apr_Model_Light[:,0]),1))
Jul_Modelled_PAR = np.zeros((len(Jul_Model_Light[:,0]),1))


for i in range(len(Jan_Modelled_PAR[:,0])):
    Jan_Modelled_PAR[i,0] = np.sum(Jan_Model_Light[i,:]) * 10
    
for i in range(len(Apr_Modelled_PAR[:,0])):
    Apr_Modelled_PAR[i,0] = np.sum(Apr_Model_Light[i,:]) * 10

for i in range(len(Jul_Modelled_PAR[:,0])):
    Jul_Modelled_PAR[i,0] = np.sum(Jul_Model_Light[i,:]) * 10    
    
    
# Determine uncertainty range of model using cloud
# Model from Kasten, F., & Czeplak, G. (1980). 
# Solar and terrestrial radiation dependent on the amount and type of cloud. Solar Energy, 24(2), 177-189. doi: 10.1016/0038-092x(80)90391-6

def clear_value_ed(Ed,Cld):
    Ed_Clear = Ed / ((1-0.75*(Cld**3.4)))    
    return Ed_Clear

def overcast_value_ed(Ed):
    Ed_Cloud = Ed * ((1-0.75*(1**3.4)))  
    return Ed_Cloud

# Create irradiance arrays for clear sky and overcast to use as boundaries on plot

Jan_Modelled_Ed_Clear = np.zeros((len(Jan_Modelled_PAR[:,0]),1))
Apr_Modelled_Ed_Clear = np.zeros((len(Apr_Modelled_PAR[:,0]),1))
Jul_Modelled_Ed_Clear = np.zeros((len(Jul_Modelled_PAR[:,0]),1))

Jan_Modelled_Ed_Overcast = np.zeros((len(Jan_Modelled_PAR[:,0]),1))
Apr_Modelled_Ed_Overcast = np.zeros((len(Apr_Modelled_PAR[:,0]),1))
Jul_Modelled_Ed_Overcast = np.zeros((len(Jul_Modelled_PAR[:,0]),1))

for i in range(len(Jan_Modelled_PAR[:,0])):
    Jan_Modelled_Ed_Clear[i,0] = clear_value_ed(Jan_Modelled_PAR[i,0], (Jan_Model_Cloud[0,i])/100)
    Jan_Modelled_Ed_Overcast[i,0] = overcast_value_ed(Jan_Modelled_PAR[i,0])

for i in range(len(Apr_Modelled_PAR[:,0])):
    Apr_Modelled_Ed_Clear[i,0] = clear_value_ed(Apr_Modelled_PAR[i,0], (Apr_Model_Cloud[0,i])/100)
    Apr_Modelled_Ed_Overcast[i,0] = overcast_value_ed(Apr_Modelled_PAR[i,0])
    
for i in range(len(Jul_Modelled_PAR[:,0])):
    Jul_Modelled_Ed_Clear[i,0] = clear_value_ed(Jul_Modelled_PAR[i,0], (Jul_Model_Cloud[0,i])/100)
    Jul_Modelled_Ed_Overcast[i,0] = overcast_value_ed(Jul_Modelled_PAR[i,0])    

    
# Uncertainty boundaries    
Jan_ci2 = Jan_Modelled_Ed_Clear[:,0]
Jan_ci1 = Jan_Modelled_Ed_Overcast [:,0]

Apr_ci2 = Apr_Modelled_Ed_Clear[:,0]
Apr_ci1 = Apr_Modelled_Ed_Overcast [:,0]

Jul_ci2 = Jul_Modelled_Ed_Clear[:,0]
Jul_ci1 = Jul_Modelled_Ed_Overcast [:,0]

# Check for duplicate timestamps in camera data and remove duplicates - convert to hour only only have 1 per hour 

Jan_datetimes = [datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H') for x in Jan_Timestamps[0,:]]
Apr_datetimes = [datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H') for x in Apr_Timestamps[0,:]]
Jul_datetimes = [datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H') for x in Jul_Timestamps[0,:]]

Jan_duplicate_indices = [idx for idx, item in enumerate(Jan_datetimes) if item in Jan_datetimes[:idx]]
Apr_duplicate_indices = [idx for idx, item in enumerate(Apr_datetimes) if item in Apr_datetimes[:idx]]
Jul_duplicate_indices = [idx for idx, item in enumerate(Jul_datetimes) if item in Jul_datetimes[:idx]]


Jan_Camera_PAR = Camera_Light[0:718]
Apr_Camera_PAR = Camera_Light[2073:2798]
Jul_Camera_PAR = Camera_Light[4334:5303]

Jan_Timestamps = np.squeeze(Jan_Timestamps)
Jan_Modelled_PAR = np.squeeze(Jan_Modelled_PAR)

Apr_Timestamps = np.squeeze(Apr_Timestamps)
Apr_Modelled_PAR = np.squeeze(Apr_Modelled_PAR)

Jul_Timestamps = np.squeeze(Jul_Timestamps)
Jul_Modelled_PAR = np.squeeze(Jul_Modelled_PAR)


Jan_Timestamps = Jan_Timestamps[~np.isin(np.arange(Jan_Timestamps.size), Jan_duplicate_indices)]
Jan_Camera_PAR = Jan_Camera_PAR[~np.isin(np.arange(Jan_Camera_PAR.size), Jan_duplicate_indices)]
Jan_Modelled_PAR = Jan_Modelled_PAR[~np.isin(np.arange(Jan_Modelled_PAR.size), Jan_duplicate_indices)]
Jan_ci1 = Jan_ci1[~np.isin(np.arange(Jan_ci1.size), Jan_duplicate_indices)]
Jan_ci2 = Jan_ci2[~np.isin(np.arange(Jan_ci2.size), Jan_duplicate_indices)]


Apr_Timestamps = Apr_Timestamps[~np.isin(np.arange(Apr_Timestamps.size), Apr_duplicate_indices)]
Apr_Camera_PAR = Apr_Camera_PAR[~np.isin(np.arange(Apr_Camera_PAR.size), Apr_duplicate_indices)]
Apr_Modelled_PAR = Apr_Modelled_PAR[~np.isin(np.arange(Apr_Modelled_PAR.size), Apr_duplicate_indices)]
Apr_ci1 = Apr_ci1[~np.isin(np.arange(Apr_ci1.size), Apr_duplicate_indices)]
Apr_ci2 = Apr_ci2[~np.isin(np.arange(Apr_ci2.size), Apr_duplicate_indices)]


Jul_Timestamps = Jul_Timestamps[~np.isin(np.arange(Jul_Timestamps.size), Jul_duplicate_indices)]
Jul_Camera_PAR = Jul_Camera_PAR[~np.isin(np.arange(Jul_Camera_PAR.size), Jul_duplicate_indices)]
Jul_Modelled_PAR = Jul_Modelled_PAR[~np.isin(np.arange(Jul_Modelled_PAR.size), Jul_duplicate_indices)]
Jul_ci1 = Jul_ci1[~np.isin(np.arange(Jul_ci1.size), Jul_duplicate_indices)]
Jul_ci2 = Jul_ci2[~np.isin(np.arange(Jul_ci2.size), Jul_duplicate_indices)]

# Find solar zenith, lunar zenith and lunar phase for timestamps.
# Requires solar zenith calculator from Reda, I., & Andreas, A. (2004). 
# Solar position algorithm for solar radiation applications. Solar Energy, 76(5), 577-589. doi: 10.1016/j.solener.2003.12.003

# Define approx latitude and longitude for ArcLight observatory

lat = 79
lon = 12

import sys

#define path where solar zenith calculator has been saved
path_2_module = r'C:\Users\...'
sys.path.append(path_2_module)

from Solar_Zenith_Calculator import zenith_calculator

# Calculate solar zenith angle for timestamps in each month
Jan_solar_zeniths = [zenith_calculator(lat, lon, str(t)) for t in Jan_Timestamps]
Apr_solar_zeniths = [zenith_calculator(lat, lon, str(int(t))) for t in Apr_Timestamps]
Jul_solar_zeniths = [zenith_calculator(lat, lon, str(int(t))) for t in Jul_Timestamps]


# Plot camera PAR and Modelled PAR with uncertainty

matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
fig, axs = plt.subplots(3, 1,figsize=(20,15))

fig.text(0.07, 0.5, 'E$_{D\ PAR}$ [W m$^{-2}$]', va='center', rotation='vertical',size=20,weight='bold')
fig.text(0.45, 0.06, 'Day of Month', va='center', rotation='horizontal',size=20,weight='bold')
fig.text(0.935, 0.5, 'Elevation [°]', va='center', rotation='vertical',size=20,weight='bold')

space = 150000/2.8
axs[0].plot(Jan_Timestamps,Jan_Camera_PAR*1.19,linewidth=2.5, color='darkred',linestyle='dotted',label='ArcLight PAR')
axs[0].plot(Jan_Timestamps,Jan_Modelled_PAR,linewidth=2.5, color='darkblue',linestyle='dashed',label='HEIMDALL PAR')
axs[0].set_yscale('log')
axs[0].set_xticks([Jan_Timestamps[0]-1000,Jan_Timestamps[320]+2000 ,Jan_Timestamps[-1]-86400])
axs[0].set_xticklabels(['','',''])                 
axs[0].fill_between(Jan_Timestamps, Jan_ci1, Jan_ci2, color='grey', alpha=.3,label='Cloud Range')
axs[0].grid(linestyle=':')
axs[0].set_ylim([5e-8,9e4])
axs[0].text(0.025, 0.5, 'JAN', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0].transAxes, size=18, weight='bold')
axs[0].set_xlim(right=Jan_Timestamps[-1]+43032)
ax3 = axs[0].twinx()

ax3.imshow(im3, aspect='auto', extent=(Jan_Timestamps[24] - space, Jan_Timestamps[24] + space, 30, 45), zorder=-1)
ax3.imshow(im1, aspect='auto', extent=(Jan_Timestamps[181] - space, Jan_Timestamps[181] + space, 30, 45), zorder=-1)
ax3.imshow(im2, aspect='auto', extent=(Jan_Timestamps[370] - space, Jan_Timestamps[370] + space, 30, 45), zorder=-1)
ax3.imshow(im4, aspect='auto', extent=(Jan_Timestamps[554] - space, Jan_Timestamps[554] + space, 30, 45), zorder=-1)
ax3.imshow(im3, aspect='auto', extent=(Jan_Timestamps[707] - space, Jan_Timestamps[707] + space, 30, 45), zorder=-1)
ax3.plot(Jan_Timestamps,[(90-x) for x in Jan_solar_zeniths],linestyle='solid',color='goldenrod',label='Solar Elevation')
ax3.plot(Jan_Timestamps,[(90-x) for x in Jan_lunar_zen[0,:]],linestyle='dashdot',color='darkolivegreen',label='Lunar Elevation')
ax3.set_ylim([-35,47])
h1, l1 = axs[0].get_legend_handles_labels()
h2, l2 = ax3.get_legend_handles_labels()
axs[0].legend(h1+h2, l1+l2, bbox_to_anchor=(0.995, 1.27),prop=dict(size=18), ncol=5)

axs[1].plot(Apr_Timestamps,Apr_Camera_PAR*1.19,linewidth=2.5, color='darkred',linestyle='dotted')
axs[1].plot(Apr_Timestamps,Apr_Modelled_PAR, linewidth=2.5, color='darkblue',linestyle='dashed')
axs[1].set_yscale('log')
axs[1].set_xticks([Apr_Timestamps[0]+2000,Apr_Timestamps[315], Apr_Timestamps[-1]])
axs[1].set_xticklabels(['','',''])                 
axs[1].fill_between(Apr_Timestamps, Apr_ci1, Apr_ci2, color='grey', alpha=.3)
axs[1].grid(linestyle=':')
axs[1].set_ylim([5e-8,9e4])
axs[1].text(0.025, 0.5, 'APR', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1].transAxes, size=18, weight='bold')
axs[1].set_xlim(right=Apr_Timestamps[-1]+3*43032)
ax4 = axs[1].twinx()

ax4.imshow(im1, aspect='auto', extent=(Apr_Timestamps[165] - space, Apr_Timestamps[165] + space, 30, 45), zorder=1)
ax4.imshow(im2, aspect='auto', extent=(Apr_Timestamps[341] - space, Apr_Timestamps[341] + space, 30, 45), zorder=-1)
ax4.imshow(im4, aspect='auto', extent=(Apr_Timestamps[482] - space, Apr_Timestamps[482] + space, 30, 45), zorder=-1)
ax4.imshow(im3, aspect='auto', extent=(Apr_Timestamps[592] - space, Apr_Timestamps[592] + space, 30, 45), zorder=-1)
ax4.plot(Apr_Timestamps,[(90-x) for x in Apr_solar_zeniths],linestyle='solid',color='goldenrod')
ax4.plot(Apr_Timestamps,[(90-x) for x in Apr_lunar_zen[0,:]],linestyle='dashdot',color='darkolivegreen')
ax4.set_ylim([-35,47])


axs[2].plot(Jul_Timestamps,Jul_Camera_PAR*1.19,linewidth=2.5, color='darkred',linestyle='dotted')
axs[2].plot(Jul_Timestamps,Jul_Modelled_PAR,linewidth=2.5, color='darkblue',linestyle='dashed')
axs[2].set_yscale('log')
axs[2].set_xticks([Jul_Timestamps[0] ,Jul_Timestamps[333], Jul_Timestamps[-1]-86400])
axs[2].set_xticklabels(['01', '15','31'])
axs[2].fill_between(Jul_Timestamps, Jul_ci1, Jul_ci2, color='grey', alpha=.3)
axs[2].grid(linestyle=':')
axs[2].set_ylim([5e-8,9e4])
axs[2].text(0.025, 0.5, 'JUL', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[2].transAxes, size=18, weight='bold')
axs[2].set_xlim(right=Jul_Timestamps[-1]+43032)
plt.subplots_adjust(wspace=0.05, hspace=0.03)
ax5 = axs[2].twinx()


ax5.plot(Jul_Timestamps,[(90-x) for x in Jul_solar_zeniths],linestyle='solid',color='goldenrod')
ax5.plot(Jul_Timestamps,[(90-x) for x in Jul_lunar_zen[0,:]],linestyle='dashdot',color='darkolivegreen')
ax5.imshow(im1, aspect='auto', extent=(Jul_Timestamps[127] - space, Jul_Timestamps[127] + space, 30, 45), zorder=1)
ax5.imshow(im2, aspect='auto', extent=(Jul_Timestamps[290] - space, Jul_Timestamps[290] + space, 30, 45), zorder=-1)
ax5.imshow(im4, aspect='auto', extent=(Jul_Timestamps[451] - space, Jul_Timestamps[451] + space, 30, 45), zorder=-1)
ax5.imshow(im3, aspect='auto', extent=(Jul_Timestamps[641] - space, Jul_Timestamps[641] + space, 30, 45), zorder=-1)
ax5.set_ylim([-35,47])

##############################################################################
##############################################################################