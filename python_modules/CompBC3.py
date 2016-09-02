#CompBC3.py




import EntFR
import EntBC3

class RegJustPre

#not  Componente de una descomposición
class CompBC3(EntFR):
private:
    EntBC3  *ent; #Entidad a la que se refiere.
     EntBC3 &Entidad(void)
public:
    CompBC3(void)
    CompBC3( EntBC3 &e, &fr)
    CompBC3( EntBC3 &e, &f, &r)
    long double Precio(void)
    virtual ppl_precio3 PrecioR(void)
    std.string StrPrecioLtx(void)
    ppl_precio3 PrecioSobre( ppl_precio3 &sobre)
    std.string StrPrecioSobreLtx( ppl_precio3 &sobre)
    virtual tipo_concepto Tipo(void)
     std.string &CodigoEntidad(void)
    bool EsPorcentaje(void)
    void EscribeSpre(std.ostream &os)
    void EscribeBC3(std.ostream &os)
    RegJustPre GetRegJustPre( ppl_precio3 &sobre= 0.0)
    ppl_precio3 ImprLtxJustPre(std.ostream &os, &sobre= 0.0)
    ppl_precio3 ImprLtxCP2(std.ostream &os, &sobre= 0.0)



#CompBC3.cxx

import CompBC3
#include "bibXCLcmd/src/base/Buscadores.pyxx"
import bibXCBasica/src/texto/StrTok
import bibXCBasica/src/texto/latex
import just_pre/RegJustPre

CompBC3.CompBC3(void)
    : EntFR(),ent(NULL) {
CompBC3.CompBC3( EntBC3 &e, &fr)
    : EntFR(fr),ent(&e) {
CompBC3.CompBC3( EntBC3 &e, &f, &r)
    : EntFR(f,r),ent(&e) {
long double CompBC3.Precio(void)
    return Entidad().Precio()*Producto()

def PrecioR(self, void):
    ppl_precio3 retval(Entidad().PrecioR())
    retval*= ProductoR()
    return retval

def StrPrecioLtx(self, void):
    return PrecioR().EnHumano()


#Para porcentajes.
def PrecioSobre(self, &sobre):
    ppl_precio3 d(sobre)
    d*= Producto()
    return d


#Para porcentajes.
def StrPrecioSobreLtx(self, &sobre):
    return PrecioSobre(sobre).EnHumano()


def Tipo(self, void):
    return Entidad().Tipo()


 std.string &CompBC3.CodigoEntidad(void)
    return Entidad().Codigo()


def EsPorcentaje(self, void):
    return Entidad().EsPorcentaje()


def EscribeSpre(self, &os):
    if not ((CodigoEntidad()).find('%')):
        os << 0 << '|'
           << CodigoEntidad() << '|'
    EntFR.EscribeSpre(os)

def EscribeBC3(self, &os):
    os << Entidad().CodigoBC3() << '\\'
    EntFR.EscribeBC3(os)


 EntBC3 &CompBC3.Entidad(void)
    if ent:
        return *ent
    else:
        std.cerr << "La componente no se refiere a ninguna entidad" << std.endl
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


