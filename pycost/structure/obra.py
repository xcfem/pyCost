# -*- coding: utf-8 -*-
#Obra.py

import yaml
import logging
import pylatex
from pycost.structure import chapter as cp
from pycost.structure import unit_price_quantities
from pycost.utils import percentages as pc
from pycost.bc3 import codigos_obra as cod
from pycost.prices import elementary_price
from pycost.utils import pylatex_utils
from pycost.utils import basic_types
import tempfile

def print_tree(current_node, indent="", last='updown'):

    nb_subcapitulos = lambda node: sum(nb_subcapitulos(child) for child in node.subcapitulos) + 1
    size_branch = {child: nb_subcapitulos(child) for child in current_node.subcapitulos}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.subcapitulos, key=lambda node: nb_subcapitulos(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:     
        next_last = 'up' if up.index(child) == 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * len(current_node.Codigo()))
        print_tree(child, indent=next_indent, last=next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, current_node.Codigo(), end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * len(current_node.Codigo()))
        print_tree(child, indent=next_indent, last=next_last)

def preprocess_file(inputFile):
    ''' Put each BC3 record in one line.

    :param inputFile: input file.
    '''
    separator= '~'
    def each_chunk(stream):
        buffer = ''
        while True:  # until EOF
            chunk = stream.read(4096)
            if not chunk:  # EOF?
                yield buffer
                break
            buffer+= chunk
            while True:  # until no separator is found
                try:
                    part, buffer = buffer.split(separator, 1)
                except ValueError:
                    break
                else:
                    yield part
    tmpFile= tempfile.NamedTemporaryFile(suffix='.bc3', mode='w', encoding='utf-8', delete=False)
    for chunk in each_chunk(inputFile):
        chunk= chunk.replace('\n','') # remove newline characters.
        if(len(chunk)>0):
            chunk= separator+chunk+'\n'
            tmpFile.write(chunk)  # writing chunk by chunk.
    tmpFile.close()
    return tmpFile.name

