//xEntBC3.cxx

#include "../src/fiebdc3.h"
#include "../src/Obra.hxx"

CmdStatus::pila_streams CmdStatus::streams;
Buscadores CmdStatus::b;
CmdStatus::pila_llamadas CmdStatus::ruta;
CmdStatus::pila_archivos CmdStatus::archivos;
LexAlgebra &CmdStatus::lexico(ExprAlgebra::LexA());

int main(void)
  {
    Obra obr("PR","Prueba");
    obr.LeeSpre(std::cin);
    obr.EscribeBC3(std::cout);
    return 0;
  }
