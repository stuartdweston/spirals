#!/usr/bin/python
#
# Use matplotlib to plot the atmos file to screen and
# also create a pdf of the plot
#
# V1.0 S.Weston Dec 2020

import matplotlib.pyplot as plt
import numpy as np
import datetime
import glob

def legend_without_duplicate_labels(ax):
    handles, labels = ax.get_legend_handles_labels()
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    ax.legend(*zip(*unique))

# Define 7 station colour index for matplotlib

colour=np.array(['b','g','r','c','m','y','k'])

# This works
filename="ATMOS.FITS"

print "Filename    : ",filename


data=np.loadtxt(filename, comments="!",skiprows=1)

#print data
data.size
#print "Array Size  : ",data.size
data.shape
#print "Array Shape : ",data.shape

rows=data.shape[0]
#print "Rows        : ",rows

# Get ready to start plotting

fig, ax = plt.subplots()

#calcultae decimal hrs
i=0
while i < rows:
   antenna=int(data[i][0])
   hh=float(data[i][2])
   mm=float(data[i][3])
   ss=float(data[i][4])
   hh_dec=hh+((mm+(ss/60))/60)
   print "Decimal Hrs  : ",hh_dec
   delay=float(data[i][5])
   print "zenith delay [cm] : ",delay
   legend_txt="Antenna : "+str(int(data[i][0]))
   print legend_txt
   ax.plot(hh_dec,delay,'o',color=colour[antenna],label=legend_txt)
   i += 1

ax.set(ylabel='zenith delay (cm)',
       xlabel='UT (hours)',title=filename)

ax.grid()

ax.legend(bbox_to_anchor=(1.05,1.05),loc='upper right',borderaxespad=0.)

plt.tight_layout()

legend_without_duplicate_labels(ax)

plot_filename="atmos.pdf"
fig.savefig(plot_filename)
plt.show()
