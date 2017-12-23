#PriceJustificationRecord.pyxx


class PriceJustificationRecord(object):

    def __init__(self, cod= '', rd= 0.0, ud= '', tit= '', isperc= False, unit= 0.0, b= 0.0):
        self.codigo= cod #Codigo del precio elemental.
        self.rdto= rd #Production rate.
        self.unidad= ud #Unidad de medida.
        self.titulo= tit #Descripción del precio elemental.
        self.is_percentage= isperc #True if it's a percentage.
        self.unitario= unit #Unit price (or percentage if is_percentage==True).
        self.sobre= b #Base to apply percentage over.

    def base(self):
        if self.is_percentage:
            return self.sobre
        else:
            return basic_types.ppl_precio(self.unitario,3)

    def SetBase(self, b):
        sobre= b

    def getTotal(self):
        retval= basic_types.ppl_precio(self.base(),3)
        retval*= rdto
        return retval

    def ImprLtxJustPre(self, os):
        doc.append(pylatex_utils.ascii2latex(codigo) + " & "
           + rdto.EnHumano() + " & " #Write el production rate
           + pylatex_utils.ascii2latex(unidad) + " & "
           + pylatex_utils.ascii2latex(titulo) + " & ")
        if self.is_percentage:
            doc.append(unitario.EnHumano() + pylatex_utils.ltx_porciento); #Percentage
        else:
            doc.append(unitario.EnHumano()) #Precio unitario
        doc.append(" & " + self.getTotal().EnHumano() + pylatex_utils.ltx_fin_reg + '\n')


    def writePriceTableTwoIntoLatexDocument(self, os):
        doc.append(" & & " + pylatex_utils.ascii2latex(titulo) + " & ")
        if(self.is_percentage): doc.append(self.getTotal().EnHumano()) #Total.
        doc.append(pylatex_utils.ltx_fin_reg + '\n')


