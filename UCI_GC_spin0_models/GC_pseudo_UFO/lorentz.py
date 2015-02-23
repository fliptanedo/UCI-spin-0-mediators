# This file was automatically created by FeynRules 2.1
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Thu 16 Oct 2014 15:27:30


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SSS6 = Lorentz(name = 'SSS6',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS13 = Lorentz(name = 'FFS13',
                spins = [ 2, 2, 1 ],
                structure = 'Gamma5(2,1)')

FFS14 = Lorentz(name = 'FFS14',
                spins = [ 2, 2, 1 ],
                structure = 'Identity(2,1)')

FFS15 = Lorentz(name = 'FFS15',
                spins = [ 2, 2, 1 ],
                structure = 'ProjM(2,1) + ProjP(2,1)')

FFV21 = Lorentz(name = 'FFV21',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,1)')

FFV22 = Lorentz(name = 'FFV22',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV23 = Lorentz(name = 'FFV23',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV24 = Lorentz(name = 'FFV24',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

VVS13 = Lorentz(name = 'VVS13',
                spins = [ 3, 3, 1 ],
                structure = '-4*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1) + 4*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS14 = Lorentz(name = 'VVS14',
                spins = [ 3, 3, 1 ],
                structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS15 = Lorentz(name = 'VVS15',
                spins = [ 3, 3, 1 ],
                structure = 'Metric(1,2)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS6 = Lorentz(name = 'SSSS6',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS6 = Lorentz(name = 'VVSS6',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVS6 = Lorentz(name = 'VVVS6',
                spins = [ 3, 3, 3, 1 ],
                structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVVV26 = Lorentz(name = 'VVVV26',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV27 = Lorentz(name = 'VVVV27',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV28 = Lorentz(name = 'VVVV28',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV29 = Lorentz(name = 'VVVV29',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV30 = Lorentz(name = 'VVVV30',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

