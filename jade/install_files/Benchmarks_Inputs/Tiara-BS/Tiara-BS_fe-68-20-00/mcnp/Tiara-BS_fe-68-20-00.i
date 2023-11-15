TIARA Fe, 68 MeV, 20 cm shield, B. Kos (bor.kos@ijs.si), 2018
c TIARA Fe, 68 MeV, 20 cm shield
c Bor Kos, JSI, July 2018
c Bonner sphere
100 6  -2.31      -100:-101:-102 :-103: -104: -105 :(-106 110):
                   (-110 -109 -106.3 104.1 105.1 111):
                   (-111  108 -106.3 104.1 105.1 112):
                   (-112  107 -106.3 104.1 105.1) imp:n=1                      $ Concrete structure
101 1  -7.87      -150 151 imp:n=1                                             $ Beam dump
102 1  -7.08      -200 201 202 2 imp:n=1                                       $ Iron filler (density is 10 % lower than ordinary iron - original documentation assumes a mixutre of iron sand and balls)
103 1  -7.87      -201 2 imp:n=1                                               $ Rotary shutter - iron
104 2  -0.928     -202 2  imp:n=1                                              $ Rotary shutter - polyethylene
105 3  -2.6989    -210 : -211 : -212 imp:n=1                                   $ Trolly (aluminium - assumed, not in benchmark documetation)
129 5  -0.001205  -282 imp:n=1                                                 $ bare Bonner sphere - polyethlyene moderator
130 5  -0.001205  -283 282 imp:n=1                                             $ 15 mm Bonner sphere - polyethlyene moderator
131 5  -0.001205  -284 283 282 imp:n=1                                         $ 30 mm Bonner sphere - polyethlyene moderator 
132 5  -0.001205  -285 284 283 282 imp:n=1                                     $ 50 mm Bonner sphere - polyethlyene moderator
133 5  -0.001205  -286 285 284 283 282 imp:n=1                                 $ 90 mm Bonner sphere - polyethlyene moderator 
134 3  -2.6989    -287 : -288 : -289 : -290 : -291 imp:n=1                     $ 90 mm Bonner sphere - detector stand      
110 1  -7.87      -1000 imp:n=1                                                $ Iron test shield 
600 0             -600 #100 #101 #102 #103 #104 -2.2 imp:n=1                   $ void
700 5  -0.001205 -600 1000 #100 #105 #129 #130 #131 #132 #133 #134 2.2 imp:n=1 $ air                                                                                                                                                                      
601 0              600 imp:n=0                                                 $ Outer space

