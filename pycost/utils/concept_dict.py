# -*- coding: utf-8 -*-
#MapaConceptos.py





import EntPyCost as epy

class MapaClaves(dict):
    def __init__(self):
        super(MapaClaves,self).__init__()


class MapaConceptos(epy.EntPyCost):
    claves= MapaClaves()
    def __init__(self):
        super(MapaConceptos,self).__init__()
        self.map= dict()
    def Agrega(self,u):
        self.claves[u.Codigo()]= u
        self.map[u.Codigo()]= u

    @staticmethod
    def err_no_encontrado(cod):
        lmsg.error("Concepto: " + cod + " no encontrado" + '\n')

    def Busca(self,cod):
        i = self.claves.find(cod)
        if not i:
            #err_no_encontrado(cod)
            return None
        else:
          return self.claves[i]

    def WriteBC3(os):
        for j in self.keys:
           map[j].WriteBC3(os)

    def Write(os):
        for j in self.keys:
           map[j].Write(os)


