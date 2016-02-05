import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

station_name = '09380000'

url1 = 'http://waterservices.usgs.gov/nwis/iv/?'
url2 = 'format=rdb'
url3 = 'sites=' + station_name 
url4 = 'startDT=2010-01-01'
url5 = 'endDT=2016-01-01'
url6 = 'parameterCd=00060,00065'

url = url1 + url2 + '&' + url3 + '&' + url4 + '&' + url5 + '&' + url6

print url

data = pd.read_csv(url, comment = '#', sep = '\t', header = 1)

new_column_names = ['Agency','Station','OldDateTime','TimeZone','Discharge','Status','Stage','StageStatus']
data.columns = new_column_names

new_station_name = "0" + str(data['Station'].unique()[0])
data['Station'] = new_station_name

data['DateTime'] = pd.to_datetime(data['OldDateTime'])

data.plot(x = 'DateTime', y = 'Discharge', title = 'Station ' + new_station_name)
plt.ylabel('Discharge (ft$^3$/s)')

plt.savefig('hydrograph_' + new_station_name + '.pdf')
