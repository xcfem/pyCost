//ppl_imprime.cxx

#include "../src/Obra.hxx"
#include "texto/tab_cod.hxx"

int main(void)
  {
    Obra obr;
    obr.LeeBC3(cin);
    obr.EscribeHCalc(cout);
    return 0;
  }
