# -*- coding: utf-8 -*-
#ComponentList.py


class ComponentList(list, EntPyCost):
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
        lista= ListaJustPre(GetListaJustPre(True))#XXX Aqui porcentajes acumulados.
        return ppl_precio(float(lista.TotalRnd()))


    #not  @brief Suma de los precios de un tipo (mdo, maq, mat,...)
    def Precio(self, tipo):
        ptipo= ppl_precio3(0.0) #Precio total.
        for i in self:
            if (i).Tipo()==tipo and not (i).EsPorcentaje():
                ptipo+= (i).PrecioR()
        return ptipo

    #not  @brief Calcula los porcentajes sobre un tipo.
    def PrecioSobre(self, tipo, sobre):
        ptipo= ppl_precio3(0.0); #Precio total.
        for i in self: #Porcentajes.
            if (i).Tipo()==tipo and (i).EsPorcentaje():
                ptipo+= (i).PrecioSobre(sobre)
        return ptipo

    def SumaPorcentajes(self, tipo):
        porc= 0.0; #Porcentaje total.
        for i in self: #Porcentajes.
            if (i).Tipo()==tipo and (i).EsPorcentaje():
                porc+= (i).Producto()
        return porc


    def CalculaLambda(self, objetivo):
        sum_porc = SumaPorcentajes(sin_clasif)
        sum_pi = Precio(mdo)+Precio(maq)
        pmat = Precio(mat)
        numerador = objetivo/(1.0+sum_porc)-pmat
        return (numerador/sum_pi)


    def FuerzaPrecio(self, objetivo):
        Lambda = CalculaLambda(objetivo)
        for i in self: #Porcentajes.
            if(((i).Tipo()!=mat) and not ((i).EsPorcentaje())):
                i.rendimiento*= Lambda
        if Lambda<0.0:
            lmsg.error("lambda = " + Lambda + " negativo" + '\n')

        return Lambda

    def GetElementosTipo(self, tipo):
        lista= ListaRegJustPre(tipo)
        for i in self:
            if (i).Tipo()==tipo and not (i).EsPorcentaje():
                lista.append((i).GetRegJustPre(0.0))
        return lista

    def GetPorcentajesTipo(self, tipo):
        lista= ListaRegJustPre(tipo)
        for i in self:
            if (i).Tipo()==tipo and (i).EsPorcentaje():
                lista.append((i).GetRegJustPre(0.0))
        return lista


    def GetListaJustPre(self, pa):
        return ListaJustPre(pa,GetElementosTipo(mdo),GetElementosTipo(mat),GetElementosTipo(maq),GetElementosTipo(sin_clasif),GetPorcentajesTipo(sin_clasif))


    def ImprLtxJustPre(self, os, pa):
        lista= ListaRegJustPre(GetListaJustPre(pa))
        lista.ImprLtxJustPre(os)

    def ImprLtxCP2(self, os, pa):
        lista= ListaRegJustPre(GetListaJustPre(pa))
        lista.ImprLtxCP2(os)

    def ImprLtxCP1(self, os, pa, genero):
        lista= ListaRegJustPre(GetListaJustPre(pa))
        lista.ImprLtxCP1(os,genero)


