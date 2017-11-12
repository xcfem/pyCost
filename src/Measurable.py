#Measurable.py




#include <string>
import EntBC3 as eBC3
import Codigos

class Measurable(eBC3.EntBC3):
    '''Thing that you can measure (en m,kg.py,m2,m3,...)'''

    def LeeBC3(self, r):
        super(Measurable,self).LeeBC3(r)
        self.unidad= r.Datos().Unidad()
        self.txt_largo= protege_signos(r.Datos().Texto())

    def __init__(self, cod, tit, ud):
        super(Measurable,self).__init__(cod,tit)
        self.unidad= ud
        self.txt_largo= ''

    def TextoLargo(self):
        return self.txt_largo

    def Unidad(self):
        return self.unidad

    def WriteBC3(self, os):
        self.WriteConceptoBC3(os)
        if len(self.TextoLargo())>0:
            os.write("~T|" + Codigo() + '|' + latin1TOpc850ML(TextoLargo()) + '|' + endl_msdos)

