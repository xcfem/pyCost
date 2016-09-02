#Porcentajes.py




import EntPyCost
import Tipos

class Porcentajes(EntPyCost):
    float gg; #Gastos generales.
    float bi; #Beneficio industrial.
    float iva; #Impuesto sobre el valor añadido.
    inline static ppl_precio AplicaPorcentaje( ppl_precio &p, &pc)
         ppl_porcentaje temp2(pc)
        ppl_precio temp3(p)
        temp3*=temp2
        return temp3

    inline ppl_precio GGenerales( ppl_precio &p)
        return AplicaPorcentaje(p,gg)

    inline ppl_precio BIndustrial( ppl_precio &p)
        return AplicaPorcentaje(p,bi)

    inline ppl_precio IVA( ppl_precio &p)
        return AplicaPorcentaje(p,iva)

public:
    Porcentajes( float &g= .17, &b=.06, i=.16)
        : gg(g), bi(b), iva(i) {
    void ImprLtx(std.ostream &os, &precio_ejec_mat)



#Porcentajes.cxx

import Porcentajes

def ImprLtx(self, &os, &precio_ejec_mat):
    os << "\\begin{itemize}" << std.endl
    os << "\\item Total presupuesto de ejecución material \\dotfill\\ "
       << precio_ejec_mat.EnHumano() << std.endl
     ppl_precio precio_gg(GGenerales(precio_ejec_mat))
    os << "\\item " << gg*100 << "\\% Gastos generales \\dotfill\\ "
       << precio_gg.EnHumano() << std.endl
     ppl_precio precio_bi(BIndustrial(precio_ejec_mat))
    os << "\\item " << bi*100 << "\\% Beneficio industrial \\dotfill\\ "
       << precio_bi.EnHumano() << std.endl
     suma_gg_bi = precio_ejec_mat+precio_gg+precio_bi
    os << "\\item Suma \\dotfill\\ "
       << suma_gg_bi.EnHumano() << std.endl
     ppl_precio precio_iva(IVA(suma_gg_bi))
    os << "\\item " << iva*100 << "\\% I.V.A. \\dotfill\\ "
       << precio_iva.EnHumano() << std.endl
    os << "\\end{itemize}" << std.endl
     total = suma_gg_bi + precio_iva
    os << "\\textbf{Presupuesto de ejecución por contrata:} \\dotfill\\ \\textbf{ " << total.EnHumano() << '}' << std.endl << std.endl << std.endl
    os << "\\vspace{0.5cm}" << std.endl
    os << "Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: \\textsc{"
    os << total.EnLetra(False) << " euros}." << std.endl

