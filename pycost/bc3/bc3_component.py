#BC3Component.py

import sys
import logging
from pycost.bc3 import fr_entity
from pycost.bc3 import bc3_entity
from pycost.prices.price_justification import PriceJustificationRecord as pjr
from pycost.utils import basic_types


class BC3Component(fr_entity.EntFR):
    '''Component of a price decomposition.'''

    def __init__(self, e= None, fr= fr_entity.EntFR()):
        super(BC3Component,self).__init__(fr.factor,fr.productionRate)
        self.ent= e

    def getPrice(self):
        return self.ent.getPrice()*self.getProduct()

    def getRoundedPrice(self):
        retval= self.ent.getRoundedPrice()
        retval*= self.getRoundedProduct()
        return retval

    def getLtxPriceString(self):
        return basic_types.human_readable(getRoundedPrice())


    def PrecioSobre(self, sobre):
        '''For percentages.'''
        d= basic_types.ppl_price(sobre)
        d*= getProduct()
        return d

    def StrPrecioSobreLtx(self, sobre):
        '''For percentages.'''
        return basic_types.human_readable(PrecioSobre(sobre))

    def getType(self):
        return self.ent.getType()

    def CodigoEntidad(self):
        return self.ent.Codigo()

    def isPercentage(self):
        return self.ent.isPercentage()

    def WriteSpre(self, os):
        if not ((self.CodigoEntidad()).find('%')):
            os.write(0 + '|' + self.CodigoEntidad() + '|')
        super(BC3Component,self).WriteSpre(os)

    def WriteBC3(self, os):
        os.write(self.ent.CodigoBC3() + '\\')
        super(BC3Component,self).WriteBC3(os)

    def Entidad(self):
        if self.ent:
            return self.ent
        else:
            logging.error("La componente no se refiere a ninguna entidad" + '\n')
            exit(1)

    def getPriceJustificationRecord(self, over):
        if self.isPercentage():
            return pjr.PriceJustificationRecord(self.ent.Codigo(),self.getRoundedProduct(),self.ent.Unidad(),self.ent.getTitle(),True,self.getRoundedPercentage(),over)
        else:
            return pjr.PriceJustificationRecord(self.ent.Codigo(),self.getRoundedProduct(),self.ent.Unidad(),self.ent.getTitle(),False,self.ent.getRoundedPrice(),0.0)

    def ImprLtxJustPre(self, os, over):
        r= self.getPriceJustificationRecord(over)
        r.ImprLtxJustPre(os)
        return r.getTotal()

    def writePriceTableTwoIntoLatexDocument(self, doc, over):
        ''' Write price table two into LaTeX document.

        :param doc: pylatex document to write into.
        '''
        r= self.getPriceJustificationRecord(over)
        r.writePriceTableTwoIntoLatexDocument(doc)
        return r.getTotal()

    def Write(self, os= sys.stdout):
        os.write(self.CodigoEntidad())
        super(BC3Component,self).Write(os)

    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= super(BC3Component,self).getDict()
        if(self.ent):
            retval['ent_code']= self.ent.Codigo()
        else:
            logging.error("La componente no se refiere a ninguna entidad" + '\n')
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        pendingLinks= list() # Links that cannot be set yet.
        ent_code= dct['ent_code']
        self.ent= None
        pendingLinks.append({'object':self, 'attr':'ent', 'key':ent_code}) 
        pendingLinks.extend(super(BC3Component,self).setFromDict(dct))
        return pendingLinks

