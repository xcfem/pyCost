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

    def printLtx(self, os, precio_ejec_mat):
        doc.append("\\begin{itemize}" + '\n')
        doc.append("\\item Total presupuesto de ejecución material \\dotfill\\ "
           + precio_ejec_mat.EnHumano() + '\n')
        precio_gg= basic_types.ppl_precio(GGenerales(precio_ejec_mat))
        doc.append("\\item " + gg*100 + "\\% Gastos generales \\dotfill\\ "
           + precio_gg.EnHumano() + '\n')
        precio_bi=  basic_types.ppl_precio(BIndustrial(precio_ejec_mat))
        doc.append("\\item " + bi*100 + "\\% Beneficio industrial \\dotfill\\ "
           + precio_bi.EnHumano() + '\n')
        suma_gg_bi= precio_ejec_mat+precio_gg+precio_bi
        doc.append("\\item Suma \\dotfill\\ "
           + suma_gg_bi.EnHumano() + '\n')
        precio_iva= basic_types.ppl_precio(IVA(suma_gg_bi))
        doc.append("\\item " + iva*100 + "\\% I.V.A. \\dotfill\\ "
           + precio_iva.EnHumano() + '\n')
        doc.append("\\end{itemize}" + '\n')
        total= suma_gg_bi + precio_iva
        doc.append("\\textbf{Presupuesto de ejecución por contrata:} \\dotfill\\ \\textbf{ " + total.EnHumano() + '}' + '\n' + '\n' + '\n')
        doc.append("\\vspace{0.5cm}" + '\n')
        doc.append("Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: \\textsc{")
        doc.append(total.EnLetra(False) + " euros}." + '\n')

