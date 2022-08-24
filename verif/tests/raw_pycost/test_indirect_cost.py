# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

from pycost.utils import basic_types
from pycost.prices import elementary_price
from pycost.prices import unit_price
from pycost.structure import unit_price_quantities
from pycost.structure import chapter
from pycost.structure import obra

# Create root chapter.
site= obra.Obra(cod="test", tit="Test title")

# Create elementary prices.
threePercent= elementary_price.ElementaryPrice(cod= '%003', tit= "3 % Medios auxiliares", ud="%", p=0.0, tp= basic_types.sin_clasif, long_description= "3 % Medios auxiliares")
site.precios.elementos.Append(threePercent) # Append elementary price.

ten= elementary_price.ElementaryPrice(cod='TEN', tit= 'Ten', ud= 'h', p= 10.0, tp= basic_types.mdo, long_description= 'Ten')
site.precios.elementos.Append(ten) # Append elementary price.

five= elementary_price.ElementaryPrice(cod='FIVE', tit= 'Five', ud= 'h', p= 5.00, tp= basic_types.mdo, long_description= 'Five')
site.precios.elementos.Append(five) # Append elementary price.

two= elementary_price.ElementaryPrice(cod='TWO', tit= 'Two', ud= 'kg', p= 2.00, tp= basic_types.mat, long_description= 'Two')
site.precios.elementos.Append(two) # Append elementary price.

one= elementary_price.ElementaryPrice(cod='ONE', tit= 'One', ud= 'kg', p= 1.00, tp= basic_types.mat, long_description= 'One')
site.precios.elementos.Append(one) # Append elementary price.


# Create unit price.
twenty= unit_price.UnitPrice(cod='TWENTY', desc='Twenty.', ud="kg", ld= 'Twenty.')
## Append unit price components.
twenty.Append(entity= ten, f= 1.0, r= 1.0)
twenty.Append(entity= five, f= 1.0, r= 1.0)
twenty.Append(entity= two, f= 1.0, r= 2.0)
twenty.Append(entity= one, f= 1.0, r= 1.0)
twenty.Append(entity= threePercent, f= 1.0, r= .03)
price= twenty.getPrice()
refPrice= 20*1.03

ratio= (float(price)-refPrice)/refPrice

'''
print(price)
print(ratio)
'''

import os
import logging
fname= os.path.basename(__file__)
if (ratio<1e-12):
    print('test: '+fname+': ok.')
else:
    logging.error('test: '+fname+' ERROR.')

