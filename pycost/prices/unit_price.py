# -*- coding: utf-8 -*-
#UnitPrice.py

import pylatex
from pycost.utils import measurable as ms
from pycost.prices import elementary_price_container
from pycost.prices import component_list
from pycost.utils import pylatex_utils
from pycost.utils import basic_types
from pycost.bc3 import fr_entity
from decimal import Decimal

class UnitPrice(ms.Measurable):
    precision= 2
    places= Decimal(10) ** -precision
    formatString= '{0:.'+str(precision)+'f}'

    def __init__(self, cod="", desc="", ud="", ld= None):
        super(UnitPrice,self).__init__(cod,desc,ud,ld)
        self.components= component_list.ComponentList()
    def getType(self):
        return basic_types.mat; #XXX provisional.
    def getPrice(self):
        return self.components.getPrice()

    def AsignaFactor(self, f):
        self.components.AsignaFactor(f)

    def Append(self,entity, f, r):
        tmp= BC3Component(e= entity,fr= fr_entity.EntFR(f,r))
        self.components.append(tmp)
        return tmp

    def LeeBC3Fase1(self,r):
        '''Lee la unidad a falta de la descomposición.'''
        super(UnitPrice,self).readBC3(r)

    def LeeBC3Fase2(self, r, bp):
        error= False
        if r.Datos().desc.size():
            tmp= ObtienePunteros(r.Datos().desc,bp,error)
            if not error:
                components= tmp
            else:
                lmsg.error("Error al leer descomposición de la unidad: " + self.Codigo() + '\n')

        else:
            components= GetSindesco(r.Datos().getPrice(),bp)
        return error

    def GetSindesco(self, productionRate, bp):
        '''Para unidades de obra sin descomposición de las que
           sólo se conoce el precio.'''
        retval= ComponentList()
        be= bp["elementos"]
        ent= be.Busca("SINDESCO")
        factorAndRate= fr_entity.EntFR(1.0,productionRate)
        retval.append(BC3Component(e= ent,fr= factorAndRate))
        return retval

    @staticmethod
    def ObtienePunteros(self, descBC3, bp, error):
        '''Obtiene los punteros a los precios de la descomposición.'''
        retval= ComponentList()
        be= bp["elementos"]
        bd= bp["ud_obra"]
        ent= None
        for i in descBC3:
            ent= be.Busca((i).codigo)
            if not ent:
                ent= bd.Busca((i).codigo)
            if not ent:
                lmsg.warning("UnitPrice.ObtienePunteros; No se encontró la componente: " + (i).codigo + '\n')
                error= True
                continue

            else:
                retval.append(fr_entity.BC3Component(ent,i))
                error= False


        return retval



    def WriteSpre(self, os):
        os.write(self.Codigo() + '|'
           + self.Unidad() + '|'
           + getTitle() + '|')
        components.WriteSpre(os)


    def WriteBC3(self, os):
        super(UnitPrice,self).WriteBC3(os)
        self.components.WriteBC3(self.Codigo(),os)


    def SimulaDescomp(self,otra):
        '''Toma la descomposición de otra unidad de obra.
           sin alterar el precio de ésta.'''
        objetivo= self.getPrice()
        self.components= copia(otra.components)
        return self.components.FuerzaPrecio(objetivo)


    def writePriceJustification(self, data_table):
        tableStr= 'l r l p{4cm} r r'
        nested_data_table= pylatex.Tabular(tableStr)
        row= [pylatex_utils.ascii2latex(self.Codigo())]
        row.append(pylatex_utils.ascii2latex(self.Unidad()))
        row.append(pylatex.table.MultiColumn(4, align=pylatex.utils.NoEscape('p{7cm}'),data=pylatex_utils.ascii2latex(self.getLongDescription())))
        nested_data_table.add_row(row)
        #Header
        headerRow= [u'Código',u'Rdto.',u'Ud.',u'Descripción',u'Unit.',u'Total']
        nested_data_table.add_row(headerRow)
        nested_data_table.add_hline()
        #Decomposition
        self.components.writePriceJustification(nested_data_table,True); #XXX Here cumulated percentages.
        data_table.add_row([nested_data_table])

    def getLtxCodeUnitDescription(self):
        retval= [pylatex_utils.ascii2latex(self.Codigo())]
        retval.append(pylatex_utils.ascii2latex(self.Unidad()))
        retval.append(pylatex_utils.ascii2latex(self.getLongDescription()))
        return retval

    def writePriceTableOneIntoLatexDocument(self, data_table):
        row= self.getLtxCodeUnitDescription()
        row.extend(['',''])
        data_table.add_row(row)
        self.components.writePriceTableOneIntoLatexDocument(data_table,True,False); #XXX Aqui género.

    def writePriceTableTwoIntoLatexDocument(self, data_table):
        tableStr= 'l r p{5.5cm} r'
        headerRow= [u'Código',u'Ud.',u'Descripción',u'Importe']
        nested_data_table= pylatex.Tabular(tableStr)
        #Header
        nested_data_table.add_row(headerRow)
        nested_data_table.add_hline()
        row= self.getLtxCodeUnitDescription()
        row.append('')
        nested_data_table.add_row(row)
        #Decomposition
        self.components.writePriceTableTwoIntoLatexDocument(nested_data_table,True); #XXX Here cumulated percentages.
        data_table.add_row([nested_data_table])

    def WriteHCalc(self, os):
        os.write(self.Codigo() + tab
           + pylatex_utils.ascii2latex(self.Unidad()) + tab
           + '"' + pylatex_utils.ascii2latex(self.getLongDescription()) + '"' + tab
           + '"' + self.StrPriceToWords(True) + '"' + tab
           + getPriceString() + '\n')


