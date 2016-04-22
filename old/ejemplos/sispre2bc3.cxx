//xEntBC3.cxx

#include "../src/fiebdc3.h"
#include "../src/Obra.hxx"


int main(void)
  {
    Obra obr("PR","Prueba");
    obr.LeeSpre(cin);
    obr.EscribeBC3(cout);
    return 0;
  }
