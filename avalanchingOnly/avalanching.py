import numpy as np

# Confinement height and length
H = 10;
L = 100;

# Lattice parameter
a = 1.;

# frition coefficient
mu_c = 0.5;

# Initial state 
# Fully filled...
s = H * np.ones(L);
# ... with a hole in the middle:
s[int(L/3.):int(2.*L/3.)] = 0;
# avalanching condition set to 1
avalanching = 1;

# Stabilization loop:
i = 0;
while avalanching > 0:
  i = i+1;
# Avalanching 
  slope = (s[1:] - s[:-1])/a; # local slopes
  avalanche = np.abs(slope) > 1./mu_c; # avalanche is triggered above some slope thershold
  avalanching = sum(avalanche);
# slope(i)  >  mu_C => s(i)+1 and s(i+1)-1;  
# slope(i)  < -mu_C => s(i)-1 and s(i+1)+1;
  ds = avalanche * np.sign(slope); 
  ds[1:] = ds[1:] + ds[:-1] * (-1);
# final state after local avalanching.
  s[:-1] = s[:-1] + ds;
