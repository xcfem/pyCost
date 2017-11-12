#Porcentajes.py




import EntPyCost
import basic_types

class Porcentajes(EntPyCost):
    float gg; #Gastos generales.
    float bi; #Beneficio industrial.
    float iva; #Impuesto sobre el valor añadido.
    def static ppl_precio AplicaPorcentaje( ppl_precio &p, &pc):
         ppl_porcentaje temp2(pc)
        ppl_precio temp3(p)
        temp3*=temp2
        return temp3

    def ppl_precio GGenerales( ppl_precio &p):
        return AplicaPorcentaje(p,gg)

    def ppl_precio BIndustrial( ppl_precio &p):
        return AplicaPorcentaje(p,bi)

    def ppl_precio IVA( ppl_precio &p):
        return AplicaPorcentaje(p,iva)

public:
    Porcentajes( float &g= .17, &b=.06, i=.16)
        : gg(g), bi(b), iva(i) {
     ImprLtx(os, &precio_ejec_mat)



#Porcentajes.cxx

import Porcentajes

def ImprLtx(self, &os, &precio_ejec_mat):
    os.write("\\begin{itemize}" + '\n'
    os.write("\\item Total presupuesto de ejecución material \\dotfill\\ "
       + precio_ejec_mat.EnHumano() + '\n'
     ppl_precio precio_gg(GGenerales(precio_ejec_mat))
    os.write("\\item " + gg*100 + "\\% Gastos generales \\dotfill\\ "
       + precio_gg.EnHumano() + '\n'
     ppl_precio precio_bi(BIndustrial(precio_ejec_mat))
    os.write("\\item " + bi*100 + "\\% Beneficio industrial \\dotfill\\ "
       + precio_bi.EnHumano() + '\n'
     suma_gg_bi = precio_ejec_mat+precio_gg+precio_bi
    os.write("\\item Suma \\dotfill\\ "
       + suma_gg_bi.EnHumano() + '\n'
     ppl_precio precio_iva(IVA(suma_gg_bi))
    os.write("\\item " + iva*100 + "\\% I.V.A. \\dotfill\\ "
       + precio_iva.EnHumano() + '\n'
    os.write("\\end{itemize}" + '\n'
     total = suma_gg_bi + precio_iva
    os.write("\\textbf{Presupuesto de ejecución por contrata:} \\dotfill\\ \\textbf{ " + total.EnHumano() + '}' + '\n' + '\n' + '\n'
    os.write("\\vspace{0.5cm}" + '\n'
    os.write("Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: \\textsc{"
    os.write(total.EnLetra(False) + " euros}." + '\n'

