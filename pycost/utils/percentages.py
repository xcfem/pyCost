# -*- coding: utf-8 -*-
#Percentages.py




import EntPyCost as epc
import basic_types
import pylatex
from pycost.utils import pylatex_utils

class Percentages(epc.EntPyCost):
    def __init__(self,gen= 0.17,profit= 0.06,vat= 0.21):
        super(Percentages,self).__init__()
        self.gg= gen #Gastos generales.
        self.bi= profit #Beneficio industrial.
        self.iva= vat #Impuesto sobre el valor añadido.
    @staticmethod
    def ApplyPercentage(p, pc):
        temp2= basic_types.ppl_percentage(pc)
        temp3= basic_types.ppl_price(p)
        temp3*=temp2
        return temp3

    def GGenerales(self, p):
        return self.ApplyPercentage(p,self.gg)

    def BIndustrial(self, p):
        return self.ApplyPercentage(p,self.bi)

    def IVA(self, p):
        return self.ApplyPercentage(p,self.iva)

    def printLtx(self, doc, precio_ejec_mat):
        precision= 2
        with doc.create(pylatex.Itemize()) as itemize:
            itemize.add_item(u'Total presupuesto de ejecución material ')
            itemize.append(pylatex.Command('dotfill'))
            itemize.append(basic_types.human_readable(precio_ejec_mat,precision))
            precio_gg= basic_types.ppl_price(self.GGenerales(precio_ejec_mat),precision)
            itemize.add_item(str(self.gg*100) + u'% Gastos generales ')
            itemize.append(pylatex.Command('dotfill'))
            itemize.append(basic_types.human_readable(precio_gg,precision))
            precio_bi=  basic_types.ppl_price(self.BIndustrial(precio_ejec_mat),precision)
            itemize.add_item(str(self.bi*100) + u'% Beneficio industrial ')
            itemize.append(pylatex.Command('dotfill'))
            itemize.append(basic_types.human_readable(precio_bi,precision))
            suma_gg_bi= precio_ejec_mat+precio_gg+precio_bi
            itemize.add_item('Suma ')
            itemize.append(pylatex.Command('dotfill'))
            itemize.append(basic_types.human_readable(suma_gg_bi,precision))
            precio_iva= basic_types.ppl_price(self.IVA(suma_gg_bi),precision)
            itemize.add_item(str(self.iva*100) + u'% I.V.A. ')
            itemize.append(pylatex.Command('dotfill'))
            itemize.append(basic_types.human_readable(precio_iva,precision))
            total= suma_gg_bi + precio_iva
            
        doc.append(pylatex.utils.bold(u'Presupuesto de ejecución por contrata:')+pylatex.NoEscape('\dotfill') + pylatex.utils.bold(basic_types.human_readable(total,precision)))
        doc.append(pylatex.VerticalSpace('0.5cm'))
        doc.append(pylatex.NewLine())
        doc.append(u'Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: ')
        doc.append(pylatex_utils.textsc(basic_types.to_words(total,False) + ' euros.'))

