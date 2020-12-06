#!/usr/bin/python
#
# Use matplotlib to plot the delay rate to screen and
# also create a pdf of the plot
#
# V1.0 S.Weston Dec 2020
#
import matplotlib.pyplot as plt
import numpy as np
import datetime
import glob

fit_geodetic_files=glob.glob("fit_geodetic_bl*.dat")

print fit_geodetic_files

# This works
for filename in fit_geodetic_files:
    print "Filename ",filename

# But first try one file

#filename="fit_geodetic_bl0102.dat"
#filename="fit_geodetic_bl1112.dat"
    prefix=filename.split(".")[0]
    print prefix

#data=np.loadtxt(filename, comments="!",delimiter=" ")
    data=np.loadtxt(filename, comments="!")

#print data
    data.size
    print "Array Size : ",data.size

    if data.size==0:
       continue

#exit()

    fig, ax = plt.subplots()
    ax.plot(data[:,0], data[:,1],'o',color='black',label="Delay")
    ax.plot(data[:,0], data[:,2],'o',color='red',label="D-model")
    ax.plot(data[:,0], data[:,3],'o',color='green',label="D-Resid")

    ax.set(ylabel='Multiband delay (nsec)',
       xlabel='UT (hours)',title=prefix)
    ax.grid()

    ax.legend(bbox_to_anchor=(1.05,1.05),loc='upper left',borderaxespad=0.)

    plt.tight_layout()

    plot_filename=prefix+".pdf"
    fig.savefig(plot_filename)
    plt.show()

