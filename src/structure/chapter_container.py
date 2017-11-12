# -*- coding: utf-8 -*-
#Subcapitulos.py




import unit_price_table
import chapter
import codigos_obra

class Subcapitulos(list, EntPyCost):

    def __init__(self,ptr_cap):
        EntPyCost.__init__(ptr_cap)

    def getContenedor(self):
        return self

    def NumDescompuestos(self):
        nd = 0
        for j in self:
            nd+= (j).NumDescompuestos()
        return nd

    def Precio(self):
        p = 0.0
        for j in self:
            p+= (j).Precio()
        return p


    def PrecioR(self):
        p = 0.0
        for j in self:
            p+= (j).PrecioR()
        return p


    def Busca(self,ruta):
        if(len(ruta)==0): return None
        indice= int(ruta[0])-1
        existe= (indice<size())
        if not existe:
            return None
        elif(ruta.size()== 1): #Es subcapitulo de este
            return self[indice]
        else:
            sc= self[indice]
            ruta.pop_front()
            return sc.BuscaSubcapitulo(ruta)
        return None

    def BuscaCodigo(self, nmb):
        retval= None
        for i in self:
            retval= (i).BuscaCodigo(nmb)
            if(retval): return retval

        return retval

    def BuscaPrecio(self, cod):
        '''Busca una unidad de obra por el árbol de capítulos.'''
        retval= None
        for i in self:
            retval= (i).BuscaPrecio(cod)
            if(retval): break
        return retval

    def AgregaCapitulo(self, c):
        self.append(c)


    #not  @brief Agrega un capitulo.
    def AgregaCapitulo(self, r):
        self.AgregaCapitulo(Capitulo(r.codigo,"",r.factor,r.rendimiento))


    #not  @brief Agrega los capítulos que se pasan como parámetro.
    def AgregaCapitulos(self, descomp):
        sz = descomp.size()
        for i in self:
            self.AgregaCapitulo(descomp[i])


    #not  @brief Carga los datos de los subcapítulos de (self).
    def LeeBC3Caps(self, co):
        sc= Codigos(co.GetDatosCaps())
        if len(sc)<1:
            lmsg.error("No se encontraron subcapitulos." + '\n')

        nombres_capitulos= co.GetCodigosCapitulos()

        for i in self:
            j= sc.BuscaCapitulo(i.Codigo()); #sc.find(i.Codigo()); #Código
            if j:
                reg = sc.GetDatosCapitulo(j)
                if i:
                    if verborrea>4:
                        logging.info("Cargando el subcapítulo: '" + reg.Datos().Titulo() + "'\n")
                    i.titulo= reg.Datos().Titulo(); #Título

                    #Lee los elementales del capítulo.
                    elementos_capitulo = co.FiltraElementales(reg.Datos().desc)
                    i.LeeBC3Elementales(elementos_capitulo)
                    if verborrea>4:
                        logging.info("  Cargados " + elementos_capitulo.size()
                                  + " precios elementales del capítulo." + '\n')
                    co.BorraElementales(elementos_capitulo); #Borra los ya leídos.
                    if verborrea>4:
                        logging.info("  Quedan " + co.GetDatosElementos().size() + " precios elementales." + '\n')

                    #Lee los subcapítulos.
                    i.subcapitulos.AgregaCapitulos(reg.Datos().FiltraCapitulos(nombres_capitulos))
                    i.subcapitulos.LeeBC3Caps(co); #Carga los subcapitulos.


            else:
                lmsg.error("LeeBC3Caps; No se encontró el capítulo: " + i.Codigo() + '\n')
                continue




    def WriteDescompBC3(self, os, cod):
        if(len(self)<1): return
        os.write("~D" + '|'
           + cod + '|')
        for i in self:
            (i).GetCompBC3().WriteBC3(os)
        os.write('|' + endl_msdos)


    def WritePreciosBC3(self, os):
        for i in self:
            (i).WritePreciosBC3(os)


    def WriteBC3(self, os, primero, pos):
        conta = 1
        for i in self:
            nueva_pos = pos+num2str(conta,0)+'\\'
            (i).WriteBC3(os,primero,nueva_pos)
            conta+=1

    def ImprCompLtxMed(self, os, sect, otro):
        '''Suponemos que ambos capítulos tienen el 
           mismo número de subcapítulos.'''
        sz= len(otro)
        for k in range(0,sz):
            i= self[k]
            j= otro[k]
            i.ImprCompLtxMed(os,sect,j)

    def ImprLtxMed(self, os, sect):
        for j in self:
            (j).ImprLtxMed(os,sect)

    def ImprLtxCP1(self, os, sect):
        for j in self:
            (j).ImprLtxCP1(os,sect)

    def ImprLtxCP2(self, os, sect):
        for j in self:
            (j).ImprLtxCP2(os,sect)

    def ImprLtxJustPre(self, os, sect):
        for j in self:
            (j).ImprLtxJustPre(os,sect)


    def ImprLtxResumen(self, os, sect, recurre):
        if len(self):
            os.write("\\begin{itemize}" + '\n')
            for j in self:
                (j).ImprLtxResumen(os,sect,recurre)
            os.write("\\end{itemize}" + '\n')

    def ImprCompLtxPre(self, os, sect, otro):
        '''Suponemos que ambos capítulos tienen el 
           mismo número de subcapítulos.'''
        sz= len(otro)
        for k in range(0,sz):
            i= self[k]
            j= otro[k]
            (i).ImprCompLtxPre(os,sect,j)

    def ImprLtxPre(self, os, sect):
        '''Imprime presupuestos parciales.'''
        for j in self:
            (j).ImprLtxPre(os,sect)


    def WriteHCalcMed(self, os, sect):
        for j in self:
            (j).WriteHCalcMed(os,sect)


    def WriteHCalcPre(self, os, sect):
        for j in self:
            (j).WriteHCalcPre(os,sect)


    def GetInformeMediciones(self):
        retval= InformeMediciones()
        for j in self:
            retval.Merge((j).GetInformeMediciones())
        return retval

