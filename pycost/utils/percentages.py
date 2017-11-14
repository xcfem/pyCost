#Percentages.py




import EntPyCost as epc
import basic_types

class Percentages(epc.EntPyCost):
    def __init__(self,gen= 0.17,profit= 0.06,vat= 0.21):
        super(Percentages,self).__init__()
        self.gg= gen #Gastos generales.
        self.bi= profit #Beneficio industrial.
        self.iva= vat #Impuesto sobre el valor añadido.
    @staticmethod
    def ApplyPercentage(self, p, pc):
        temp2= basic_types.ppl_percentage(pc)
        temp3= basic_types.ppl_precio(p)
        temp3*=temp2
        return temp3

    def GGenerales(self, p):
        return ApplyPercentage(p,gg)

    def BIndustrial(self, p):
        return ApplyPercentage(p,bi)

    def IVA(self, p):
        return ApplyPercentage(p,iva)

    def ImprLtx(self, os, precio_ejec_mat):
        os.write("\\begin{itemize}" + '\n')
        os.write("\\item Total presupuesto de ejecución material \\dotfill\\ "
           + precio_ejec_mat.EnHumano() + '\n')
        precio_gg= ppl_precio(GGenerales(precio_ejec_mat))
        os.write("\\item " + gg*100 + "\\% Gastos generales \\dotfill\\ "
           + precio_gg.EnHumano() + '\n')
        precio_bi=  ppl_precio(BIndustrial(precio_ejec_mat))
        os.write("\\item " + bi*100 + "\\% Beneficio industrial \\dotfill\\ "
           + precio_bi.EnHumano() + '\n')
        suma_gg_bi= precio_ejec_mat+precio_gg+precio_bi
        os.write("\\item Suma \\dotfill\\ "
           + suma_gg_bi.EnHumano() + '\n')
        precio_iva= ppl_precio(IVA(suma_gg_bi))
        os.write("\\item " + iva*100 + "\\% I.V.A. \\dotfill\\ "
           + precio_iva.EnHumano() + '\n')
        os.write("\\end{itemize}" + '\n')
        total = suma_gg_bi + precio_iva
        os.write("\\textbf{Presupuesto de ejecución por contrata:} \\dotfill\\ \\textbf{ " + total.EnHumano() + '}' + '\n' + '\n' + '\n')
        os.write("\\vspace{0.5cm}" + '\n')
        os.write("Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: \\textsc{")
        os.write(total.EnLetra(False) + " euros}." + '\n')

