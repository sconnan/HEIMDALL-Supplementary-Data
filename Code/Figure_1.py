##############################################################################
################################   FIGURE 1  #################################
##############################################################################

#  Spitschan et al., 2016 zenith shifted data plot.

#Specifiy path to where data is stored on your machine
path_to_data = r'C:\Users\...'

# Load in Rural sepctra and wavelength data. 
# Data managed by Spitschan, M., Aguirre, G., Brainard, D., & Sweeney, A. (2016). 
# Variation of outdoor illumination as a function of solar elevation and light pollution. Scientific Reports, 6(1). doi: 10.1038/srep26756
df=pd.read_csv(path + '\Rural_Spectra.csv')   
df2=pd.read_csv(path + '\wavelengths.csv') 

# read in measured solar elevation,lunar phase, datetime and wavelengths
solar_elevs_measured = np.array(df.iloc[1,:-1])
datetime_measured = np.array(df.columns[:-1])
wavelengths = np.array(df2)
moon_illum_measured = np.array(df.iloc[3,:-1])

# Spitschan uses "visible range" - 400-800nm. Read in this to reproduce plot.
spectral_irrad = np.array(df.iloc[4:,:-1])
wl_matched_spectral_irrad = spectral_irrad[120:521,:]
wl_matched_wls = wavelengths[120:521,:]



#find indices where moon illumination is <0.3 (paper states this is min threshold to minimise additional irradiance from moon)
idx = np.where(moon_illum_measured < 0.3)

# Pick out measurements for spectra, zenith and timestamp when moon was negligible
# This is to match data plots of Spitschan as they filtered for 'no moon' <0.3 fraction

no_moon_spectral_irrad = np.zeros((401,1759))
no_moon_solar_elevs = np.zeros(1759)
no_moon_timestamps = list(np.zeros(1759))


for i in range(1759):
    no_moon_spectral_irrad[:,i] = wl_matched_spectral_irrad[:,idx[0][i]]
    no_moon_solar_elevs[i] = solar_elevs_measured[idx[0][i]]
    no_moon_timestamps[i] = datetime_measured[idx[0][i]]


#Separate into before and afternoon values

before_noon_timestamps = []
after_noon_timestamps = []
before_noon_solar_elevs = []
after_noon_solar_elevs = []
before_noon_irrad = []
after_noon_irrad = []

for i in range(len(no_moon_timestamps)):
    
    date_check = datetime.strptime(no_moon_timestamps[i], "%d-%b-%Y %H:%M:%S")
    if date_check.hour >= 12:
        after_noon_timestamps.append(no_moon_timestamps[i])
        after_noon_solar_elevs.append(no_moon_solar_elevs[i])
        after_noon_irrad.append(np.sum(no_moon_spectral_irrad[:,i]))
    else:
        before_noon_timestamps.append(no_moon_timestamps[i])
        before_noon_solar_elevs.append(no_moon_solar_elevs[i])
        before_noon_irrad.append(np.sum(no_moon_spectral_irrad[:,i]))
        
# Calculate modelled zeniths using datetime info from dataframe (df). 
# Requires solar zenith calculator from Reda, I., & Andreas, A. (2004). 

import sys
# Define path where solar zenith calculator is saved
path_2_module = r'C:\Users\...'
sys.path.append(path_2_module)

from Solar_Zenith_Calculator import zenith_calculator


def dt2ts(dt):
    """Converts a datetime object to UTC timestamp

    naive datetime will be considered UTC.

    """

    return calendar.timegm(dt.utctimetuple())

# Convert local timestamps to unix timestamps
unix_time_local_before_noon = [int(dt2ts(datetime.strptime(before_noon_timestamps[i], "%d-%b-%Y %H:%M:%S")))
                  for i in range(len(before_noon_timestamps))]
unix_time_local_after_noon = [int(dt2ts(datetime.strptime(after_noon_timestamps[i], "%d-%b-%Y %H:%M:%S")))
                  for i in range(len(after_noon_timestamps))]

# Shift to UTC - Location and time was - 4 hour UTC. 
# Confirmed at https://gml.noaa.gov/grad/solcalc/
unix_times_before_noon_UTC = [(x + 14400)  for x in unix_time_local_before_noon]
unix_times_after_noon_UTC = [(x + 14400)  for x in unix_time_local_after_noon]

# Calculate zeniths/elevations for location/unix time - moon phase <0.3. This is to compared binned elevation calculated here
# against binned elevation provided by Spitschan et al., 2016.

# Lat/Lon defined in Spitschan et al., 2016 for "Rural Location".
lat = 41.6646
lon= -77.8125

before_noon_modelled_zeniths = [zenith_calculator(lat, lon, str(t)) for t in unix_times_before_noon_UTC]
after_noon_modelled_zeniths = [zenith_calculator(lat, lon, str(t)) for t in unix_times_after_noon_UTC]

# Calculate elevation from zenith angles - data is presented as function of elevtion in Spitschan et al., 2016.
before_modelled_elevs = [(90-x) for x in before_noon_modelled_zeniths]
after_modelled_elevs = [(90-x) for x in after_noon_modelled_zeniths]

