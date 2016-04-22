#MedsCap.h
#Mediciones de un capítulo.

#ifndef MEDSCAP_H
#define MEDSCAP_H

#include "Partida.h"
#include "InformeMediciones.h"
#include "bibXCBasica/src/stl/poli_deque.h"
##include "Pieza.h"


class MedsCap: public poli_deque<ProtoPartida>, EntPpl
    typedef poli_deque<ProtoPartida> dq_med
public:
    long double Precio(void)
    ppl_precio PrecioR(void)
    std.string StrPrecioLtx(void)
        return PrecioR().EnHumano()

    void Escribe(std.ostream &os, &cod, &pos="")
    void EscribeDescompBC3(std.ostream &os, &cod)
    void ImprCompLtxMed(std.ostream &os, &otra)
    void ImprLtxMed(std.ostream &os)
    void ImprCompLtxPre(std.ostream &os, &tit, &otra, &tit_otra)
    void ImprLtxPre(std.ostream &os, &tit)
    #Imprime presupuestos parciales.
    void EscribeHCalcMed(std.ostream &os)
    void EscribeHCalcPre(std.ostream &os)
    InformeMediciones GetInformeMediciones(void)


#endif
