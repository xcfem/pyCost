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
        ''' Constructor.'''
        super(ConceptDict,self).__init__()
        self.concepts= dict()
    def __len__(self):
        return len(self.concepts)
    
    def Append(self, u):
        ''' Append the argument to the concept dictionary.'''
        key= u.Codigo()
        self.claves[key]= u
        self.concepts[key]= u
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
        for j in self.concepts.keys():
           self.concepts[j].WriteBC3(os)

    def Write(self,os):
        for j in self.concepts.keys():
           self.concepts[j].Write(os)


def find_concept(conceptName):
    return ConceptDict.claves[conceptName]