class Obra(cp.Chapter):
    ''' Construction site class.

    :ivar percentages: percentage tables.
    '''
    def __init__(self, cod="ObraSinCod", tit="ObraSinTit"):
        ''' Constructor.

        :param cod: construction site codename.
        :param tit: constuction site description.
        '''
        super(Obra,self).__init__(cod,tit,1,1)
        elem= elementary_price.ElementaryPrice("SINDESCO",basic_types.sin_desc_string,"",1.0,basic_types.mat)
        self.precios.Elementales().Append(elem)
        self.percentages= pc.Percentages()
        
    def nombre_clase(self):
        return "Obra"

    def WriteSpre(self):
        precios.WriteSpre()
        logging.error(u"Exportación de capítulos no implementada." + '\n')

    def findPrice(self, cod):
        retval= super(Obra,self).findPrice(cod)
        # if not retval:
        #     logging.error('unit price: '+ cod + ' not found.')
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

    def LeeMedicSpre(self, inputFile):
        cdg= ""
        while(not inputFile.eof()):
            if self.peek(inputFile,1)==26:
                resto= ''
                getline(inputFile,resto,'\n')
                continue

            lista= ''
            getline(inputFile,lista,'|')
            if(lista==""): break
            if(lista!=cdg): #capitulo nuevo
                cod= replace(lista,'/','_')
                tit= ''
                getline(inputFile,tit,'\n')
                tit= q_blancos(tit.substr(0,len(tit)-1))
                logging.error(u"Cargando capítulo: " + cod + ' ' + tit + '*' + '\n')
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
                getline(inputFile,contenido,'\n')
                pos= contenido.find('|')
                cod_ud_obra= contenido.substr(0,pos)
                contenido= contenido.substr(pos+1,len(contenido))
                udo= precios.searchForUnitPrice(cod_ud_obra)
                if not udo:
                    logging.error("Unidad de obra: " + cod_ud_obra
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

    def LeeSpre(self, inputFile):
        str= ''
        precios.LeeSpre(inputFile)
        getline(inputFile,Str,'\n')
        if Str.find("[MED]")<len(Str):
            LeeMedicSpre(inputFile)


    def findChapterMedicion(self,ruta):
        ruta.pop(-1) #Eliminamos el último elemento que es la posición.
        return self.BuscaSubcapitulo(ruta)


    def LeeBC3DatosObra(self, rootChapterDict):
        if(len(rootChapterDict)<1):
            logging.error('Root chapter not found.')
        key= next(iter(rootChapterDict)) # first key
        rootChapter= rootChapterDict[key]
        reg= rootChapterDict.getChapterData(key= key)
        self.codigo= reg.Codigo(); # code
        self.titulo= reg.Datos().getTitle(); # title
        components= reg.Datos().desc
        self.subcapitulos.newChapters(components)

    def readQuantitiesFromBC3(self, co):
        med= co.getQuantityData()
        if(len(med)<1):
            logging.info("No quantities in BC3 file.")
        for i in med:
            reg= med.GetDatosMedicion(i)
            # UnitPrice *ud= precios.searchForUnitPrice(reg.CodigoUnidad())
            tmp= reg.CodigoUnidad()
            cod_unidad= reg.CodigoUnidad().partition('@')[0]
            ud= self.findPrice(cod_unidad)
            if not ud:
                logging.error(u"Obra.readQuantitiesFromBC3: No se encontró el precio: \'"
                          + cod_unidad + "\'" + '\n')
                logging.error(u"  El concepto de código: \'" + cod_unidad + "\'")
                if not co.ExisteConcepto(cod_unidad):
                    logging.error(" no existe." + '\n')
                else:
                    logging.error(" exists in the table: "
                              + co.StrTablaConcepto(cod_unidad) + '\n')
            else:
                m= unit_price_quantities.UnitPriceQuantities(ud)
                m.readBC3(reg.Datos())
                ruta= reg.Datos().Ruta()
                chapterCode= reg.getChapterCode()
                c= self.findChapterMedicion(ruta)
                if not c:
                    c= self.BuscaCodigo(chapterCode)
                if c:
                    c.AppendUnitPriceQuantities(m)
                else:
                    logging.error(u"No se encontró el capítulo: " + chapterCode + '\n')


    def readBC3(self, inputFile):
        ''' Read data from FIEBDC 3 file.

        :param inputFile: input file to read from.
        '''
        tmpFileName= preprocess_file(inputFile)
        tmpFile= open(tmpFileName, 'r')
        co= cod.CodigosObra()
        logging.info("Reading FIEBDC 3 records...")
        co.readBC3(tmpFile) #Reads BC3 records.
        logging.info("done." + '\n')
        logging.info(u"Leyendo estructura de capítulos...")
        self.LeeBC3DatosObra(co.GetDatosObra())
        self.subcapitulos.LeeBC3Caps(co); #Lee capitulos y precios elementales.
        logging.info("done." + '\n')

        logging.info("Reading prices...")
        self.precios.LeeBC3Elementales(co.GetDatosElementos()); #Lee los precios elementales fuera de capítulo.

        #LeeBC3DescFase1(co); #Lee descompuestos de capitulos.
        self.precios.LeeBC3DescompFase1(co.GetDatosUnidades())

        logging.info("done." + '\n')
        logging.info("Leyendo descomposiciones...")

        #pendientes= LeeBC3DescFase2(co); #Lee descomposiciones.
        pendientes= self.precios.LeeBC3DescompFase2(co.GetDatosUnidades())

        logging.info("done." + '\n')
        logging.info("Leyendo precios globales...")
        self.precios.LeeBC3DescompFase1(co.GetDatosUnidades())
        tmp= self.precios.LeeBC3DescompFase2(co.GetDatosUnidades())
        logging.info("num. precios= " + str(self.precios.NumDescompuestos()) + '\n')
        pendientes.update(tmp)
        logging.info("done." + '\n')
        if(len(pendientes)>0):
            logging.info("   Leyendo descomposiciones (y 2)...")
            #pendientes= LeeBC3DescFase2(co); #Lee descomposiciones.
            pendientes= precios.LeeBC3DescompFase2(co.GetDatosUnidades()); #Lee descomposiciones.
            logging.info("done." + '\n')
            logging.info("   Leyendo precios globales (y 2)...")
            precios.LeeBC3DescompFase1(co.GetDatosUnidades())
            tmp= precios.LeeBC3DescompFase2(co.GetDatosUnidades())
            pendientes.insert(tmp.begin(),tmp.end())
            logging.info("done." + '\n')

        logging.info("Reading quantities...")

        self.readQuantitiesFromBC3(co)
        logging.info("done." + '\n')

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
        chapter.append(pylatex.utils.bold(self.getLtxPriceString()))
        chapter.append(pylatex.VerticalSpace('0.5cm'))
        chapter.append(pylatex.NewLine())
        chapter.append(u'Asciende el presente presupuesto de ejecución material a la expresada cantidad de: ')
        chapter.append(pylatex_utils.textsc(basic_types.to_words(self.getRoundedPrice(),False) + ' euros.'))
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
        self.percentages.printLtx(chapter,self.getRoundedPrice())
        chapter.append(pylatex_utils.input('firmas'))
        doc.append(chapter)

    def WriteBC3(self, os, pos= ''):
        os.write("~V|XC, S.L.|FIEBDC-3/2012|pyCost 0.1|\n")
        self.WritePreciosBC3(os)
        self.WriteConceptoBC3(os)
        self.WriteDescompBC3(os)
        self.WriteQuantitiesBC3(os,pos)
        self.WriteSubChaptersBC3(os,pos)

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

    def getPriceJustification(self):
        retval= pylatex.Document(documentclass= 'article')
        super(Obra,self).writePriceJustification(retval,'root')
        retval.append(pylatex.Command('input{firmas}'))
        return retval

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
        super(Obra,self).ImprLtxResumen(chapter,sect= 'root')
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
        retval.packages.append(pylatex.Package('minitoc'))
        retval.append(pylatex.Command('doparttoc'))
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

    def WriteHCalc(self, outputFile):
        ''' Write data using spreadsheet format
 
        '''
        doc.create(basic_types.quantitesCaption + '\n')
        super(Obra,self).WriteHCalcMed(outputFile,'root')
        doc.create("Cuadros de precios" + '\n')
        precidoc.createHCalc(outputFile)
        doc.create("Presupuestos parciales" + '\n')
        super(Obra,self).WriteHCalcPre(outputFile,'root')

    def SimulaDescomp(self, origen, destino):
        precios.SimulaDescomp(origen,destino)

    def printTree(self):
        print_tree(self)
        
def bc3_to_yaml(inputFileName, outputFileName, cod='CodelessRoot', tit= 'TitlelessRoot'):
    ''' Reads a BC3 file and creates the corresponding YAML format file.

    :param inputFileName: name of the input file.
    :param cod: construction site codename.
    :param tit: constuction site description.
    '''
    # Create root object.
    site= Obra(cod= cod, tit= tit)

    # Read section definition from file.
    inputFile= open(inputFileName,mode='r', encoding="latin-1")

    site.readBC3(inputFile)
    inputFile.close()

    # Write in YAML format
    with open(outputFileName, 'w') as outputFile:
        outputs= yaml.dump(site.getDict(), outputFile, allow_unicode=True)
    outputFile.close()

