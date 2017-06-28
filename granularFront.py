import numpy as np

# Confinement height and length
H = 10;
L = 100;

# Lattice parameter
a = 1.;

# frition coefficient
mu_c = 0.5;

# Homogeneously sedimented initial state
s = H/2. * np.ones(L);

# Piston/meniscus progression speed
dt = 1.
U = a/dt;
dP = U*dt;

# Initial time:
t=0;
# Integration time:
tmax=2;
# Piston initial position :
P = np.zeros(tmax);

for j in range(0,tmax):
  np.savetxt("s"+str(t)+".dat",s);
# Bulldozing
# Granular material to be redistributed
  Ds = s[P[j]]
# Available location to accept the granular material to be redistributed
  availability = np.cumsum(H-s);
# Redistribute the bulldozed granular material
  s[availability < Ds] = H; # Full
  s[availability > Ds][0] = H - (availability[availability > Ds][0] - Ds); # Remaining 
# Avalanching 
  slope = (s[1:] - s[:-1])/a; # local slopes
  avalanche = np.abs(slope) > mu_c; # avalanche is triggered above some slope thershold
# slope(i)  >  mu_C => s(i)+1 and s(i+1)-1;  slope(i)  < -mu_C => s(i)-1 and s(i+1)+1;
  ds = avalanche * np.sign(slope); 
  ds[1:] = ds[1:] + ds[:-1] * (-1);
# Time update
  t = t +dt;
# Piston position update :
  P[j] = P[j-1] + dP
