# -*- coding: utf-8 -*-
#Obra.py

from pycost.structure import chapter as cp
from pycost.utils import percentages as pc
from pycost.bc3 import codigos_obra as cod
from pycost.prices import elementary_price

import pylatex
from pycost.utils import pylatex_utils
from pycost.utils import basic_types

class Obra(cp.Chapter):

    def nombre_clase(self):
        return "Obra"

    def WriteSpre(self):
        precios.WriteSpre()
        lmsg.error(u"Exportación de capítulos no implementada." + '\n')


    def __init__(self, cod="ObraSinCod", tit="ObraSinTit"):
        super(Obra,self).__init__(cod,tit,1,1)
        elem= elementary_price.ElementaryPrice("SINDESCO",basic_types.sin_desc_string,"",1.0,basic_types.mat)
        self.precios.Elementales().Append(elem)
        self.percentages= pc.Percentages()

    def BuscaPrecio(self, cod):
        retval= super(Obra,self).BuscaPrecio(cod)
        if not retval:
            print 'unit price: '+ cod + ' not found.'
        return retval

    def CodigoBC3(self):
        return super(Obra,self).CodigoBC3() + "#"

    def newChapter(self, cap_padre, cap):
        ''' Appends the chapter to the sub-chapter
            obtained from the string of the form 1\2\1\4.'''
        if(cap_padre==""): #root chapter.
            subcapitulos.newChapter(cap)
        else:
            self.BuscaSubcapitulo(cap_padre).getSubcapitulos().newChapter(cap)

    def AppendUnitPriceQuantities(self, cap_padre, m):
        ''' Appends la partida being passed as parameter
            to the sub-chapter indicated by the string
            of the form 1\2\1\4.'''
        BuscaSubcapitulo(cap_padre).AppendUnitPriceQuantities(m)

    def LeeMedicSpre(self, iS):
        cdg= ""
        while(not iS.eof()):
            if iS.peek()==26:
                resto= ''
                getline(iS,resto,'\n')
                continue

            lista= ''
            getline(iS,lista,'|')
            if(lista==""): break
            if(lista!=cdg): #capitulo nuevo
                cod= replace(lista,'/','_')
                tit= ''
                getline(iS,tit,'\n')
                tit= q_blancos(tit.substr(0,len(tit)-1))
                lmsg.error(u"Cargando capítulo: " + cod + ' ' + tit + '*' + '\n')
                cp= Chapter(cod,tit)
                ruta= replace(lista,'/','\\')
                pos= ruta.find('\\')
                if(pos>len(ruta)): #Es capítulo raiz.
                    newChapter("",cp)
                else: #es capitulo.pyijo.
                    pos2= ruta.rfind('\\')
                    ruta= ruta.substr(0,pos2)
                    newChapter(ruta,cp)

                cdg= lista
            else: #Medicion
                cod= replace(lista,'/','\\')
                contenido= ''
                getline(iS,contenido,'\n')
                pos= contenido.find('|')
                cod_ud_obra= contenido.substr(0,pos)
                contenido= contenido.substr(pos+1,len(contenido))
                udo= precios.searchForUnitPrice(cod_ud_obra)
                if not udo:
                    lmsg.error("Unidad de obra: " + cod_ud_obra
                              + " no encontrada" + '\n')
                    return

                muo= UnitPriceQuantities(udo)
                while(True):
                    pos= contenido.find('|')
                    comentario= contenido.substr(0,pos)
                    contenido= contenido.substr(pos+1,len(contenido))
                    pos= contenido.find('|')
                    uds= contenido.substr(0,pos)
                    contenido= contenido.substr(pos+1,len(contenido))
                    pos= contenido.find('|')
                    lng= contenido.substr(0,pos)
                    contenido= contenido.substr(pos+1,len(contenido))
                    pos= contenido.find('|')
                    lat= contenido.substr(0,pos)
                    contenido= contenido.substr(pos+1,len(contenido))

                    pos= contenido.find('|')
                    alt= ""
                    if pos>len(contenido):
                        pos= contenido.find('\n')
                        alt= contenido.substr(0,pos-1)
                        rm= MeasurementRecord(comentario,float(uds),float(lng),float(lat),float(alt))
                        muo.Append(rm)
                        break

                    else:
                        alt= contenido.substr(0,pos)
                        contenido= contenido.substr(pos+1,len(contenido))
                        rm= MeasurementRecord(comentario,float(uds),float(lng),float(lat),float(alt))
                        muo.Append(rm)


                AppendUnitPriceQuantities(cod,muo)

    def LeeSpre(self, iS):
        str= ''
        precios.LeeSpre(iS)
        getline(iS,Str,'\n')
        if Str.find("[MED]")<len(Str):
            LeeMedicSpre(iS)


    def findChapterMedicion(self,ruta):
        ruta.pop_back(); #Eliminamos el último elemento que es la posición.
        return self.BuscaSubcapitulo(ruta)


    def LeeBC3DatosObra(self, obra):
        if obra.size()<1:
            lmsg.error(u"No se encontró la obra." + '\n')
        reg= obra.getChapterData(obra.begin())
        self.codigo= reg.Codigo(); #Código
        self.titulo= reg.Datos().getTitle(); #Título
        subcapitulos.newChapters(reg.Datos().desc)

    def readQuantitiesFromBC3(self, co):
        med= co.getQuantityData()
        if med.size()<1:
            lmsg.error("Quantities not found." + '\n')
        for i in med:
            reg= med.GetDatosMedicion(i)
            # UnitPrice *ud= precios.searchForUnitPrice(reg.CodigoUnidad())
            cod_unidad= copia_desde(reg.CodigoUnidad(),'@')
            ud= self.BuscaPrecio(cod_unidad)
            if not ud:
                lmsg.error(u"Obra.readQuantitiesFromBC3: No se encontró el precio: \'"
                          + cod_unidad + "\'" + '\n')
                lmsg.error(u"  El concepto de código: \'" + cod_unidad + "\'")
                if not co.ExisteConcepto(cod_unidad):
                    lmsg.error(" no existe." + '\n')
                else:
                    lmsg.error(" exists in the table: "
                              + co.StrTablaConcepto(cod_unidad) + '\n')


            else:
                m= UnitPriceQuantities(ud)
                m.LeeBC3(reg.Datos())
                r=reg.Datos().Ruta()
                c= findChapterMedicion(r)
                if not c:
                    c= BuscaCodigo(reg.getChapterCode())
                if c:
                    c.AppendUnitPriceQuantities(m)
                else:
                    lmsg.error(u"No se encontró el capítulo: " + reg.getChapterCode() + '\n')



    def LeeBC3(self, iS):
        co= CodigosObra()
        logging.info("Leyendo registros FIEBDC 3...")
        co.LeeBC3(iS,verborrea); #Carga los registros BC3.
        logging.info("hecho." + '\n')
        logging.info(u"Leyendo estructura de capítulos...")
        LeeBC3DatosObra(co.GetDatosObra())
        subcapitulos.LeeBC3Caps(co); #Lee capitulos y precios elementales.
        logging.info("hecho." + '\n')

        logging.info("Leyendo precios...")
        precios.LeeBC3Elementales(co.GetDatosElementos()); #Lee los precios elementales fuera de capítulo.

        #LeeBC3DescFase1(co); #Lee descompuestos de capitulos.
        precios.LeeBC3DescompFase1(co.GetDatosUnidades())

        logging.info("hecho." + '\n')
        logging.info("Leyendo descomposiciones...")

        #pendientes= LeeBC3DescFase2(co); #Lee descomposiciones.
        pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades())

        logging.info("hecho." + '\n')
        logging.info("Leyendo precios globales...")
        precios.LeeBC3DescompFase1(co.GetDatosUnidades())
        tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades())
        logging.info("num. precios= " + precios.NumDescompuestos() + '\n')
        pendientes.insert(tmp.begin(),tmp.end())
        logging.info("hecho." + '\n')
        if pendientes.size():
            logging.info("   Leyendo descomposiciones (y 2)...")
            #pendientes= LeeBC3DescFase2(co); #Lee descomposiciones.
            pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades()); #Lee descomposiciones.
            logging.info("hecho." + '\n')
            logging.info("   Leyendo precios globales (y 2)...")
            precios.LeeBC3DescompFase1(co.GetDatosUnidades())
            tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades())
            pendientes.insert(tmp.begin(),tmp.end())
            logging.info("hecho." + '\n')

        logging.info("Reading quantities...")

        readQuantitiesFromBC3(co)
        logging.info("hecho." + '\n')

    def ImprLtxPresEjecMat(self, doc):
        #doc.append(u"\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución material}" + '\n')
        chapter= pylatex_utils.Chapter(title= u'Presupuesto de ejecución material',numbering= False)
        chapter.append(pylatex.Command('cleardoublepage'))
        center= pylatex.Center()
        center.append(pylatex_utils.LargeCommand())
        center.append(pylatex.utils.bold(u'Presupuesto de Ejecución Material'))
        center.append(pylatex_utils.largeCommand())
        chapter.append(center)
        chapter.append(pylatex.VerticalSpace('2cm'))
        self.subcapitulos.ImprLtxResumen(chapter,"",False)
        chapter.append(pylatex.utils.bold(u'Presupuesto de Ejecución Material:'))
        chapter.append(pylatex.Command('dotfill'))
        chapter.append(pylatex.utils.bold(self.StrPrecioLtx()))
        chapter.append(pylatex.VerticalSpace('0.5cm'))
        chapter.append(u'Asciende el presente presupuesto de ejecución material a la expresada cantidad de: ')
        chapter.append(pylatex_utils.textsc(basic_types.to_words(self.PrecioR(),False) + ' euros.'))
        chapter.append(pylatex_utils.input('firmas'))
        doc.append(chapter)
        
    def ImprLtxPresContrata(self, doc):
        #doc.append(u"\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución por contrata}" + '\n')
        chapter= pylatex_utils.Chapter(title= u'Presupuesto de ejecución por contrata',numbering= False)
        chapter.append(pylatex.Command('cleardoublepage'))
        center= pylatex.Center()
        center.append(pylatex_utils.LargeCommand())
        center.append(pylatex.utils.bold(u'Presupuesto de Ejecución por Contrata'))
        center.append(pylatex_utils.largeCommand())
        chapter.append(center)
        chapter.append(pylatex.VerticalSpace('2cm'))
        self.percentages.printLtx(chapter,self.PrecioR())
        chapter.append(pylatex_utils.input('firmas'))
        doc.append(chapter)

    def WriteBC3(self, os, pos):
        os.write("~V|Iturribizia, S.L.|FIEBDC-3/95|ppl 0.1|" + endl_msdos)
        WritePreciosBC3(os)
        WriteConceptoBC3(os)
        WriteDescompBC3(os)
        WriteQuantities(os,pos)
        WriteSubChapters(os,True,pos)


    def ImprLtxPresGen(self, doc):
        part= pylatex_utils.Part("Presupuestos Generales")
        self.ImprLtxPresEjecMat(doc)
        self.ImprLtxPresContrata(doc)

    def writeQuantitiesIntoLatexDocument(self, doc):
        super(Obra,self).writeQuantitiesIntoLatexDocument(doc,'root')

    def ImprCompLtxMed(self, otra, os):
        doc.create(pylatex_utils.ltx_part(basic_types.quantitesCaption) + '\n')
        doc.create(pylatex.Command('parttoc'))
        doc.create(pylatex_utils.ltx_begin("landscape") + '\n')
        super(Obra,self).ImprCompLtxMed(os,'root',otra)
        doc.create(pylatex_utils.ltx_end("landscape") + '\n')

    def writePriceTableOneIntoLatexDocument(self, doc):
        part= pylatex_utils.Part("Cuadro de precios no. 1")
        part.append(pylatex.Command('parttoc'))
        part.append(pylatex.Command('setcounter{chapter}{0}'))
        super(Obra,self).writePriceTableOneIntoLatexDocument(part,'root')
        part.append(pylatex.Command('input{firmas}'))
        doc.append(part)

    def writePriceTableTwoIntoLatexDocument(self, doc):
        part= pylatex_utils.Part("Cuadro de precios no. 2")
        part.append(pylatex.Command('parttoc'))
        part.append(pylatex.Command('setcounter{chapter}{0}'))
        super(Obra,self).writePriceTableTwoIntoLatexDocument(part,'root')
        part.append(pylatex.Command('input{firmas}'))
        doc.append(part)

    def ImprLtxJustPre(self, doc):
        super(Obra,self).ImprLtxJustPre(doc,'root')
        doc.create("\\input{firmas}" + '\n')

    def writePriceTablesIntoLatexDocument(self, doc):
        self.writePriceTableOneIntoLatexDocument(doc)
        self.writePriceTableTwoIntoLatexDocument(doc)

    def ImprLtxPreParc(self, doc):
        part= pylatex_utils.Part('Presupuestos parciales')
        part.append(pylatex.Command('parttoc'))
        part.append(pylatex.Command('setcounter{chapter}{0}'))
        super(Obra,self).ImprLtxPre(part,'root')
        doc.append(part)

    def ImprCompLtxPreParc(self, otra, doc):
        part= pylatex_utils.Part('Presupuestos parciales')
        part.append(pylatex.Command('parttoc'))
        part.append(pylatex.Command('setcounter{chapter}{0}'))
        part.append(pylatex_utils.ltx_begin("landscape") + '\n')
        super(Obra,self).ImprCompLtxPre(part,'root',otra)
        part.append(pylatex_utils.ltx_end("landscape") + '\n')
        doc.append(part)

    def ImprLtxResumen(self, doc):
        part= pylatex_utils.Part('Resumen de los presupuestos parciales')
        chapter= pylatex_utils.Chapter(title= 'Resumen',numbering= False)
        part.append(chapter)
        super(Obra,self).ImprLtxResumen(chapter,'root')
        doc.append(part)

    def ImprCompLtx(self, otra, os):
        ''' Prints the comparison with another project.'''
        #ImprCompLtxMed(otra,os)
        ImprCompLtxMed(otra,os)
        precios.writePriceTablesIntoLatexDocument(os); #Price tables.
        ImprCompLtxPreParc(otra,os)
        #ImprLtxResumen(os)

    def getLatexDocument(self):
        '''get the construction budget in LaTeX format.'''
        retval= pylatex.Document(documentclass= 'book')
        self.writeQuantitiesIntoLatexDocument(retval) #Quantities.
        self.writePriceTablesIntoLatexDocument(retval) #Price lists.
        self.ImprLtxPreParc(retval) #Presupuestos parciales.
        self.ImprLtxResumen(retval) #Resument presup. parciales.
        self.ImprLtxPresGen(retval) #Presupuestos generales.
        return retval

    def ImprLtxInformeObra(self, os):
    #Imprime en LaTeX el informe de obra.
        im= getQuantitiesReport()
        im.printLtx(os)

    def WriteHCalc(self, os):
    #Imprime la obra en LaTex.
        doc.create(basic_types.quantitesCaption + '\n')
        super(Obra,self).WriteHCalcMed(os,'root')
        doc.create("Cuadros de precios" + '\n')
        precidoc.createHCalc(os)
        doc.create("Presupuestos parciales" + '\n')
        super(Obra,self).WriteHCalcPre(os,'root')

    def SimulaDescomp(self, origen, destino):
        precios.SimulaDescomp(origen,destino)


