#Measurable.py

#include <string>
from pycost.bc3 import bc3_entity as eBC3
from pycost.bc3 import codes

class Measurable(eBC3.EntBC3):
    '''Thing that you can measure (en m,kg.py,m2,m3,...)'''

    def readBC3(self, r):
        ''' Read from BC3 record.'''
        super(Measurable,self).readBC3(r)
        self.unidad= r.Datos().Unidad()
        self.long_description= r.Datos().Texto()

    def __init__(self, cod, tit, ud, ld= None):
        super(Measurable,self).__init__(cod,tit)
        self.unidad= ud
        if(ld):
          self.long_description= ld #unicode(ld,encoding='utf-8')
        else:
          self.long_description= ''

    def getLongDescription(self):
        return self.long_description

    def Unidad(self):
        return self.unidad

    def WriteBC3(self, os):
        self.WriteConceptoBC3(os)
        if len(self.getLongDescription())>0:
            os.write("~T|" + self.Codigo() + '|' + self.getLongDescription() + '|' + '\n')

    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= super(Measurable, self).getDict()
        retval['long_description']= self.long_description
        retval['unit']= self.unidad
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.'''
        self.long_description= dct['long_description']
        self.unidad= dct['unit']
        super(Measurable, self).setFromDict(dct)
