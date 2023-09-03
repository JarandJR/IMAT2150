import numpy as np

sec = lambda x: 1.0/np.cos(x)
f_orig = lambda x: (1 - sec(x))/(np.tan(x)**2)#<------- Utrykk fra oppgaveteksten her
f_ny = lambda x: -1/(1 + sec(x))#<------------Omformet uttrykk her

x = [10**(-i) for i in range(1,15)]

print("{:<10}{:<30}{:<30}{:<20}".format("x", "Original", "Omskrevet", "Korrekte desimalplasser"))
print("------------------------------------")
for xi in x:
   fx_orig = f_orig(xi)
   fx_ny = f_ny(xi)
   korrekte = -np.floor(np.log10(np.abs(fx_orig-fx_ny)))-1
   print("{:<10}{:<30}{:<30}{:<20}".format(xi, fx_orig, fx_ny,korrekte))