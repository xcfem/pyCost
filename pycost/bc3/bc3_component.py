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
        retval= ppl_precio3(ent.PrecioR())
        retval*= ProductoR()
        return retval

    def StrPrecioLtx(self):
        return PrecioR().EnHumano()


    def PrecioSobre(self, sobre):
        '''For percentages.'''
        d= ppl_precio3(sobre)
        d*= Producto()
        return d


    def StrPrecioSobreLtx(self, sobre):
        '''For percentages.'''
        return PrecioSobre(sobre).EnHumano()


    def Tipo(self):
        return ent.Tipo()


    def CodigoEntidad(self):
        return ent.Codigo()


    def IsPercentage(self):
        return ent.IsPercentage()


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

    def GetRegJustPre(self, sobre):
        if IsPercentage():
            return RegJustPre(CodigoEntidad(),ppl_precio4(Producto()),ent.Unidad(),ent.Titulo(),True,ppl_precio(Producto()*100.0),sobre)
        else:
            return RegJustPre(ent.Codigo(),ppl_precio4(Producto()),ent.Unidad(),ent.Titulo(),False,ent.PrecioR(),0.0)


    def ImprLtxJustPre(self, os, sobre):
        r= RegJustPre(GetRegJustPre(sobre))
        r.ImprLtxJustPre(os)
        return r.getTotal()


    def ImprLtxCP2(self, os, sobre):
        r= RegJustPre(GetRegJustPre(sobre))
        r.ImprLtxCP2(os)
        return r.getTotal()


