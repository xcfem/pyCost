# -*- coding: utf-8 -*-
#Obra.py

from pycost.structure import chapter as cp
from pycost.utils import percentages as pc
from pycost.bc3 import codigos_obra as cod
from pycost.bc3 import bc3_entity
from pycost.prices import elementary_price

import pylatex
from pycost.utils import pylatex_utils
from pycost.utils import basic_types

class Obra(cp.Chapter):

    def nombre_clase(self):
        return "Obra"

    def WriteSpre(self):
        precios.WriteSpre()
        lmsg.error("Exportación de capítulos no implementada." + '\n')


    def __init__(self, cod="ObraSinCod", tit="ObraSinTit"):
        super(Obra,self).__init__(cod,tit,1,1)
        elem= elementary_price.ElementaryPrice("SINDESCO","Sin descomposición","",1.0,bc3_entity.mat)
        self.precios.Elementales().Append(elem)
        self.percentages= pc.Percentages()

    def BuscaPrecio(self, cod):
        retval= super(Obra,self).BuscaPrecio(cod)
        if not retval:
            print 'unit price: '+ cod + ' not found.'
        return retval

    def CodigoBC3(self):
        return Chapter.CodigoBC3() + "#"

    def newChapter(self, cap_padre, cap):
        ''' Agrega el capítulo que se pasa como
            parámetro al subcapítulo que indica la
            cadena de la forma 1\2\1\4.'''
        if(cap_padre==""): #Es un capítulo raíz
            subcapitulos.newChapter(cap)
        else:
            self.BuscaSubcapitulo(cap_padre).getSubcapitulos().newChapter(cap)

    def AppendUnitPriceQuantities(self, cap_padre, m):
        ''' Agrega la partida que se pasa como
            parámetro al subcapítulo que indica la
            cadena de la forma 1\2\1\4.'''
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
                lmsg.error("Cargando capítulo: " + cod + ' ' + tit + '*' + '\n')
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
            lmsg.error("No se encontró la obra." + '\n')
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
                lmsg.error("Obra.readQuantitiesFromBC3: No se encontró el precio: \'"
                          + cod_unidad + "\'" + '\n')
                lmsg.error("  El concepto de código: \'" + cod_unidad + "\'")
                if not co.ExisteConcepto(cod_unidad):
                    lmsg.error(" no existe." + '\n')
                else:
                    lmsg.error(" existe y está en la tabla: "
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
                    lmsg.error("No se encontró el capítulo: " + reg.getChapterCode() + '\n')



    def LeeBC3(self, iS):
        co= CodigosObra()
        logging.info("Leyendo registros FIEBDC 3...")
        co.LeeBC3(iS,verborrea); #Carga los registros BC3.
        logging.info("hecho." + '\n')
        logging.info("Leyendo estructura de capítulos...")
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

    def ImprLtxPresEjecMat(self, os):
        doc.append("\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución material}" + '\n')
        doc.append("\\addcontentsline{toc}{starchapter}{Presupuesto de ejecución material}" + '\n')
        doc.append("\\cleardoublepage" + '\n')
        doc.append("\\begin{center}" + '\n')
        doc.append("\\Large \\textbf{Presupuesto de Ejecución Material} \\large" + '\n')
        doc.append("\\end{center}" + '\n')
        doc.append("\\vspace{2cm}" + '\n')
        subcapitulos.ImprLtxResumen(os,"",False)
        doc.append("\\textbf{Presupuesto de ejecución material:} \\dotfill\\ \\textbf{" + StrPrecioLtx() + '}' + '\n' + '\n' + '\n')
        doc.append("\\vspace{0.5cm}" + '\n')
        doc.append("Asciende el presente presupuesto de ejecución material a la expresada cantidad de: \\textsc{")
        doc.append(PrecioR().EnLetra(False) + " euros}." + '\n')
        doc.append("\\input{firmas}" + '\n')

    def ImprLtxPresContrata(self, os):
        doc.append("\\subportadilla{Presupuestos Generales}{Presupuesto de ejecución por contrata}" + '\n')
        doc.append("\\addcontentsline{toc}{starchapter}{Presupuesto de ejecución por contrata}" + '\n')
        doc.append("\\cleardoublepage" + '\n')
        doc.append("\\begin{center}" + '\n')
        doc.append("\\Large \\textbf{Presupuesto de Ejecución por Contrata} \\large" + '\n')
        doc.append("\\end{center}" + '\n')
        doc.append("\\vspace{2cm}" + '\n')
        percentages.ImprLtx(os,PrecioR())
        doc.append("\\input{firmas}" + '\n')


    def WriteBC3(self, os, pos):
        os.write("~V|Iturribizia, S.L.|FIEBDC-3/95|ppl 0.1|" + endl_msdos)
        WritePreciosBC3(os)
        WriteConceptoBC3(os)
        WriteDescompBC3(os)
        WriteQuantities(os,pos)
        WriteSubChapters(os,True,pos)


    def ImprLtxPresGen(self, os):
        doc.append("\\part{Presupuestos Generales}" + '\n')
        ImprLtxPresEjecMat(os)
        ImprLtxPresContrata(os)

    def writeQuantitiesIntoLatexDocument(self, doc):
        doc.create(pylatex_utils.Part(basic_types.quantitiesCaption) + '\n')
        #doc.create(pylatex_utils.ltx_parttoc + '\n')
        super(Obra,self).writeQuantitiesIntoLatexDocument(doc,'root')

    def ImprCompLtxMed(self, otra, os):
        doc.create(pylatex_utils.ltx_part(basic_types.quantitesCaption) + '\n')
        doc.create(pylatex_utils.ltx_parttoc + '\n')
        doc.create(pylatex_utils.ltx_begin("landscape") + '\n')
        Chapter.ImprCompLtxMed(os,'root',otra)
        doc.create(pylatex_utils.ltx_end("landscape") + '\n')

    def ImprLtxCP1(self, os):
        doc.create(pylatex_utils.ltx_part("Cuadro de precios no. 1") + '\n')
        doc.create(pylatex_utils.ltx_parttoc + '\n')
        doc.create("\\setcounter{chapter}{0}" + '\n')
        Chapter.ImprLtxCP1(os,'root')
        doc.create("\\input{firmas}" + '\n')

    def ImprLtxCP2(self, os):
        doc.create(pylatex_utils.ltx_part("Cuadro de precios no. 2") + '\n')
        doc.create(pylatex_utils.ltx_parttoc + '\n')
        doc.create("\\setcounter{chapter}{0}" + '\n')
        Chapter.ImprLtxCP2(os,'root')
        doc.create("\\input{firmas}" + '\n')

    def ImprLtxJustPre(self, os):
        Chapter.ImprLtxJustPre(os,'root')
        doc.create("\\input{firmas}" + '\n')

    def ImprLtxCP(self, os):
        self.ImprLtxCP1(os)
        self.ImprLtxCP2(os)

    def ImprLtxPreParc(self, os):
        doc.create(pylatex_utils.ltx_part("Presupuestos parciales") + '\n')
        doc.create(pylatex_utils.ltx_parttoc + '\n')
        doc.create("\\setcounter{chapter}{0}" + '\n')
        Chapter.ImprLtxPre(os,'root')

    def ImprCompLtxPreParc(self, otra, os):
        doc.create(pylatex_utils.ltx_part("Presupuestos parciales") + '\n')
        doc.create(pylatex_utils.ltx_parttoc + '\n')
        doc.create("\\setcounter{chapter}{0}" + '\n')
        doc.create(pylatex_utils.ltx_begin("landscape") + '\n')
        Chapter.ImprCompLtxPre(os,'root',otra)
        doc.create(pylatex_utils.ltx_end("landscape") + '\n')

    def ImprLtxResumen(self, os):
        doc.create(pylatex_utils.ltx_part("Resumen de los presupuestos parciales") + '\n'
           + pylatex_utils.ltx_star_chapter("Resumen") + '\n')
        Chapter.ImprLtxResumen(os,'root')

    def ImprCompLtx(self, otra, os):
    #Imprime el comparativo con otra obra.
        #ImprCompLtxMed(otra,os)
        ImprCompLtxMed(otra,os)
        precios.ImprLtxCP(os); #Cuadros de precios.
        ImprCompLtxPreParc(otra,os)
        #ImprLtxResumen(os)

    def getLatexDocument(self):
        '''get the construction budget in LaTeX format.'''
        retval= pylatex.Document()
        self.writeQuantitiesIntoLatexDocument(retval) #Quantities.
        # self.ImprLtxCP(os) #Cuadros de precios.
        # self.ImprLtxPreParc(os) #Presupuestos parciales.
        # self.ImprLtxResumen(os) #Resument presup. parciales.
        # self.ImprLtxPresGen(os) #Presupuestos generales.
        return retval

    def ImprLtxInformeObra(self, os):
    #Imprime en LaTeX el informe de obra.
        im= getQuantitiesReport()
        im.ImprLtx(os)

    def WriteHCalc(self, os):
    #Imprime la obra en LaTex.
        doc.create(basic_types.quantitesCaption + '\n')
        Chapter.WriteHCalcMed(os,'root')
        doc.create("Cuadros de precios" + '\n')
        precidoc.createHCalc(os)
        doc.create("Presupuestos parciales" + '\n')
        Chapter.WriteHCalcPre(os,'root')

    def SimulaDescomp(self, origen, destino):
        precios.SimulaDescomp(origen,destino)


