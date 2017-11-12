#ProtoPartida.h
#Algo capaz de devolver mediciones de una unidad de obra.

#ifndef PROTOPARTIDA_H
#define PROTOPARTIDA_H

#include "InformeUdObra.h"
#include "Mediciones.h"
#include "Tipos.h"

class ProtoPartida : public EntPpl
     Medible *ud
    void EscribeBC3RegM(std.ostream &os, &cap_padre="", &pos="")
public:
    ProtoPartida(void):ud(NULL) {
    ProtoPartida( Medible &u):ud(&u) {
    inline virtual ~ProtoPartida(void) {
    virtual ProtoPartida *Copia(void) const= 0; #Constructor virtual.
     std.string CodigoUdObra(void)
        return ud.Codigo()

     std.string UnidadMedida(void)
        return ud.Unidad()

     std.string TextoLUdObra(void)
        return ud.TextoLargo()

    long double PrecioUd(void)
        return ud.Precio()

    ppl_precio PrecioRUd(void)
        return ud.PrecioR()

    virtual long double Total(void) const= 0
    virtual ppl_dimension TotalR(void) const= 0
    InformeUdObra Informe(void)
        return InformeUdObra(ud,Total())

    std.string StrPrecioUd(void)
        return ud.StrPrecio()

    std.string StrPrecioLtxUd(void)
        return ud.StrPrecioLtx()

    long double Precio(void)
        return Total()*PrecioUd()

    ppl_precio PrecioR(void)
        return ppl_precio(double(TotalR())*double(PrecioRUd()))

    std.string StrPrecioLtx(void)
        return PrecioR().EnHumano()

    virtual Mediciones Meds(void) const= 0
    virtual void EscribeBC3(std.ostream &os, &cap_padre="", &pos="")
    #Latex.
    void ImprLtxCabecera(std.ostream &os, &totalr, ancho)
    static void ImprLtxLeyenda(std.ostream &os)
    static void ImprLtxPie(std.ostream &os, &totalr)
    void ImprCompLtxMed(std.ostream &os, &otra)
    void ImprCompLtxMed(std.ostream &os)
    void ImprLtxMed(std.ostream &os)
    void ImprLtxCabeceraPre(std.ostream &os, &totalr, ancho)
    void ImprCompLtxPre(std.ostream &os, &otra)
    void ImprCompLtxPre(std.ostream &os)
    void ImprLtxPre(std.ostream &os)
    void EscribeHCalcMed(std.ostream &os)
    void EscribeHCalcPre(std.ostream &os)


#endif
