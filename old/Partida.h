//Partida.h
#ifndef MED_UD_OBRA_H
#define MED_UD_OBRA_H

#include "ProtoPartida.h"
#include "Mediciones.h"

class Partida : public ProtoPartida
//Partida del presupuesto correspondiente a una unidad de obra.
{
    Mediciones meds;
public:
    Partida(void): ProtoPartida() {}
    Partida(const Medible &u):ProtoPartida(u) {}
    virtual ProtoPartida *Copia(void) const
    {
        return new Partida(*this);
    }
    void Agrega(const RegMedicion &med)
    {
        meds.push_back(med);
    }
    virtual long double Total(void) const
    {
        return meds.Total();
    }
    virtual ppl_dimension TotalR(void) const
    {
        return meds.TotalR();
    }
    void LeeBC3(const regBC3_medicion &m);
    Mediciones Meds(void) const
    {
        return meds;
    }
};

#endif
