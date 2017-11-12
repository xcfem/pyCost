# -*- coding: utf-8 -*-
#Capitulo.py




import MedsCap
import EntFR
import Subcapitulos
import price_table
import Descompuestos


class Capitulo(EntBC3):
    def __init__(cod= "CapSinCod", tit= "CapSinTit", factor= 1.0, rendimiento= 1.0):
      super(Capitulo,self).__init__(cod,tit)
      self.fr= EntFR(factor,rendimiento)
      self.subcapitulos= Subcapitulos(self)
      self.mediciones= MedsCap()
      self.precios= CuaPre() #Para precios elementales y
                             #descompuestos clasificados por capítulos.
    def TieneElementales():
        return precios.TieneElementales()
    def NumDescompuestos():
        return precios.NumDescompuestos()+subcapitulos.NumDescompuestos()
    def TieneDescompuestos():
        return NumDescompuestos()> 0
    def GetBuscadorDescompuestos():
        return self.precios.GetBuscadorDescompuestos()
    def getSubcapitulos(self):
        return self.subcapitulos
    def getMediciones(self):
        return self.mediciones
    def WriteMediciones(os, pos=""):
        self.mediciones.Write(os,CodigoBC3(),pos)
    def WriteSubCapitulos(os, primero= "False", pos=""):
        self.subcapitulos.WriteBC3(os,primero,pos)
    def CodigoBC3(self):
        return EntBC3.CodigoBC3() + "#"
    def CuadroPrecios(self):
        return precios
    def AgregaPartida(self, m):
        mediciones.append(m)
    def GetCompBC3(self):
        '''Return this chapter as a component.'''
        return CompBC3(self,fr)
    def LeeBC3Elementales(self, elementos):
        '''Appends the elementary prices from argument.'''
        self.precios.LeeBC3Elementales(elementos)
    def LeeBC3DescompFase1(self, descompuestos):
        self.precios.LeeBC3DescompFase1(descompuestos)
    def LeeBC3DescompFase2(self, descompuestos):
        return precios.LeeBC3DescompFase2(descompuestos)
    def BuscaSubcapitulo(self, ruta):
        retval= None
        if ruta:
            retval= subcapitulos.Busca(ruta)
            if not retval:
                lmsg.error("Capitulo.BuscaSubcapitulo: no se encontró el subcapítulo: " + ruta[1]
                          + " en el capítulo: " + Codigo() + " (" + Titulo()
                          + ") (ruta: " + ruta + ')' + '\n')
                #Si no encuentra el capítulo devuelve este mismo
                retval= self
        return retval
    def BuscaSubcapitulo(self, lst):
        '''Busca el subcapítulo que indica la cadena
           de caracteres que se pasa como parámetro.
           ésta es una cadena de la forma '1\2\1\4'''
        retval= None
        pos = lst.find('\\')
        if(pos>len(lst)): #No aparece la barra luego.pya de ser subcapitulo de éste.
            indice = atoi(lst.c_str())
            if indice>subcapitulos.size():
                lmsg.error("Capítulo: " + indice + " no encontrado." + '\n')
                return None

            retval= subcapitulos[indice-1]
            return retval

        else: #Ha de ser subcapitulo del que esta a la izquierda de la barra
            ind = lst.substr(0,pos)
            indice = atoi(ind.c_str())
            if indice>subcapitulos.size():
                lmsg.error("Capítulo: " + indice + " no encontrado." + '\n')
                return None

            return subcapitulos[indice-1].BuscaSubcapitulo(lst.substr(pos+1,lst.size()-1))

        lmsg.error("sale por aqui (y no debiera) en el capitulo: " + Codigo() + '\n')
        return retval
    def BuscaCodigo(self, nmb):
        if (Codigo()==nmb) or ((Codigo()+'#')==nmb):
            return self
        else:
            return subcapitulos.BuscaCodigo(nmb)
    def BuscaCodigo(self, nmb):
        if Codigo()==nmb:
            return self
        else:
            return subcapitulos.BuscaCodigo(nmb)
    def BuscaPrecio(self, cod):
        retval= precios.BuscaPrecio(cod)
        if not retval:
            retval= subcapitulos.BuscaPrecio(cod)
        return retval
    def WritePreciosBC3(self, os):
        precios.WriteBC3(os)
        subcapitulos.WritePreciosBC3(os)
    def WriteDescompBC3(self, os):
        subcapitulos.WriteDescompBC3(os,CodigoBC3())
        mediciones.WriteDescompBC3(os,CodigoBC3())
    def WriteBC3(self, os, primero, pos):
        WriteConceptoBC3(os,primero)
        WriteDescompBC3(os)
        WriteMediciones(os,pos)
        WriteSubCapitulos(os,False,pos)
    def Precio(self):
        return (subcapitulos.Precio() + mediciones.Precio()) * fr.Producto()
    def PrecioR(self):
        retval = subcapitulos.PrecioR() + mediciones.PrecioR()
        retval*= fr.Producto()
        return retval
    def SectionLtx(self, sect):
        '''Return the section from those of the parent.'''
        if(sect == "raiz"):
            return "chapter"
        elif sect == "chapter":
            return "section"
        elif sect == "section":
            return "subsection"
        elif sect == "subsection":
            return "subsubsection"
        elif sect == "subsubsection":
            return "paragraph"
        elif sect == "paragraph":
            return "subparagraph"
        else:
            return "xxx"
    def ImprCompLtxMed(self, os, sect, otro):
        if sect!="raiz":
            os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
        self.mediciones.ImprCompLtxMed(os, otro.mediciones)
        lmsg.error("aqui 1: " + Titulo() + ' ' + subcapitulos.size() + " subcapítulos" + '\n')
        lmsg.error("aqui 2: " + otro.Titulo() + ' ' + otro.subcapitulos.size() + " subcapítulos" + '\n')
        subcapitulos.ImprCompLtxMed(os,SectionLtx(sect), otro.subcapitulos)
    def ImprLtxMed(self, os, sect):
        if sect!="raiz":
            os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
        self.mediciones.ImprLtxMed(os)
        if self.mediciones.size():
            os.write("\\newpage" + '\n')
        self.subcapitulos.ImprLtxMed(os,SectionLtx(sect))
    def ImprLtxCP1(self, os, sect):
        if(TieneDescompuestos()):
            if sect!="raiz":
                os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
            if self.precios.TieneDescompuestos():
                self.precios.ImprLtxCP1(os)
            self.subcapitulos.ImprLtxCP1(os,SectionLtx(sect))
    def ImprLtxCP2(self, os, sect):
        if self.precios.TieneDescompuestos():
            if sect!="raiz":
                os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
            precios.ImprLtxCP2(os)
        subcapitulos.ImprLtxCP2(os,SectionLtx(sect))
    def ImprLtxJustPre(self, os, sect):
        if(sect!="raiz"):
            os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
        if self.precios.TieneDescompuestos():
            self.precios.ImprLtxJustPre(os)
        self.subcapitulos.ImprLtxJustPre(os,SectionLtx(sect))
    def ImprLtxResumen(self, os, sect, recurre):
        if(sect!="raiz"):
            os.write("\\item " + Titulo() + " \\dotfill\\ "
               + StrPrecioLtx() + '\n')
        else:
            os.write("\\Large\\textbf{Total}\\dotfill\\ \\textbf{"
               + StrPrecioLtx() + "} \\normalsize" + '\n')
        if(recurre):
            self.subcapitulos.ImprLtxResumen(os,SectionLtx(sect),recurre)
    def ImprCompLtxPre(self, os, sect, otro):
        if sect!="raiz":
            os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
        self.mediciones.ImprCompLtxPre(os, Titulo(),otro.mediciones,otro.Titulo())
        self.subcapitulos.ImprCompLtxPre(os,SectionLtx(sect), otro.subcapitulos)
        if self.subcapitulos:
            os.write(ltx_beg_itemize + '\n')
            os.write("\\item \\noindent \\textbf{Total " + Titulo()
               + " (P. de construcción): } \\dotfill \\textbf{"
               + otro.StrPrecioLtx() + "} " + '\n' + '\n')
            os.write("\\item \\noindent \\textbf{Total " + Titulo()
               + " (P. modificado): }\\dotfill \\textbf{"
               + StrPrecioLtx() + "} " + '\n')
            os.write(ltx_end_itemize + '\n')
            os.write("\\clearpage" + '\n')

        if self.mediciones:
            os.write("\\newpage" + '\n')
    def ImprLtxPre(self, os, sect):
        '''Imprime presupuestos parciales.'''
        if sect!="raiz":
            os.write('\\' + sect + '{' + Titulo() + '}' + '\n')
        self.mediciones.ImprLtxPre(os,Titulo())
        self.subcapitulos.ImprLtxPre(os,SectionLtx(sect))
        if self.subcapitulos:
            os.write("\\noindent \\large \\textbf{Total: " + Titulo() + "} \\dotfill \\textbf{" + StrPrecioLtx() + "} \\\\ \\normalsize" + '\n')

    def WriteHCalcMed(self, os, sect):
        if sect!="raiz":
            os.write(Titulo() + '\n')
        mediciones.WriteHCalcMed(os)
        subcapitulos.WriteHCalcMed(os,sect)

    def WriteHCalcPre(self, os, sect):
        if sect!="raiz":
            os.write(Titulo() + '\n')
        mediciones.WriteHCalcPre(os)
        os.write(tab + tab + tab + tab + "Total: " + tab + Titulo() + tab + StrPrecio() + '\n')
        subcapitulos.WriteHCalcPre(os,sect)

    def GetInformeMediciones(self):
        retval = mediciones.GetInformeMediciones()
        retval.Merge(subcapitulos.GetInformeMediciones())
        return retval

