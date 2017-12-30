#BC3Component.py

import fr_entity
import bc3_entity
from pycost.prices.price_justification import PriceJustificationRecord as pjr
from pycost.utils import basic_types


class BC3Component(fr_entity.EntFR):
    '''Component of a price decomposition.'''

    def __init__(self, e= None, f=1.0, r= 1.0):
        super(BC3Component,self).__init__(f,r)
        self.ent= e

    def Precio(self):
        return self.ent.Precio()*Producto()

    def PrecioR(self):
        retval= basic_types.ppl_price(self.ent.PrecioR(),3)
        retval*= self.ProductoR()
        return retval

    def StrPrecioLtx(self):
        return basic_types.human_readable(PrecioR())


    def PrecioSobre(self, sobre):
        '''For percentages.'''
        d= basic_types.ppl_price(sobre,3)
        d*= Producto()
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
        if not ((CodigoEntidad()).find('%')):
            os.write(0 + '|' + CodigoEntidad() + '|')
        super(BC3Component,self).WriteSpre(os)

    def WriteBC3(self, os):
        os.write(self.ent.CodigoBC3() + '\\')
        super(BC3Component,self).WriteBC3(os)

    def Entidad(self):
        if self.ent:
            return self.ent
        else:
            lmsg.error("La componente no se refiere a ninguna entidad" + '\n')
            exit(1)

    def getPriceJustificationRecord(self, over):
        print '  here over= ', over
        if self.isPercentage():
            return pjr.PriceJustificationRecord(CodigoEntidad(),ppl_price(self.Producto(),4),self.ent.Unidad(),self.ent.getTitle(),True,basic_types.ppl_price(Producto()*100.0),over)
        else:
            return pjr.PriceJustificationRecord(self.ent.Codigo(),basic_types.ppl_price(self.Producto(),4),self.ent.Unidad(),self.ent.getTitle(),False,self.ent.PrecioR(),0.0)


    def ImprLtxJustPre(self, os, over):
        r= self.getPriceJustificationRecord(over)
        r.ImprLtxJustPre(os)
        return r.getTotal()


    def writePriceTableTwoIntoLatexDocument(self, doc, over):
        r= self.getPriceJustificationRecord(over)
        r.writePriceTableTwoIntoLatexDocument(doc)
        return r.getTotal()


