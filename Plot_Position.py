# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:31:54 2015

@author: BEC
"""

from pylab import *
from time import strftime
#x = genfromtxt(strftime('Z:\%Y\%b%Y\%d%b%Y\Pictures\VerdiPosition\positions_not_locked.txt'))
#y = genfromtxt(strftime('Z:\%Y\%b%Y\%d%b%Y\Pictures\VerdiPosition\positions_locked6.txt'))
y = genfromtxt(strftime('Z:\%Y\%b%Y\%d%b%Y\Pictures\VerdiPosition\positions_aft4.txt'))

figure()

subplot(1,2,1)
#plot((x[:,0]-x[0,0])/60.,x[:,1],'ob-')
plot((y[:,0]-y[0,0])/60.,y[:,1],'sr-')
xlabel('Time (mn)')
ylabel('Y Position (Pixels)')

subplot(1,2,2)
#plot((x[:,0]-x[0,0])/60,x[:,2],'ob-')
plot((y[:,0]-y[0,0])/60.,y[:,2],'sr-')
xlabel('Time (mn)')
ylabel('X Position (Pixels)')
legend(('Not Locked','Locked'))
show()