c -----------------------------------------------------------------------------
c         SURFACES                                                         
c -----------------------------------------------------------------------------
c Source
1   px    0.0                                                                   $ Source plane
c Beam line
2   rcc 0.0 0.0 0.0 396.0 0.0 0.0 5.45  
c Concret stucture
100 box -124.0  250.0 -109.0 0.0 0.0 -200.0 0.0 -500.0 0.0 300.0 0.0 0.0
101 box  176.0  250.0 -119.0 0.0 -500.0 0.0 60.0 0.0 0.0 0.0 0.0 -190.0
102 box  716.0 -250.0 -309.0 0.0 0.0 232.65 0.0 500.0 0.0 -480.0 0.0 0.0
103 box  236.0  250.0  -20.0 0.0 -500.0 0.0 160.0 0.0 0.0 0.0 0.0 -56.35
104 box -124.0 -250.0 -119.0 0.0 190.0 0.0 0.0 0.0 399.065125 640.0 0.0 0.0
105 box -124.0  250.0 -119.0 0.0 -190.0 0.0 0.0 0.0 399.065125 640.0 0.0 0.0
106 box  516.0 -60.0    60.0 0.0 120.0 0.0 0.0 0.0 220.065122 -640.0 0.0 0.0
107 p    16020.908203 0.0 16038.62915 2.5053e+6
108 pz   146.558
109 p   -5443.936157 0.0 -5563.590088 -1.5211e+6
110 px   176
111 px   129.637
112 px   9.65524
c Beam dump
150 box 236.0 -20.0 -119.0 -60.0 0.0 0.0 0.0 40.0 0.0 0.0 0.0 99.0
151 box 206.0 -20.0 -89.0 0.0 40.0 0.0 -30.0 0.0 0.0 0.0 0.0 50.0
c Iron filler (iron balls and iron sand)
200 box 176.0 60.0 60.0 0.0 0.0 -80.0 0.0 -120.0 0.0 220.0 0.0 0.0
c Rotary shutter - iron
201 rcc 183 0 9.08 100.0 0.0 0.0 21.8
c Rotary shutter - polyethylene
202 rcc 283 0 9.08 50.0 0.0 0.0 21.8
c Trolly
210 box 398.5 -60.0 -60.0 0.0 0.0 -10.0 0.0 120.0 0.0 120.0 0.0 0.0
211 rcc 409.718 -60.0 -70.0 0.0 120.0 0.0 6.35
212 rcc 503.650752 -60.0 -70.0 0.0 120.0 0.0 6.35
c Bonner spheres with 3-He counter - bare to 90 mm polyethylene
282 s   423.5908 0.0 0.0 2.5908                   $ 3-He counter
283 s   425.0908 0.0 0.0 4.0908                   $ Polyethylene sphere 15 mm thick
284 s   426.55 0.0 0.0 5.55                     $ Polyethylene sphere 30 mm thick
285 s   428.55 0.0 0.0 7.55                     $ Polyethylene sphere 50 mm thick
286 s   432.55 0.0 0.0 11.55                    $ Polyethylene sphere 90 mm thick
287 box 421.0 10.0 -11.55 0.0 0.0 -1.000 0.0 -20.0 0.0 40.0 0.0 0.0 $ Detector support table - aluminium assumed
288 rcc 422.0  9.0 -12.55 0.0 0.0 -47.45 1.0
289 rcc 422.0 -9.0 -12.55 0.0 0.0 -47.45 1.0
290 rcc 460.0  9.0 -12.55 0.0 0.0 -47.45 1.0
291 rcc 460.0 -9.0 -12.55 0.0 0.0 -47.45 1.0
c Outside world
600 box -130 -252 -315 850 0.0 0.0 0.0 504.0 0.0 0.0 0.0 600.0
c Additional iron colimator
c 800
c Shield
1000 box 401.0 -60 -60 20.0 0.0 0.0 0.0 120.0 0.0 0.0 0.0 120.0

c -----------------------------------------------------------------------------
c         MATERIALS
c -----------------------------------------------------------------------------
c Iron shield - atom density, Density ( g /cm3 )= 7.87. Naturan iron from benchmark documetation - Table 1.2 JAERI-Data/Code 96-029
m1   26054. 4.9605E-03
     26056. 7.7869E-02
     26057. 1.7983E-03
     26058. 2.3933E-04
c Polyethylene - atom density, Density ( g /cm3 )= 0.928, Reference: http://physics.nist.gov/PhysRefData/XrayMassCoef/tab2.html    
m2    1001. 0.079855
      6000. 0.039929
c Aluminum - atom density, Density ( g /cm3 )= 2.6989
m3   13027. 0.060238
c Liquid scintillator - atom density, Density ( g /cm3 )= 0.874  "https://www.crystals.saint-gobain.com/sites/imdf.crystals.com/files/documents/sgc-bc501-501a-519-data-sheet_69711.pdf"
m4    1001. 0.0482
      6000. 0.0398
c Dry Air - atom density, Density ( g /cm3 )= 0.001205
m5    6000. 7.4919E-09
      7014. 3.8987E-05
      7015. 1.4243E-07
      8016. 1.0487E-05
      8017. 3.9948E-09
     18036. 7.8407E-10
     18038. 1.4726E-10
     18040. 2.3208E-07
