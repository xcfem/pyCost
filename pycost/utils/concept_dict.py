# -*- coding: utf-8 -*-
#ConceptDict.py

import logging
from pycost.utils import EntPyCost as epy

class KeyMap(dict):
    def __init__(self):
        super(KeyMap,self).__init__()


class ConceptDict(epy.EntPyCost):
    claves= KeyMap()
    def __init__(self):
        super(ConceptDict,self).__init__()
        self.map= dict()
    def __len__(self):
        return len(self.map)
    def Append(self,u):
        self.claves[u.Codigo()]= u
        self.map[u.Codigo()]= u
        return u

    @staticmethod
    def err_no_encontrado(cod):
        logging.error("Concepto: " + cod + " no encontrado" + '\n')

    def Busca(self,cod):
        retval= None
        if cod in self.claves:
          retval= self.claves[cod]
        return retval

    def WriteBC3(self,os):
        for j in self.map.keys():
           self.map[j].WriteBC3(os)

    def Write(self,os):
        for j in self.map.keys():
           self.map[j].Write(os)


def find_concept(conceptName):
    return ConceptDict.claves[conceptName]
