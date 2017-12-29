
# coding: utf-8

# In[1]:

#load necessary libraries


# In[99]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')


# In[133]:

#set directory path as variable "data" and import to a pandas DataFrame
data = open('C:\\Users\\SCOTT\\Desktop\\Data Mining\\ExcelFormattedGISTEMPDataCSV.csv')
df = pd.read_csv(data).replace('****', np.NaN)
dmin = [0,0,0,0]
dmax = [0,0,0,0]
dmin[0] = df.loc[:,'DJF'].dropna().min(axis=0)
dmin[1] = df.loc[:,'MAM'].dropna().min(axis=0)
dmin[2] = df.loc[:,'JJA'].dropna().min(axis=0)
dmin[3] = df.loc[:,'SON'].dropna().min(axis=0)
dmax[0] = df.loc[:,'DJF'].dropna().max(axis=0)
dmax[1] = df.loc[:,'MAM'].dropna().max(axis=0)
dmax[2] = df.loc[:,'JJA'].dropna().max(axis=0)
dmax[3] = df.loc[:,'SON'].dropna().max(axis=0)
print(dmin)
print(dmax)


# In[28]:

#Prep the figure space and graph
#Prep graph colors for each individual month
RGB_COLORS = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148)]
#matlibplot only accepts RGB colors with values from [0,1] so convert current RGB colors
for rgb in range(len(RGB_COLORS)):
    r,g,b = RGB_COLORS[rgb]
    RGB_COLORS[rgb] = (r/255. , g/255. , b/255.)
    

RGB_COLORS


# In[29]:

#Remove all "Chart Junk"
#Remove plot frame lines
ax = plt.subplot(111)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

#Axis ticks only show up on the bottom left of the plot
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

#limit the range of the plot to only where the data is
plt.ylim(-80,100)
plt.xlim(1879,2016)

#rotate x-axis labels
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

#set axis ticks
plt.yticks(range(-100,120,20))
plt.xticks(range(1880,2030,15))

#rotate x-axis labels
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

#tick lines across the plot
for y in range(-100, 120, 10):
    plt.plot(range(1880,2020), [y]*len(range(1880,2020)), '--',lw=0.5, color = 'black', alpha=0.3)
    
#remove tick marks on the axis
plt.tick_params(axis='both', which='both', bottom ='off', top='off', labelbottom='on', left = 'off', right='off', labelleft='on')


# In[164]:

#Plot the Data
#plt.figure(figsize=(14,14))

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
tri_month_average = ['DJF','MAM','JJA','SON']
seasons = ['Winter','Spring','Summer','Fall']
tri_month_year = []
for year in range(1880, 2020, 20):
    tri_month_year.append(year)
    
df2 = df.set_index("Year")
color = ['red', 'green','blue','orange']    
df3 = pd.DataFrame(tri_month_year)
df3 = df3.rename(columns = {0:'Year'})
DJF = [np.NaN,-24,-23,11,3,40,44]
MAM = [-19,-5,-18,11,-20,32,53]
JJA = [-19,-7,-29,6,-1,24,43]
SON = [-16,0,-25,11,0,23,35]
df3['DJF'] = DJF
df3['MAM'] = MAM
df3['JJA'] = JJA
df3['SON'] = SON


#Create first subplot for graph 1 subplot(3 rows, 1 column, 1 position)
f, axs = plt.subplots(3,1,figsize=(15,15))
ax1 = plt.subplot(311)
#plot data
for rank, month in enumerate(months):
    ax1.plot(df.Year.values, df[month].values, lw = 1.5, label = month)
#hide the plot ticklabels since they will be displayed at the bottom
plt.setp(ax1.get_xticklabels(),visible = False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.set_title('Monthly Trend of Temperature Deviation')
ax1.legend(loc = 'right')
plt.tick_params(axis='both', which='both', bottom ='off', top='off', labelbottom='on', left = 'off', right='off', labelleft='on')
for y in range(-80, 120, 20):
    plt.plot(range(1880,2020), [y]*len(range(1880,2020)), '--',lw=0.5, color = 'black', alpha=0.3)
plt.plot(range(1880,2020), [0]*len(range(1880,2020)),'--', lw=0.5, color = 'black')

ax2 = plt.subplot(312, sharex=ax1)
for rank, quarter in enumerate(tri_month_average):
    ax2.plot(df3.Year.values, df3[quarter].values, 'o', color = color[rank], label = seasons[rank])
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_title('Seasonal Trend of Temperature Deviation')
ax2.legend(loc = 'right')
plt.tick_params(axis='both', which='both', bottom ='off', top='off', labelbottom='on', left = 'off', right='off', labelleft='on')
for y in range(-50, 100, 25):
    plt.plot(range(1880,2020), [y]*len(range(1880,2020)), '--',lw=0.5, color = 'black', alpha=0.3)
plt.plot(range(1880,2020), [0]*len(range(1880,2020)),'--', lw=0.5, color = 'black')

ax3 = plt.subplot(313, sharex=ax1)   
ax3.plot(df.Year.values, df['J-D'].values, label = 'Yearly Average')
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.set_title('Yearly Average of Temperature Deviation')
ax3.legend(loc = 'right')
plt.tick_params(axis='both', which='both', bottom ='off', top='off', labelbottom='on', left = 'off', right='off', labelleft='on')
for y in range(-50, 100, 25):
    plt.plot(range(1880,2020), [y]*len(range(1880,2020)),'--',lw=0.5, color = 'black', alpha=0.3)
plt.plot(range(1880,2020), [0]*len(range(1880,2020)),'--', lw=0.5, color = 'black')


#plt.plot(tri_month_year, data, 'o', label = [['Winter'],['Spring']])
ax.legend(bbox_to_anchor = (0.94,0.43))

ax.text(1995,93,"Trend of Global Temperature Deviation - 1880 to Present Day", fontsize = 17, ha = 'right')

plt.show()
    



# In[83]:




# In[165]:

plt.savefig("Global_Temp_Trend.png", bbox_inches="tight")


# In[ ]:



