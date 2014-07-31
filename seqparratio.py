c = [0.8916583583 ,0.9364599092 ,0.9418026692 ,0.9660107754 ,0.9735619037 
,0.9752730086 ,0.9795233774 ,0.9736945491 ,0.983412122 ,0.8847568897 
,0.937049294 ,0.9556460673 ,0.9521823306 ,0.9457192893 ,0.9755469101 
,0.9781225838 ,0.9804915898 ,0.7425709229 ,0.885471973 ,0.8549843111 
,0.9540545879 ,0.9638071451 ,0.9549170066 ,0.9591822503 ,0.9771572723 
,0.9802537765 ,0.9703582279 ,0.9436619718 ,0.9485614647 ,0.8532666905 
,0.9380387931 ,0.9383123181 ,0.9020750758 ,0.8996929376 ,0.9635932203 
,0.9663973089 ,0.9712227524 ,0.9697056889 ,0.9709112973 ]
import numpy as np
import matplotlib.pyplot as plt
from pylab import var,mean
cc = range(len(c))
plt.figure()
v = var(c)
plt.errorbar(cc, c, xerr=v,label=str(var(c)))
plt.plot(cc,[mean(c)]*len(c),'--',label=str(mean(c)))
plt.plot(cc,[0]*len(c),'.w')
plt.title("Sequential Parallel Ratio")
plt.legend(loc='lower center')
plt.show()
