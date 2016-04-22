//Porcentajes.cxx

#include "Porcentajes.h"

void Porcentajes::ImprLtx(std::ostream &os,const ppl_precio &precio_ejec_mat) const
{
    os << "\\begin{itemize}" << std::endl;
    os << "\\item Total presupuesto de ejecución material \\dotfill\\ "
       << precio_ejec_mat.EnHumano() << std::endl;
    const ppl_precio precio_gg(GGenerales(precio_ejec_mat));
    os << "\\item " << gg*100 << "\\% Gastos generales \\dotfill\\ "
       << precio_gg.EnHumano() << std::endl;
    const ppl_precio precio_bi(BIndustrial(precio_ejec_mat));
    os << "\\item " << bi*100 << "\\% Beneficio industrial \\dotfill\\ "
       << precio_bi.EnHumano() << std::endl;
    const ppl_precio suma_gg_bi= precio_ejec_mat+precio_gg+precio_bi;
    os << "\\item Suma \\dotfill\\ "
       << suma_gg_bi.EnHumano() << std::endl;
    const ppl_precio precio_iva(IVA(suma_gg_bi));
    os << "\\item " << iva*100 << "\\% I.V.A. \\dotfill\\ "
       << precio_iva.EnHumano() << std::endl;
    os << "\\end{itemize}" << std::endl;
    const ppl_precio total= suma_gg_bi + precio_iva;
    os << "\\textbf{Presupuesto de ejecución por contrata:} \\dotfill\\ \\textbf{ " << total.EnHumano() << '}' << std::endl << std::endl << std::endl;
    os << "\\vspace{0.5cm}" << std::endl;
    os << "Asciende el presente presupuesto de ejecución por contrata a la expresada cantidad de: \\textsc{";
    os << total.EnLetra(false) << " euros}." << std::endl;
}
