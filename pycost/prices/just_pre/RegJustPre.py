#RegJustPre.pyxx


class RegJustPre(EntCmd):

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
            return ppl_precio(self.unitario,3)

    def SetBase(self, b):
        sobre= b

    def Total(self):
        retval= ppl_precio(self.base(),3)
        retval*= rdto
        return retval

    def ImprLtxJustPre(self, os):
        os.write(ascii2latex(codigo) + " & "
           + rdto.EnHumano() + " & " #Write el production rate
           + ascii2latex(unidad) + " & "
           + ascii2latex(titulo) + " & ")
        if self.is_percentage:
            os.write(unitario.EnHumano() + ltx_porciento); #Percentage
        else:
            os.write(unitario.EnHumano()) #Precio unitario
        os.write(" & " + Total().EnHumano() + ltx_fin_reg + '\n')


    def ImprLtxCP2(self, os):
        os.write(" & & " + ascii2latex(titulo) + " & ")
        if(self.is_percentage): os.write(Total().EnHumano()) #Total.
        os.write(ltx_fin_reg + '\n')


