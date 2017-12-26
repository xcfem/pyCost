#BC3Component.py

import fr_entity
import bc3_entity


class BC3Component(fr_entity.EntFR):
    '''Component of a price decomposition.'''

    def __init__(self, e= None, f=1.0, r= 1.0):
        super(BC3Component,self).__init__(f,r)
        self.ent= e

    def Precio(self):
        return self.ent.Precio()*Producto()

    def PrecioR(self):
        retval= basic_types.ppl_price(ent.PrecioR(),3)
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


    def Tipo(self):
        return self.ent.Tipo()


    def CodigoEntidad(self):
        return self.ent.Codigo()


    def IsPercentage(self):
        return self.ent.IsPercentage()


    def WriteSpre(self, os):
        if not ((CodigoEntidad()).find('%')):
            os.write(0 + '|' + CodigoEntidad() + '|')
        super(BC3Component,self).WriteSpre(os)

    def WriteBC3(self, os):
        os.write(ent.CodigoBC3() + '\\')
        super(BC3Component,self).WriteBC3(os)

    def Entidad(self):
        if self.ent:
            return self.ent
        else:
            lmsg.error("La componente no se refiere a ninguna entidad" + '\n')
            exit(1)

    def getPriceJustificationRecord(self, sobre):
        if IsPercentage():
            return PriceJustificationRecord(CodigoEntidad(),ppl_price(self.Producto(),4),ent.Unidad(),ent.getTitle(),True,basic_types.ppl_price(Producto()*100.0),sobre)
        else:
            return PriceJustificationRecord(ent.Codigo(),basic_types.ppl_price(self.Producto(),4),ent.Unidad(),ent.getTitle(),False,ent.PrecioR(),0.0)


    def ImprLtxJustPre(self, os, sobre):
        r= PriceJustificationRecord(getPriceJustificationRecord(sobre))
        r.ImprLtxJustPre(os)
        return r.getTotal()


    def writePriceTableTwoIntoLatexDocument(self, os, sobre):
        r= PriceJustificationRecord(getPriceJustificationRecord(sobre))
        r.writePriceTableTwoIntoLatexDocument(os)
        return r.getTotal()


