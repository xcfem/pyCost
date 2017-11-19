# -*- coding: utf-8 -*-
#ComponentList.py

from pycost.utils import EntPyCost as epc

class ComponentList(list, epc.EntPyCost):
    '''Componentes de un precio descompuesto.'''
    def Precio(self):
        return self.PrecioR()

    def AsignaFactor(self, f):
        '''Asigna el valor f a los factores de toda la descomposición.'''
        for i in self:
            (i).factor= f

    def WriteSpre(self, os):
        if(len(self)):
            for i in self:
                i.WriteSpre(os)
            os.write('|' + endl_msdos)

    def WriteBC3(self, cod, os):
        if(len(self)):
            os.write("~D" + '|' + cod + '|')
            for i in self:
                i.WriteBC3(os)
            os.write('|' + endl_msdos)


    def PrecioR(self):
        lista= ListaJustPre(GetListaJustPre(True))#XXX Here cumulated percentages.
        return ppl_precio(float(lista.TotalRnd()))


    #not  @brief Suma de los precios de un tipo (mdo, maq, mat,...)
    def Precio(self, tipo):
        ptipo= ppl_precio3(0.0) #Precio total.
        for i in self:
            if (i).Tipo()==tipo and not (i).IsPercentage():
                ptipo+= (i).PrecioR()
        return ptipo

    def PrecioSobre(self, tipo, sobre):
        '''Computes percentages over a type.'''
        ptipo= ppl_precio3(0.0); #Precio total.
        for i in self: #Percentages.
            if (i).Tipo()==tipo and (i).IsPercentage():
                ptipo+= (i).PrecioSobre(sobre)
        return ptipo

    def SumPercentages(self, tipo):
        porc= 0.0; #Total percentage.
        for i in self: #Percentages.
            if (i).Tipo()==tipo and (i).IsPercentage():
                porc+= (i).Producto()
        return porc


    def CalculaLambda(self, objetivo):
        sum_porc = SumPercentages(sin_clasif)
        sum_pi = Precio(mdo)+Precio(maq)
        pmat = Precio(mat)
        numerador = objetivo/(1.0+sum_porc)-pmat
        return (numerador/sum_pi)


    def FuerzaPrecio(self, objetivo):
        Lambda = CalculaLambda(objetivo)
        for i in self: #Percentages.
            if(((i).Tipo()!=mat) and not ((i).IsPercentage())):
                i.productionRate*= Lambda
        if Lambda<0.0:
            lmsg.error("lambda = " + Lambda + " negativo" + '\n')

        return Lambda

    def getElementaryPricesOfType(self, tipo):
        lista= ListaRegJustPre(tipo)
        for i in self:
            if (i).Tipo()==tipo and not (i).IsPercentage():
                lista.append((i).GetRegJustPre(0.0))
        return lista

    def GetPorcentagesForType(self, tipo):
        lista= ListaRegJustPre(tipo)
        for i in self:
            if (i).Tipo()==tipo and (i).IsPercentage():
                lista.append((i).GetRegJustPre(0.0))
        return lista


    def GetListaJustPre(self, pa):
        return ListaJustPre(pa,getElementaryPricesOfType(mdo),getElementaryPricesOfType(mat),getElementaryPricesOfType(maq),getElementaryPricesOfType(sin_clasif),GetPorcentagesForType(sin_clasif))


    def ImprLtxJustPre(self, os, pa):
        lista= ListaRegJustPre(GetListaJustPre(pa))
        lista.ImprLtxJustPre(os)

    def ImprLtxCP2(self, os, pa):
        lista= ListaRegJustPre(GetListaJustPre(pa))
        lista.ImprLtxCP2(os)

    def ImprLtxCP1(self, os, pa, genero):
        lista= ListaRegJustPre(GetListaJustPre(pa))
        lista.ImprLtxCP1(os,genero)


