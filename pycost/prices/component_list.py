# -*- coding: utf-8 -*-
#ComponentList.py

import logging
from pycost.utils import EntPyCost as epc
from pycost.prices.price_justification import PriceJustificationList as pjl
from pycost.prices.price_justification import PriceJustificationRecordContainer as pjrc
from pycost.utils import basic_types

class ComponentList(list, epc.EntPyCost):
    '''Componentes de un precio descompuesto.'''
    def getPrice(self):
        return self.getRoundedPrice()

    def AsignaFactor(self, f):
        '''Asigna el valor f a los factores de toda la descomposición.'''
        for i in self:
            (i).factor= f

    def WriteSpre(self, os):
        if(len(self)):
            for i in self:
                i.WriteSpre(os)
            os.write('|' + '\n')

    def WriteBC3(self, cod, os):
        if(len(self)):
            os.write("~D" + '|' + cod + '|')
            for i in self:
                i.WriteBC3(os)
            os.write('|' + '\n')


    def getRoundedPrice(self):
        lista= self.getPriceJustificationList(True)#XXX Here cumulated percentages.
        return basic_types.ppl_price(float(lista.getRoundedTotal()))


    #not  @brief Suma de los precios de un tipo (mdo, maq, mat,...)
    def PrecioPorTipo(self, tipo):
        ptipo= basic_types.ppl_price(0.0) #Total price.
        for i in self:
            if (i).getType()==tipo and not (i).isPercentage():
                ptipo+= (i).getRoundedPrice()
        return ptipo

    def PrecioSobre(self, tipo, sobre):
        '''Computes percentages over a type.'''
        ptipo= basic_types.ppl_price(0.0); #Precio total.
        for i in self: #Percentages.
            if (i).getType()==tipo and (i).isPercentage():
                ptipo+= (i).PrecioSobre(sobre)
        return ptipo

    def SumPercentages(self, tipo):
        porc= 0.0; #Total percentage.
        for i in self: #Percentages.
            if (i).getType()==tipo and (i).isPercentage():
                porc+= (i).getProduct()
        return porc


    def CalculaLambda(self, objetivo):
        sum_porc= SumPercentages(sin_clasif)
        sum_pi= getPrice(mdo)+getPrice(maq)
        pmat= getPrice(mat)
        numerador= objetivo/(1.0+sum_porc)-pmat
        return (numerador/sum_pi)


    def FuerzaPrecio(self, objetivo):
        Lambda= CalculaLambda(objetivo)
        for i in self: #Percentages.
            if(((i).getType()!=mat) and not ((i).isPercentage())):
                i.productionRate*= Lambda
        if Lambda<0.0:
            logging.error("lambda= " + Lambda + " negativo" + '\n')

        return Lambda

    def getElementaryPricesOfType(self, typo):
        lista= pjrc.PriceJustificationRecordContainer(typo)
        for i in self:
            if(i.getType()==typo):
                if not i.isPercentage():
                    lista.append((i).getPriceJustificationRecord(0.0))
        return lista

    def getPourcentagesForType(self, typo):
        lista= pjrc.PriceJustificationRecordContainer(typo)
        for i in self:
            if (i).getType()==typo and (i).isPercentage():
                lista.append((i).getPriceJustificationRecord(0.0))
        return lista


    def getPriceJustificationList(self, pa):
        return pjl.PriceJustificationList(pa,self.getElementaryPricesOfType(basic_types.mdo),self.getElementaryPricesOfType(basic_types.mat),self.getElementaryPricesOfType(basic_types.maq),self.getElementaryPricesOfType(basic_types.sin_clasif),self.getPourcentagesForType(basic_types.sin_clasif))


    def writePriceJustification(self, data_table, pa):
        lista= self.getPriceJustificationList(pa)
        lista.writePriceJustification(data_table)

    def writePriceTableTwoIntoLatexDocument(self, os, pa):
        lista= self.getPriceJustificationList(pa)
        lista.writePriceTableTwoIntoLatexDocument(os)

    def writePriceTableOneIntoLatexDocument(self, os, pa, genero):
        lista= self.getPriceJustificationList(pa)
        lista.writePriceTableOneIntoLatexDocument(os,genero)


