from matplotlib.pyplot import *
from numpy import *

t=arange(1,3,0.02)
T=6*log(t)-7*exp(0.2*t)
#T=6*t
figure(1)
clf()
plot(t,T)
xlabel('Time (min)')
ylabel('Temperature (C)')
title('Chris Buckley-Plot')

savefig('myfig.png', dpi=300)

show()
print'Hello World! I just wrote my first Python program. Yayyyyyyyy'
print'Chris Buckley'
