#CompBC3.py




import EntFR
import EntBC3

class RegJustPre

#not  Componente de una descomposición
class CompBC3(EntFR):
private:
    EntBC3  *ent; #Entidad a la que se refiere.
     EntBC3 &Entidad()
public:
    CompBC3()
    CompBC3( EntBC3 &e, &fr)
    CompBC3( EntBC3 &e, &f, &r)
    long double Precio()
    def ppl_precio3 PrecioR():
    std.string StrPrecioLtx()
    ppl_precio3 PrecioSobre( ppl_precio3 &sobre)
    std.string StrPrecioSobreLtx( ppl_precio3 &sobre)
    def tipo_concepto Tipo():
     CodigoEntidad()
    bool EsPorcentaje()
     WriteSpre(os)
     WriteBC3(os)
    RegJustPre GetRegJustPre( ppl_precio3 &sobre= 0.0)
    ppl_precio3 ImprLtxJustPre(os, &sobre= 0.0)
    ppl_precio3 ImprLtxCP2(os, &sobre= 0.0)



#CompBC3.cxx

import CompBC3
#include "bibXCLcmd/src/base/Buscadores.pyxx"
import bibXCBasica/src/texto/StrTok
import bibXCBasica/src/texto/latex
import just_pre/RegJustPre

CompBC3.CompBC3()
    : EntFR(),ent(NULL) {
CompBC3.CompBC3( EntBC3 &e, &fr)
    : EntFR(fr),ent(&e) {
CompBC3.CompBC3( EntBC3 &e, &f, &r)
    : EntFR(f,r),ent(&e) {
long double CompBC3.Precio()
    return Entidad().Precio()*Producto()

def PrecioR(self, ):
    ppl_precio3 retval(Entidad().PrecioR())
    retval*= ProductoR()
    return retval

def StrPrecioLtx(self, ):
    return PrecioR().EnHumano()


#Para porcentajes.
def PrecioSobre(self, &sobre):
    ppl_precio3 d(sobre)
    d*= Producto()
    return d


#Para porcentajes.
def StrPrecioSobreLtx(self, &sobre):
    return PrecioSobre(sobre).EnHumano()


def Tipo(self, ):
    return Entidad().Tipo()


 CompBC3.CodigoEntidad()
    return Entidad().Codigo()


def EsPorcentaje(self, ):
    return Entidad().EsPorcentaje()


def WriteSpre(self, &os):
    if not ((CodigoEntidad()).find('%')):
        os.write(0 + '|'
           + CodigoEntidad() + '|'
    EntFR.WriteSpre(os)

def WriteBC3(self, &os):
    os.write(Entidad().CodigoBC3() + '\\'
    EntFR.WriteBC3(os)


 EntBC3 &CompBC3.Entidad()
    if ent:
        return *ent
    else:
        std.cerr + "La componente no se refiere a ninguna entidad" + '\n'
        exit(1)



def GetRegJustPre(self, &sobre):
    if EsPorcentaje():
        return RegJustPre(CodigoEntidad(),ppl_precio4(Producto()),Entidad().Unidad(),Entidad().Titulo(),True,ppl_precio(Producto()*100.0),sobre)
    else:
        return RegJustPre(Entidad().Codigo(),ppl_precio4(Producto()),Entidad().Unidad(),Entidad().Titulo(),False,Entidad().PrecioR(),0.0)


def ImprLtxJustPre(self, &os, &sobre):
    RegJustPre r(GetRegJustPre(sobre))
    r.ImprLtxJustPre(os)
    return r.Total()


def ImprLtxCP2(self, &os, &sobre):
    RegJustPre r(GetRegJustPre(sobre))
    r.ImprLtxCP2(os)
    return r.Total()


