import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

df: pd.DataFrame = pd.read_csv("../data/Cleaned_Data_Monthly.csv")
Monthly_Smoothed_60s = (df[(df['Year'] > 1959) & (df['Year'] < 1970)][['Region', 'Year', 'Month', 'Sea_Level_Monthly_Smoothed']])
Monthly_Smoothed_70s = (df[(df['Year'] > 1969) & (df['Year'] < 1980)][['Region', 'Year', 'Month', 'Sea_Level_Monthly_Smoothed']])
Monthly_Smoothed_80s = (df[(df['Year'] > 1979) & (df['Year'] < 1990)][['Region', 'Year', 'Month', 'Sea_Level_Monthly_Smoothed']])
Monthly_Smoothed_90s = (df[(df['Year'] > 1989) & (df['Year'] < 2000)][['Region', 'Year', 'Month', 'Sea_Level_Monthly_Smoothed']])
Monthly_Smoothed_00s = (df[(df['Year'] > 1999) & (df['Year'] < 2010)][['Region', 'Year', 'Month', 'Sea_Level_Monthly_Smoothed']])
Monthly_Smoothed_10s = (df[(df['Year'] > 2009) & (df['Year'] < 2020)][['Region', 'Year', 'Month', 'Sea_Level_Monthly_Smoothed']])
# Separated sea stations
US_Sea_Stations = ['ALA', 'CWP', 'SWP', 'SPL', 'SEA', 'CEA']  # removed MID because no data
Canada_Sea_Stations = ['NWP', 'NPL', 'NEF', 'NEA']  # removed CAR because no data

# Plotting Smoothed Sea Level Data for US 1960's
US_Smoothed_60s = Monthly_Smoothed_60s[Monthly_Smoothed_60s['Region'].isin(US_Sea_Stations)]
US_Smoothed_60s['Date'] = (US_Smoothed_60s['Year'].astype(str) + '-' + US_Smoothed_60s['Month'].astype(str))
#US_Smoothed_60s = US_Smoothed_60s.set_index('Date')
fig, ax = plt.subplots(figsize=(10, 8))
for key, grp in US_Smoothed_60s.groupby(['Region']):
    ax = grp.plot(ax=ax, kind='line', x='Date', y='Sea_Level_Monthly_Smoothed', label=key)
plt.legend(loc='best')
plt.grid()
plt.xlabel('Years')
plt.ylabel('Sea Level Monthly')
plt.title('US Sea Level Stations from 1960-1969')
plt.show()

# Plotting Smoothed Sea Level Data for Canada 1960's
Canada_Smoothed_60s = Monthly_Smoothed_60s[Monthly_Smoothed_60s['Region'].isin(Canada_Sea_Stations)]
Canada_Smoothed_60s['Date'] = (Canada_Smoothed_60s['Year'].astype(str) + '-' + Canada_Smoothed_60s['Month'].astype(str))
fig, ax = plt.subplots(figsize=(10, 8))
for key, grp in Canada_Smoothed_60s.groupby(['Region']):
    ax = grp.plot(ax=ax, kind='line', x='Date', y='Sea_Level_Monthly_Smoothed', label=key)
plt.legend(loc='best')
plt.grid()
plt.xlabel('Years')
plt.ylabel('Sea Level Monthly')
plt.title('Canada Sea Level Stations from 1960-1969')
plt.show()

US_Smoothed_70s = Monthly_Smoothed_70s[Monthly_Smoothed_70s['Region'].isin(US_Sea_Stations)]
US_Smoothed_70s['Date'] = (US_Smoothed_70s['Year'].astype(str) + '-' + US_Smoothed_70s['Month'].astype(str))

Canada_Smoothed_70s = Monthly_Smoothed_70s[Monthly_Smoothed_70s['Region'].isin(Canada_Sea_Stations)]
Canada_Smoothed_70s['Date'] = (Canada_Smoothed_70s['Year'].astype(str) + '-' + Canada_Smoothed_70s['Month'].astype(str))

US_Smoothed_80s = Monthly_Smoothed_80s[Monthly_Smoothed_80s['Region'].isin(US_Sea_Stations)]
US_Smoothed_80s['Date'] = (US_Smoothed_80s['Year'].astype(str) + '-' + US_Smoothed_80s['Month'].astype(str))

Canada_Smoothed_80s = Monthly_Smoothed_80s[Monthly_Smoothed_80s['Region'].isin(Canada_Sea_Stations)]
Canada_Smoothed_80s['Date'] = (Canada_Smoothed_80s['Year'].astype(str) + '-' + Canada_Smoothed_80s['Month'].astype(str))

US_Smoothed_90s = Monthly_Smoothed_90s[Monthly_Smoothed_90s['Region'].isin(US_Sea_Stations)]
US_Smoothed_90s['Date'] = (US_Smoothed_90s['Year'].astype(str) + '-' + US_Smoothed_90s['Month'].astype(str))

Canada_Smoothed_90s = Monthly_Smoothed_90s[Monthly_Smoothed_90s['Region'].isin(Canada_Sea_Stations)]
Canada_Smoothed_90s['Date'] = (Canada_Smoothed_90s['Year'].astype(str) + '-' + Canada_Smoothed_90s['Month'].astype(str))

US_Smoothed_00s = Monthly_Smoothed_00s[Monthly_Smoothed_00s['Region'].isin(US_Sea_Stations)]
US_Smoothed_00s['Date'] = (US_Smoothed_00s['Year'].astype(str) + '-' + US_Smoothed_00s['Month'].astype(str))

Canada_Smoothed_00s = Monthly_Smoothed_00s[Monthly_Smoothed_00s['Region'].isin(Canada_Sea_Stations)]
Canada_Smoothed_00s['Date'] = (Canada_Smoothed_00s['Year'].astype(str) + '-' + Canada_Smoothed_00s['Month'].astype(str))

US_Smoothed_10s = Monthly_Smoothed_10s[Monthly_Smoothed_10s['Region'].isin(US_Sea_Stations)]
US_Smoothed_10s['Date'] = (US_Smoothed_10s['Year'].astype(str) + '-' + US_Smoothed_10s['Month'].astype(str))

Canada_Smoothed_10s = Monthly_Smoothed_10s[Monthly_Smoothed_10s['Region'].isin(Canada_Sea_Stations)]
Canada_Smoothed_10s['Date'] = (Canada_Smoothed_10s['Year'].astype(str) + '-' + Canada_Smoothed_10s['Month'].astype(str))

#fig = plt.figure(figsize=(16, 8))
#plt.subplot(221)
#plt.scatter(Monthly_Smoothed_70s['Year'], Monthly_Smoothed_70s['Sea_Level_Monthly_Smoothed'])
#plt.subplot(222)
#plt.scatter(Monthly_Smoothed_80s['Year'], Monthly_Smoothed_80s['Sea_Level_Monthly_Smoothed'])
#plt.subplot(223)
#plt.scatter(Monthly_Smoothed_90s['Year'], Monthly_Smoothed_90s['Sea_Level_Monthly_Smoothed'])
#plt.show()
