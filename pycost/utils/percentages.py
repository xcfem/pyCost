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
        temp3= basic_types.ppl_price(p)
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
           + basic_types.human_readable(precio_ejec_mat) + '\n')
        precio_gg= basic_types.ppl_price(GGenerales(precio_ejec_mat))
        doc.append("\\item " + gg*100 + "\\% Gastos generales \\dotfill\\ "
           + basic_types.human_readable(precio_gg) + '\n')
        precio_bi=  basic_types.ppl_price(BIndustrial(precio_ejec_mat))
        doc.append("\\item " + bi*100 + "\\% Beneficio industrial \\dotfill\\ "
           + basic_types.human_readable(precio_bi) + '\n')
        suma_gg_bi= precio_ejec_mat+precio_gg+precio_bi
        doc.append("\\item Suma \\dotfill\\ "
           + basic_types.human_readable(suma_gg_bi) + '\n')
        precio_iva= basic_types.ppl_price(IVA(suma_gg_bi))
        doc.append("\\item " + iva*100 + "\\% I.V.A. \\dotfill\\ "
           + basic_types.human_readable(precio_iva) + '\n')
        doc.append("\\end{itemize}" + '\n')
        total= suma_gg_bi + precio_iva
        doc.append("\\textbf{Presupuesto de ejecución por contrata:} \\dotfill\\ \\textbf{ " + basic_types.human_readable(total) + '}' + '\n' + '\n' + '\n')
        doc.append("\\vspace{0.5cm}" + '\n')
        doc.append("Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: \\textsc{")
        doc.append(basic_types.to_words(total,False) + " euros}." + '\n')

