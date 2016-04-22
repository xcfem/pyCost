//MedsCap.h
//Mediciones de un capítulo.

#ifndef MEDSCAP_H
#define MEDSCAP_H

#include "Partida.h"
#include "InformeMediciones.h"
#include "bibXCBasica/src/stl/poli_deque.h"
//#include "Pieza.h"


class MedsCap: public poli_deque<ProtoPartida>, public EntPpl
{
    typedef poli_deque<ProtoPartida> dq_med;
public:
    long double Precio(void) const;
    ppl_precio PrecioR(void) const;
    std::string StrPrecioLtx(void) const
    {
        return PrecioR().EnHumano();
    }
    void Escribe(std::ostream &os,const std::string &cod,const std::string &pos="") const;
    void EscribeDescompBC3(std::ostream &os,const std::string &cod) const;
    void ImprCompLtxMed(std::ostream &os, const MedsCap &otra) const;
    void ImprLtxMed(std::ostream &os) const;
    void ImprCompLtxPre(std::ostream &os, const std::string &tit, const MedsCap &otra, const std::string &tit_otra) const;
    void ImprLtxPre(std::ostream &os,const std::string &tit) const;
    //Imprime presupuestos parciales.
    void EscribeHCalcMed(std::ostream &os) const;
    void EscribeHCalcPre(std::ostream &os) const;
    InformeMediciones GetInformeMediciones(void) const;
};

#endif
