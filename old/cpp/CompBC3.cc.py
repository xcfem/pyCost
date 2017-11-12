#CompBC3.cxx

#include "CompBC3.h"
#include "bibXCLcmd/src/base/Buscadores.hxx"
#include "bibXCBasica/src/texto/StrTok.h"
#include "bibXCBasica/src/texto/latex.h"
#include "just_pre/RegJustPre.h"

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