c Concrete from benchmark documentation (per nuclide definition) - atom desnity, Density ( g /cm3 )= 2.31   
m6    1001. 1.49783E-02
      1002. 1.72270E-06 
      8016. 4.18641E-02
      8017. 1.59471E-05
     11023. 1.23000E-03
     12024. 4.89740E-04
     12025. 6.19982E-05
     12026. 6.82614E-05
     13027. 3.12000E-03
     14028. 1.02368E-02
     14029. 5.20043E-04
     14030. 3.43204E-04
     19039. 3.54381E-04
     19040. 4.44605E-08
     19041. 2.55745E-05
     20040. 4.16846E-03
     20042. 2.78219E-05
     20043. 5.80511E-06
     20044. 8.96994E-05
     20046. 1.72004E-07
     20048. 8.04130E-06
     26054. 8.24154E-05
     26056. 1.29373E-03
     26057. 2.98785E-05
     26058. 3.97622E-06
c -----------------------------------------------------------------------------
c         SOURCE
c -----------------------------------------------------------------------------
c --- Point isotropic neutron source collimated into an -x cone. 
c Particles are confined to a (+x axis) cone whose half-angle
c is acos(0.99990531) = 0.7788 degrees about the x-axis. 
c Angles are with respect to the vector specified by VEC
c
sdef cell=600 pos=0 0 0 erg=d1 par=1 vec=1 0 0 dir=d2
si2 -1  0.99990531  1          $ histogram for cosine bin limits
sp2  0  0.99995265  0.00004735 $ frac. solid angle for each bin
sb2  0. 0.          1.         $ source bias for each bin
si1 H    0.0
         5.5  6.5  7.5  8.5  9.5 10.5 11.5 12.5 13.5 14.5
        15.5 16.5 17.5 18.5 19.5 20.5 21.5 22.5 23.5 24.5
        25.5 26.5 27.5 28.5 29.5 30.5 31.5 32.5 33.5 34.5
        35.5 36.5 37.5 38.5 39.5 40.5 41.5 42.5 43.5 44.5
        45.5 46.5 47.5 48.5 49.5 50.5 51.5 52.5 53.5 54.5
        55.5 56.5 57.5 58.5 59.5 60.5 61.5 62.5 63.5 64.5
        65.5 66.5 67.5 68.5 69.5 70.5 71.5 72.5
  sp1   0.0      0.
        2.373E-2 2.373E-2 2.395E-2 2.440E-2 2.508E-2
        2.569E-2 2.533E-2 2.592E-2 2.678E-2 2.714E-2
        2.788E-2 2.795E-2 2.855E-2 2.954E-2 3.100E-2
        3.149E-2 3.334E-2 3.383E-2 3.528E-2 3.624E-2
        3.669E-2 3.841E-2 3.806E-2 3.927E-2 3.845E-2
        3.875E-2 3.857E-2 3.878E-2 3.762E-2 3.702E-2
        3.716E-2 3.656E-2 3.615E-2 3.399E-2 3.345E-2
        3.324E-2 3.340E-2 3.137E-2 3.211E-2 3.103E-2
        3.102E-2 3.160E-2 3.086E-2 3.003E-2 2.856E-2
        2.804E-2 2.656E-2 2.505E-2 2.391E-2 2.177E-2
        1.959E-2 1.604E-2 1.281E-2 1.088E-2 9.010E-3
        7.428E-3 8.095E-3 4.701E-2 2.104E-1 3.614E-1
        2.765E-1 8.202E-2 8.896E-3 1.074E-3 4.013E-4
        4.973E-4 1.324E-4
