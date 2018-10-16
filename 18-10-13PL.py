import pandas as pd
import matplotlib.pyplot as plt
import re
from matplotlib.ticker import MultipleLocator
import numpy as np

al_data = pd.read_table('al-multi.txt', sep='[ |\t]', encoding='utf=8', engine='python', skiprows=[0, 1]+list(range(3, 24)))
g_data = pd.read_table('g-multi.txt', sep='[ |\t]', encoding='utf=8', engine='python', skiprows=[0, 1]+list(range(3, 24)))


def new_columns_data_al(orginal_data):     #改变data的columns，使label变成功率
    new_columns = ['Labels']
    for column in orginal_data.columns[1:]:
        regex = re.compile(r'(\d)+')
        match = regex.search(column)
        new_columns.append(int(match.group())*17.5)
    orginal_data.columns = new_columns
    return orginal_data

def new_columns_data_g(orginal_data):     #改变data的columns，使label变成功率
    new_columns = ['Labels']
    for column in orginal_data.columns[1:]:
        regex = re.compile(r'(\d)+')
        match = regex.search(column)
        new_columns.append(int(match.group())*8.5)
    orginal_data.columns = new_columns
    return orginal_data



new_al_data = new_columns_data_al(al_data)
new_g_data = new_columns_data_g(g_data)

print(new_g_data.columns)

fig = plt.figure(1, figsize=(18, 14), dpi=300)
fig.suptitle('PL spectra on glass and '+ r'$Al_2O_3$', size=21)

ax1 = fig.add_subplot(221)
ax1.set_title(r'$Al_2O_3$',loc='left', size=18, color='coral')
ax1.set_xlabel('Wavelength(nm)', size=16)
ax1.set_ylabel('PL Intensity(a.u.)', size=16)
ax1.set_yticklabels([])
plt.tick_params(axis='both', which='both',direction='in')

color=['red','lime','peru','blue','brown','grey','violet','black','forestgreen']
ax1.plot(new_al_data['Labels'], new_al_data[1750.0],color=color[0])
ax1.plot(new_al_data['Labels'], new_al_data[1400.0],color=color[1])
ax1.plot(new_al_data['Labels'], new_al_data[1102.5],color=color[2])
ax1.plot(new_al_data['Labels'], new_al_data[875.0],color=color[3])
ax1.plot(new_al_data['Labels'], new_al_data[700.0],color=color[4])
ax1.plot(new_al_data['Labels'], new_al_data[542.5],color=color[5])
ax1.plot(new_al_data['Labels'], new_al_data[350.0],color=color[6])
ax1.plot(new_al_data['Labels'], new_al_data[175.0],color=color[7])
ax1.plot(new_al_data['Labels'], new_al_data[87.5],color=color[8])
xminorLocator = MultipleLocator(5)
ax1.xaxis.set_minor_locator(xminorLocator)
plt.legend(frameon=False)

ax2 = fig.add_subplot(222)
ax2.set_title('Glass',loc='left', size=18, color='steelblue')
ax2.set_xlabel('Wavelength(nm)', size=16)
ax2.set_ylabel('PL Intensity(a.u.)', size=16)
ax2.set_yticklabels([])
plt.tick_params(axis='both', which='both',direction='in')

ax2.plot(new_g_data['Labels'], new_g_data[850.0],color=color[0])
ax2.plot(new_g_data['Labels'], new_g_data[680.0],color=color[1])
ax2.plot(new_g_data['Labels'], new_g_data[535.5],color=color[2])
ax2.plot(new_g_data['Labels'], new_g_data[425.0],color=color[3])
ax2.plot(new_g_data['Labels'], new_g_data[340.0],color=color[4])
ax2.plot(new_g_data['Labels'], new_g_data[170.0],color=color[5])
ax2.plot(new_g_data['Labels'], new_g_data[85.0],color=color[6])
ax2.plot(new_g_data['Labels'], new_g_data[42.5],color=color[7])
xminorLocator = MultipleLocator(5)
ax2.xaxis.set_minor_locator(xminorLocator)
plt.legend(frameon=False)



al_top = new_al_data.max()[1:].sort_index()
g_top = new_g_data.max()[1:].sort_index()
print('the al top is:')
print(al_top)
print('the g top is')
print(g_top)



ax3=fig.add_subplot(223)
ax3.set_xlabel('Excition Fluence '+r'$\mu W/cm^2$', size=16)
ax3.set_ylabel('PL Intensity(a.u.)', size=16)
plt.tick_params(axis='both', which='both',direction='in')
ax3.scatter(al_top.index, al_top.values,color='coral', label=r'$Al_2O_3$')
ax3.scatter(g_top.index, g_top.values, color='steelblue',label='Glass')
al_x1 = np.linspace(87.5,425.8,100)
al_y1 = 0.06657*al_x1 + 17.1
al_x2 = np.linspace(425.8,1750,500)
al_y2 = 0.28796*al_x2 - 77.02191
ax3.plot(al_x1, al_y1, color='coral')
ax3.plot(al_x2, al_y2, color='coral')
g_x1 = np.linspace(42.5,298.1,100)
g_y1 = 0.18495*g_x1 + 9.5
g_x2 = np.linspace(298.1,850,500)
g_y2 = 0.86335*g_x2 - 192.4
ax3.plot(g_x1, g_y1, color='steelblue')
ax3.plot(g_x2, g_y2, color='steelblue')
ax3.scatter(425.8, 0.06657*425.8 + 17.1, color='coral',marker = '^', s = 100)
ax3.scatter(298.1, 0.18495*298.1 + 9.5, color='steelblue', marker ='^', s=100)
xminorLocator = MultipleLocator(50)
ax3.xaxis.set_minor_locator(xminorLocator)
plt.legend(frameon=False)

#plt.text(0,150,r'$298.1\ \mu W/cm^2$', color='steelblue',fontsize=13)    #添加空格也需要转义
#plt.text(1000,100,r'$425.8\ \mu W/cm^2$', color='coral',fontsize=13)

plt.annotate(r'$425.8\ \mu W/cm^2$',xy=(425.8,45.446), xytext = (+30, -15), color='coral', textcoords='offset points', fontsize=12, arrowprops = dict(lw=3,alpha=0.4,color='black',arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.annotate(r'$298.1\ \mu W/cm^2$',xy=(298.1,64.633), xytext = (-80, +30), color='steelblue', textcoords='offset points', fontsize=12, arrowprops = dict(lw=3, alpha=0.4,color='black',arrowstyle='->',connectionstyle='arc3,rad=.2'))


plt.savefig('18-10-13.png')
