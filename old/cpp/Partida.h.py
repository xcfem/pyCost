#Partida.h
#ifndef MED_UD_OBRA_H
#define MED_UD_OBRA_H

#include "ProtoPartida.h"
#include "Mediciones.h"

class Partida : public ProtoPartida
#Partida del presupuesto correspondiente a una unidad de obra.
    Mediciones meds
public:
    Partida(void): ProtoPartida() {
    Partida( Medible &u):ProtoPartida(u) {
    virtual ProtoPartida *Copia(void)
        return Partida(*self)

    void Agrega( RegMedicion &med)
        meds.push_back(med)

    virtual long double Total(void)
        return meds.Total()

    virtual ppl_dimension TotalR(void)
        return meds.TotalR()

    void LeeBC3( regBC3_medicion &m)
    Mediciones Meds(void)
        return meds



#endif