c -----------------------------------------------------------------------------
c         TALLIES
c -----------------------------------------------------------------------------  
c Experimental results in SINBAD documentation - Table 28 (JAERI-Data/Code J96-005 Table 22), July 2018
c -------------------------------------------------
c Table 28  Reaction rates behind iron measured by the Bonner sphere
c           spectrometer for 68-MeV p-Li neutrons
c -------------------------------------------------
c Counter     Reaction rate (counts microC-1)
c           20cm thick  40cm thick  100cm thick
c -------------------------------------------------
c  Bare      9.205E+2*   4.948E+2    7.238E+1
c 1.5cm+Cd   1.087E+4    7.587E+3    6.287E+2
c   3cm      3.317E+4    1.858E+4    1.302E+3
c   5cm      5.131E+4    2.249E+4    1.343E+3
c   9cm      3.847E+4    1.344E+4    5.402E+2
c -------------------------------------------------
c * Read as 9.205 x 10**2
c Absolute normalization of results 1.31126E+11 (=2.61*4000000000*4*3.14=peak to continuum from SINBAD html note, peak flux of neutrons in SINBAD html, solid angle (4 pi))    
c Bare Bonner sphere response function from from Table 26
F14:n 129 t
FC14 Bare Bonner sphere - on-axis
FM14 1.31126E+11
DE14 LIN 
     4.14E-07 1.12E-06 5.04E-06 2.26E-05 4.54E-04 3.35E-03 1.50E-02 8.65E-02
     2.24E-01 4.98E-01 9.07E-01 1.35E+00 2.02E+00 3.01E+00 4.49E+00 6.70E+00
     1.00E+01 1.35E+01 1.75E+01 2.25E+01 2.75E+01 3.50E+01 4.50E+01 5.50E+01
     6.50E+01 8.00E+01 1.00E+02 1.20E+02 1.60E+02 2.00E+02 2.50E+02 3.00E+02
     3.50E+02 4.00E+02
DF14 LIN 
     1.8810E+01 1.7590E+01 9.5960E+00 4.5370E+00 1.5720E+00 4.0110E-01
     1.6160E-01 6.6420E-02 2.8140E-02 1.8310E-02 1.5580E-02 3.3150E-02 
     5.4740E-02 5.2850E-02 4.6920E-02 3.9020E-02 3.0720E-02 2.3130E-02
     1.7300E-02 1.1330E-02 7.9280E-03 3.0890E-03 0.0000E+00 0.0000E+00
     0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00
     0.0000E+00 0.0000E+00 0.0000E+00 0.0000E+00  
c 15 mm Bonner sphere response function from from Table 26
F24:n 130 129 t
FC24 15 mm Bonner sphere - on-axis
FM24 1.31126E+11
DE24 LIN 
     4.14E-07 1.12E-06 5.04E-06 2.26E-05 4.54E-04 3.35E-03 1.50E-02 8.65E-02
     2.24E-01 4.98E-01 9.07E-01 1.35E+00 2.02E+00 3.01E+00 4.49E+00 6.70E+00
     1.00E+01 1.35E+01 1.75E+01 2.25E+01 2.75E+01 3.50E+01 4.50E+01 5.50E+01
     6.50E+01 8.00E+01 1.00E+02 1.20E+02 1.60E+02 2.00E+02 2.50E+02 3.00E+02
     3.50E+02 4.00E+02
DF24 LIN 
     1.300E+02 7.941E+00 1.239E+01 1.171E+01 8.548E+00 6.596E+00
     5.175E+00 3.949E+00 2.922E+00 2.084E+00 1.387E+00 9.762E-01
     7.286E-01 5.126E-01 3.509E-01 2.399E-01 1.541E-01 1.263E-01
     1.396E-01 1.284E-01 1.154E-01 1.185E-01 1.018E-01 1.024E-01
     1.049E-01 1.069E-01 1.072E-01 1.072E-01 1.090E-01 1.110E-01
     1.131E-01 1.168E-01 1.204E-01 1.212E-01 
c 30 mm Bonner sphere response function from from Table 26
F34:n 131 130 129 t
FC34 30 mm Bonner sphere - on-axis
FM34 1.31126E+11
DE34 LIN 
     4.14E-07 1.12E-06 5.04E-06 2.26E-05 4.54E-04 3.35E-03 1.50E-02 8.65E-02
     2.24E-01 4.98E-01 9.07E-01 1.35E+00 2.02E+00 3.01E+00 4.49E+00 6.70E+00
     1.00E+01 1.35E+01 1.75E+01 2.25E+01 2.75E+01 3.50E+01 4.50E+01 5.50E+01
     6.50E+01 8.00E+01 1.00E+02 1.20E+02 1.60E+02 2.00E+02 2.50E+02 3.00E+02
     3.50E+02 4.00E+02
