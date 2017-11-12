#Partida.py



import ProtoPartida
import Mediciones

class Partida (ProtoPartida):
#Partida del presupuesto correspondiente a una unidad de obra.
    Mediciones meds
public:
    Partida(): ProtoPartida() {
    Partida( Measurable &u):ProtoPartida(u) {
    def ProtoPartida *Copia():
        return Partida(*self)

     Agrega( RegMedicion &med)
        meds.append(med)

    def Total():
        return meds.Total()

    def ppl_dimension TotalR():
        return meds.TotalR()

     LeeBC3( regBC3_medicion &m)
    Mediciones Meds()
        return meds




#Partida.cxx

import Partida

def LeeBC3(self, &m):
    if m.med.lista_med.empty():
        RegMedicion rm("",m.med.med_total)
        meds.append(rm)

    else:
        meds.LeeBC3(m.med.lista_med)