# Now have before and afternoon modelled and measured zeniths v irradiance
# Need to bin and average irradiance values to match data plotted by Spitschan. Averaged into 2° elevation bins.

def myRound(n):
    answer = round(n)
    if not answer%2:
        return answer
    if abs(answer+1-n) < abs(answer-1-n):
        return answer + 1
    else:
        return answer - 1

model_rounded_before_noon_elevs = [myRound(x) for x in before_modelled_elevs ]
model_rounded_after_noon_elevs = [myRound(x) for x in after_modelled_elevs ]

measured_rounded_before_noon_elevs = [myRound(x) for x in before_noon_solar_elevs ]
measured_rounded_after_noon_elevs = [myRound(x) for x in after_noon_solar_elevs ]

modelled_before_noon_zen_range = np.arange(min(model_rounded_before_noon_elevs)
                                        ,max(model_rounded_before_noon_elevs)+1,2)
modelled_after_noon_zen_range = np.arange(min(model_rounded_after_noon_elevs)
                                        ,max(model_rounded_after_noon_elevs)+1,2)

measured_before_noon_zen_range = np.arange(min(measured_rounded_before_noon_elevs)
                                        ,max(measured_rounded_before_noon_elevs)+1,2)
measured_after_noon_zen_range = np.arange(min(measured_rounded_after_noon_elevs)
                                        ,max(measured_rounded_after_noon_elevs)+1,2)

before_noon_averaged_irrad_measured = []
after_noon_averaged_irrad_measured = []

before_noon_averaged_irrad_model = []
after_noon_averaged_irrad_model = []

for i in range(len(modelled_before_noon_zen_range)):
    indices = np.where(np.array(model_rounded_before_noon_elevs) == modelled_before_noon_zen_range[i])
    irrad =  [before_noon_irrad[x] for x in indices[0][:]]
    before_noon_averaged_irrad_model.append(np.mean(np.array(irrad)))
 
for j in range(len(modelled_after_noon_zen_range)):
    indices = np.where(np.array(model_rounded_after_noon_elevs) == modelled_after_noon_zen_range[j])
    irrad =  [after_noon_irrad[x] for x in indices[0][:]]
    after_noon_averaged_irrad_model.append(np.mean(np.array(irrad)))
        
for i in range(len(measured_before_noon_zen_range)):
    indices = np.where(np.array(measured_rounded_before_noon_elevs) == measured_before_noon_zen_range[i])
    irrad =  [before_noon_irrad[x] for x in indices[0][:]]
    before_noon_averaged_irrad_measured.append(np.mean(np.array(irrad)))
 
for i in range(len(measured_after_noon_zen_range)):
    indices = np.where(np.array(measured_rounded_after_noon_elevs) == measured_after_noon_zen_range[i])
    irrad =  [after_noon_irrad[x] for x in indices[0][:]]
    after_noon_averaged_irrad_measured.append(np.mean(np.array(irrad)))
        

# Plot original data and corrected data.
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
fig, axs = plt.subplots(2, 1,figsize=(8.27,11.69))

fig.text(0.01, 0.5, 'E$_{D\ VISIBLE}$ [W m$^{-2}$]', va='center', rotation='vertical',size=18,weight='bold')
fig.text(0.38, 0.06, 'Solar Elevation [°]', va='center', rotation='horizontal',size=18,weight='bold')

axs[0].plot(measured_before_noon_zen_range,before_noon_averaged_irrad_measured,linewidth=3,color='darkred',label='Dawn') 
axs[0].plot(measured_after_noon_zen_range,after_noon_averaged_irrad_measured,linewidth=3,color='seagreen',label='Dusk')   
axs[0].set_yscale('log')
axs[0].set_xticks([-20,-10,0,10,20])
axs[0].set_xticklabels(['','','','',''])
axs[0].grid(linestyle=':')
axs[0].set_xlim([-30,30])
axs[0].text(1.04, 0.5, 'ORIGINAL', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[0].transAxes, size=15, weight='bold')
axs[0].legend(bbox_to_anchor=(0.75, 1.2),prop=dict(size=18), ncol=2)
axs[0].text(0.05, 0.85, 'a', rotation='horizontal', transform=axs[0].transAxes,size=20, weight='bold')

axs[1].plot(modelled_before_noon_zen_range,before_noon_averaged_irrad_model,linewidth=3
            ,color='darkred',label='Dawn') 
axs[1].plot(modelled_after_noon_zen_range,after_noon_averaged_irrad_model,linewidth=3
            ,color='seagreen',label='Dusk')   
axs[1].set_yscale('log')
axs[1].set_xticks([-20,-10,0,10,20])
axs[1].grid(linestyle=':')
axs[1].set_xlim([-30,30])
axs[1].text(1.04, 0.5, 'ADJUSTED', horizontalalignment='center', rotation='vertical'
              , verticalalignment='center', transform=axs[1].transAxes, size=15, weight='bold')
axs[1].text(0.05, 0.85, 'b', rotation='horizontal', transform=axs[1].transAxes,size=20, weight='bold')

plt.subplots_adjust(wspace=0.02, hspace=0.05)
