# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename( columns = {'Total':'Total_Medals'}, inplace = True )
data.head(10)

# Summer or Winter
c1 = data['Total_Summer'] == data['Total_Winter']
c2 = data['Total_Summer'] > data['Total_Winter']
data['Better_Event'] = np.where( c1, 'Both', (np.where(c2, 'Summer', 'Winter')) )
better_event = data['Better_Event'][data['Better_Event'].value_counts().max()]
print(better_event)

# Top 10
def top_ten(df, col):
    country_list = []
    a = df.nlargest(10, col)
    country_list = list(a['Country_Name'])
    return country_list

top_countries = pd.DataFrame( data, columns = ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] )[:-1]
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print( top_10_summer, "\n", top_10_winter, "\n", top_10, "\n", common )

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

p1 = plt.figure().add_axes([0,0,1,1])
p1.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.title('Top 10 Countries for Summer Olympics')

p2 = plt.figure().add_axes([0,0,1,1])
p2.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.title('Top 10 Countries for Winter Olympics')

p3 = plt.figure().add_axes([0,0,1,1])
p3.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.title('Top 10 Countries for Olympics Overall')

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] % summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = list(summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio])[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] % winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = list(winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio])[0]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = list(top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio])[0]

# Best in the world 
data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = data_1['Total_Points'].max()
best_country = list(data_1['Country_Name'][data_1['Total_Points']==most_points])[0]

# Plotting the best
best = data[ data['Country_Name'] == best_country ]
best = pd.DataFrame( best, columns = ['Gold_Total','Silver_Total','Bronze_Total'] )
best.plot.bar( stacked=True )
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


