//ppl.cxx

#include "../src/DatosPpl.h"
#include "../src/ppl.h"
#include "bibXCLcmd/src/base/CmdStatus.h"

//CmdStatus::pila_streams CmdStatus::streams;
//Buscadores CmdStatus::b;
//CmdStatus::pila_llamadas CmdStatus::ruta;
//CmdStatus::pila_archivos CmdStatus::archivos;
//LexAlgebra &CmdStatus::lexico(ExprAlgebra::LexA());

int main(void)
  {
    CmdStatus s;
    DatosPpl d_ppl("PR","Prueba");

    d_ppl.LeeCmd(s);
    return 0;
  }
