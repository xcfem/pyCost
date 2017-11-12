# -*- coding: utf-8 -*-
#Partida.py



import ProtoPartida as ptp
import Mediciones as m

class Partida(ptp.ProtoPartida):
    '''Partida del presupuesto correspondiente a una unidad de obra.'''

    def __init__(self, u= None):
        super(Partida,self).__init__(u)
        meds= m.Mediciones()

    def Copia(self):
        return Partida(self)

    def Agrega(self,med):
        meds.append(med)

    def Total(self):
        return self.meds.Total()

    def TotalR(self):
        return self.meds.TotalR()

    def Meds(self):
        return self.meds

    def LeeBC3(self, m):
        if m.med.lista_med.empty():
            rm= RegMedicion("",m.med.med_total)
            meds.append(rm)
        else:
            meds.LeeBC3(m.med.lista_med)

