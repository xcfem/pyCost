//xEntBC3.cxx

#include "../fiebdc3.h"

int main(void)
  {
    regBC3_m m("1\\2\\3\\4\\5\\|2|\\cubierta\\0\\2\\0\\0\\\\cub2\\0\\2\\0\\0\\|");
    cout << "********* Registro tipo Medición: " << endl;
    m.Escribe(cout);
    cout <<  "******** Registro tipo Descompuesto: " << endl;
    regBC3_d d("SINDESCO\\1\\3713\\|");
    d.Escribe(cout);
    cout  << "******** Registro tipo Concepto: " << endl;
    regBC3_c c("tm|Mezcla bituminosa en caliente tipo D-12, con  rido of¡tico, incluida su puesta en obra, extendido y compactaci¢n. |3648|040400|0|");
    c.Escribe(cout);
    cout  << "******** Registro tipo Texto: " << endl;
    regBC3_t t("Mezcla bituminosa en caliente tipo D-12, con  rido of¡tico, incluida su puesta en obra, extendido y compactaci¢n. |");
    t.Escribe(cout);
    return 0;
  }
