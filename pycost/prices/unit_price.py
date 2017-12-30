# -*- coding: utf-8 -*-
#UnitPrice.py


from pycost.utils import measurable as ms
from pycost.prices import elementary_price_container
from pycost.prices import component_list
from pycost.utils import pylatex_utils
from pycost.utils import basic_types
import pylatex

class UnitPrice(ms.Measurable):

    def __init__(self, cod="", desc="", ud="", ld= None):
        super(UnitPrice,self).__init__(cod,desc,ud,ld)
        self.components= component_list.ComponentList()
    def getType(self):
        return basic_types.mat; #XXX provisional.
    def Precio(self):
        return self.components.Precio()

    def AsignaFactor(self, f):
        self.components.AsignaFactor(f)

    def Append(self,e, f, r):
        tmp= BC3Component(e,f,r)
        self.components.append(tmp)
        return tmp

    def LeeBC3Fase1(self,r):
        '''Lee la unidad a falta de la descomposición.'''
        super(UnitPrice,self).LeeBC3(r)

    def LeeBC3Fase2(self, r, bp):
        error= False
        if r.Datos().desc.size():
            tmp= ObtienePunteros(r.Datos().desc,bp,error)
            if not error:
                components= tmp
            else:
                lmsg.error("Error al leer descomposición de la unidad: " + self.Codigo() + '\n')

        else:
            components= GetSindesco(r.Datos().Precio(),bp)
        return error

    def GetSindesco(self, productionRate, bp):
        '''Para unidades de obra sin descomposición de las que
           sólo se conoce el precio.'''
        retval= ComponentList()
        be= bp["elementos"]
        ent= be.Busca("SINDESCO")
        retval.append(BC3Component(ent,1.0,productionRate))
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
                if(verborrea>6): #Puede no ser un error.
                    lmsg.error("UnitPrice.ObtienePunteros; No se encontró la componente: " + (i).codigo + '\n')
                error= True
                continue

            else:
                retval.append(BC3Component(ent,(i).factor,(i).productionRate))
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
        objetivo= self.Precio()
        self.components= copia(otra.components)
        return self.components.FuerzaPrecio(objetivo)


    def ImprLtxJustPre(self, os):
        doc.append("\\begin{tabular}{l r l p{4cm} r r}" + '\n')
        #Cabecera
        doc.append(pylatex_utils.ascii2latex(self.Codigo()) + " & "
           + pylatex_utils.ascii2latex(self.Unidad()) + " & "
           + pylatex_utils.ltx_multicolumn(pylatex_utils.ltx_datos_multicolumn("4","p{7cm}",pylatex_utils.ascii2latex(self.getLongDescription()))) + pylatex_utils.ltx_fin_reg + '\n')
        doc.append(u"Código & Rdto. & Ud. & Descripción & Unit. & Total"
           + pylatex_utils.ltx_fin_reg + '\n' + pylatex_utils.ltx_hline + '\n')
        #Descomposición
        components.ImprLtxJustPre(os,True); #XXX Here cumulated percentages.
        doc.append("\\end{tabular}" + '\n')

    def writePriceTableOneIntoLatexDocument(self, data_table):
        data_table.add_row([pylatex_utils.ascii2latex(self.Codigo()),
                            pylatex_utils.ascii2latex(self.Unidad()),
                            pylatex_utils.ascii2latex(self.getLongDescription()),'',''])
        self.components.writePriceTableOneIntoLatexDocument(data_table,True,False); #XXX Aqui género.

    def writePriceTableTwoIntoLatexDocument(self, doc, data_table):
        tableStr= 'l r p{5.5cm} r'
        with doc.create(pylatex.Tabular(tableStr)) as nested_data_table:
            #Header
            nested_data_table.add_row([u'Código',u'Ud.',u'Descripción',u'Importe'])
            nested_data_table.add_hline()
            row= [pylatex_utils.ascii2latex(self.Codigo())]
            row.append(pylatex_utils.ascii2latex(self.Unidad()))
            row.append(pylatex_utils.ascii2latex(self.getLongDescription()))
            row.append('')
            nested_data_table.add_row(row)
            #Descomposición
            self.components.writePriceTableTwoIntoLatexDocument(nested_data_table,True); #XXX Here cumulated percentages.
            data_table.add_row([nested_data_table])

    def WriteHCalc(self, os):
        os.write(self.Codigo() + tab
           + pylatex_utils.ascii2latex(self.Unidad()) + tab
           + '"' + pylatex_utils.ascii2latex(self.getLongDescription()) + '"' + tab
           + '"' + self.StrPriceToWords(True) + '"' + tab
           + StrPrecio() + '\n')


