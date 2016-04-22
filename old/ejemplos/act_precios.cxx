//actualiza_precios.cxx

#include "../fiebdc3.h"

int main(void)
  {
    Obra obr("PR","Prueba");
    obr.LeeSpre(cin);
    obr.CuadroPrecios().AsignaFactor(1.25);
    //obr.EscribeBC3(cout);
    obr.EscribeSpre();
    return 0;
  }
