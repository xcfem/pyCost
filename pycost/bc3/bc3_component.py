#CompBC3.py




import fr_entity
import bc3_entity


class CompBC3(EntFR):
    '''Component of a price decomposition.'''

    def __init__(self, e= None, f=1.0, r= 1.0):
        super(CombBC3,self).__init__(f,r)
        self.ent= e

    def Precio(self):
        return self.Entidad().Precio()*Producto()

    def PrecioR(self):
        retval= ppl_precio3(Entidad().PrecioR())
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
        return Entidad().Tipo()


    def CodigoEntidad(self):
        return Entidad().Codigo()


    def IsPercentage(self):
        return Entidad().IsPercentage()


    def WriteSpre(self, os):
        if not ((CodigoEntidad()).find('%')):
            os.write(0 + '|' + CodigoEntidad() + '|')
        super(CombBC3,self).WriteSpre(os)

    def WriteBC3(self, os):
        os.write(Entidad().CodigoBC3() + '\\')
        super(CompBC3,self).WriteBC3(os)

    def Entidad(self):
        if self.ent:
            return self.ent
        else:
            lmsg.error("La componente no se refiere a ninguna entidad" + '\n')
            exit(1)

    def GetRegJustPre(self, sobre):
        if IsPercentage():
            return RegJustPre(CodigoEntidad(),ppl_precio4(Producto()),Entidad().Unidad(),Entidad().Titulo(),True,ppl_precio(Producto()*100.0),sobre)
        else:
            return RegJustPre(Entidad().Codigo(),ppl_precio4(Producto()),Entidad().Unidad(),Entidad().Titulo(),False,Entidad().PrecioR(),0.0)


    def ImprLtxJustPre(self, os, sobre):
        r= RegJustPre(GetRegJustPre(sobre))
        r.ImprLtxJustPre(os)
        return r.Total()


    def ImprLtxCP2(self, os, sobre):
        r= RegJustPre(GetRegJustPre(sobre))
        r.ImprLtxCP2(os)
        return r.Total()