DF34 LIN 
     2.6070E+00 6.9920E+00 9.0830E+00 1.0400E+01 1.0660E+01 1.0010E+01
     9.2510E+00 8.4810E+00 7.7650E+00 6.8080E+00 5.5390E+00 4.4200E+00
     3.4820E+00 2.5870E+00 1.8300E+00 1.2730E+00 7.9260E-01 5.3480E-01
     4.2460E-01 3.1650E-01 2.4090E-01 1.9950E-01 1.6900E-01 1.5600E-01
     1.4680E-01 1.3490E-01 1.2260E-01 1.1040E-01 9.6540E-02 8.4840E-02
     7.8660E-02 7.3260E-02 6.7100E-02 6.6240E-02 
c 50 mm Bonner sphere response function from from Table 26
F44:n 132 131 130 129 t
FC44 50 mm Bonner sphere - on-axis
FM44 1.31126E+11
DE44 LIN 
     4.14E-07 1.12E-06 5.04E-06 2.26E-05 4.54E-04 3.35E-03 1.50E-02 8.65E-02
     2.24E-01 4.98E-01 9.07E-01 1.35E+00 2.02E+00 3.01E+00 4.49E+00 6.70E+00
     1.00E+01 1.35E+01 1.75E+01 2.25E+01 2.75E+01 3.50E+01 4.50E+01 5.50E+01
     6.50E+01 8.00E+01 1.00E+02 1.20E+02 1.60E+02 2.00E+02 2.50E+02 3.00E+02
     3.50E+02 4.00E+02
DF44 LIN 
     1.1900E+00 3.2540E+00 4.4370E+00 5.5360E+00 6.7090E+00 7.4790E+00
     7.8610E+00 8.3930E+00 9.2430E+00 9.7680E+00 9.5600E+00 8.7850E+00
     7.7210E+00 6.3170E+00 4.8820E+00 3.7210E+00 2.4980E+00 1.7580E+00
     1.4380E+00 1.1150E+00 8.6490E-01 7.1980E-01 6.1060E-01 5.6230E-01
     5.2960E-01 4.8680E-01 4.4250E-01 3.9980E-01 3.5290E-01 3.1320E-01
     2.9340E-01 2.7370E-01 2.4920E-01 2.4650E-01 
c 90mm Bonner sphere response function from from Table 26
F54:n 133 132 131 130 129 t
FC54 90mm Bonner sphere - on-axis
FM54 1.31126E+11
DE54 LIN 
     4.14E-07 1.12E-06 5.04E-06 2.26E-05 4.54E-04 3.35E-03 1.50E-02 8.65E-02
     2.24E-01 4.98E-01 9.07E-01 1.35E+00 2.02E+00 3.01E+00 4.49E+00 6.70E+00
     1.00E+01 1.35E+01 1.75E+01 2.25E+01 2.75E+01 3.50E+01 4.50E+01 5.50E+01
     6.50E+01 8.00E+01 1.00E+02 1.20E+02 1.60E+02 2.00E+02 2.50E+02 3.00E+02
     3.50E+02 4.00E+02
DF54 LIN 
     2.1930E-01 5.8120E-01 8.0430E-01 1.0360E+00 1.3810E+00 1.7400E+00
     2.0440E+00 2.5740E+00 3.6130E+00 5.1650E+00 6.9530E+00 8.1840E+00
     8.7680E+00 8.5140E+00 7.6720E+00 6.9450E+00 5.3270E+00 4.0990E+00
     3.4860E+00 2.8560E+00 2.2980E+00 1.9410E+00 1.6580E+00 1.5270E+00
     1.4430E+00 1.3320E+00 1.2160E+00 1.1070E+00 9.9070E-01 8.9100E-01
     8.4400E-01 7.9050E-01 7.1890E-01 7.1410E-01
print
c nps 1000000
prdmp  2J  -1
