//Partida.cxx

#include "Partida.h"

void Partida::LeeBC3(const regBC3_medicion &m)
{
    if(m.med.lista_med.empty())
    {
        RegMedicion rm("",m.med.med_total);
        meds.push_back(rm);
    }
    else
        meds.LeeBC3(m.med.lista_med);
}
