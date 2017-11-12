//ppl.cxx

#include "DatosPpl.hxx"
#include "ppl.h"

void compara(const Obra &o1, const Obra &o2,std::ostream &os)
  {
    os << ltx_input("cabecera") << std::endl;
    o2.ImprCompLtx(o1,os);
    os << ltx_end("document") << std::endl;
  }

int main(void)
  {

    Obra obr1("PR1","Construcc");
    ifstream strm_ppl1("sahechores/presu_sahech_base_ene.ppl");
    obr1.LeeCmd(strm_ppl1);

    Obra obr2("PR2","Modificado");
    ifstream strm_ppl2("modif/presu_sahech_ene_corrg.ppl");
    obr2.LeeCmd(strm_ppl2);

    ofstream strm_cmp("comparativo.tex");
    
    compara(obr1,obr2,strm_cmp);

    return 0;
  }
