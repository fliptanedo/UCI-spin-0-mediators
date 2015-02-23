# This file was automatically created by FeynRules 2.1
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Thu 16 Oct 2014 15:26:32


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SSS5 = Lorentz(name = 'SSS5',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS11 = Lorentz(name = 'FFS11',
                spins = [ 2, 2, 1 ],
                structure = 'Identity(2,1)')

FFS12 = Lorentz(name = 'FFS12',
                spins = [ 2, 2, 1 ],
                structure = 'ProjM(2,1) + ProjP(2,1)')

FFV17 = Lorentz(name = 'FFV17',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,1)')

FFV18 = Lorentz(name = 'FFV18',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV19 = Lorentz(name = 'FFV19',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV20 = Lorentz(name = 'FFV20',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

VVS11 = Lorentz(name = 'VVS11',
                spins = [ 3, 3, 1 ],
                structure = 'Metric(1,2)')

VVS12 = Lorentz(name = 'VVS12',
                spins = [ 3, 3, 1 ],
                structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVV5 = Lorentz(name = 'VVV5',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS5 = Lorentz(name = 'SSSS5',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS5 = Lorentz(name = 'VVSS5',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVS5 = Lorentz(name = 'VVVS5',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVV21 = Lorentz(name = 'VVVV21',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV22 = Lorentz(name = 'VVVV22',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV23 = Lorentz(name = 'VVVV23',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV24 = Lorentz(name = 'VVVV24',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV25 = Lorentz(name = 'VVVV25',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVVS7 = Lorentz(name = 'VVVVS7',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVS8 = Lorentz(name = 'VVVVS8',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVS9 = Lorentz(name = 'VVVVS9',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

