//prueba_geom.cxx

#include "Pieza.hxx"
#include "matemat/geom/Cubo.h"

CmdStatus::pila_streams CmdStatus::streams;
Buscadores CmdStatus::b;
CmdStatus::pila_llamadas CmdStatus::ruta;
CmdStatus::pila_archivos CmdStatus::archivos;
LexAlgebra &CmdStatus::lexico(ExprAlgebra::LexA());

int main(void)
  {
    Cubo c;
    CmdStatus status;
    c.LeeCmd(status);
    std::cout << c.Volumen() << std::endl;
    return 0;
  }
