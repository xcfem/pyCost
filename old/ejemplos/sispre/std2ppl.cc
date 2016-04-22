#include "../ppl.h"

int main(void)
  {
    PPLProyecto proy;
    cin >> ignore_to(string("[MDO]"));cin.get(); //Para retorno carro
    PPLPrecioMdo prec_mdo;
    while(prec_mdo.LeeStd(cin))
      prec_mdo.EscribeBc3(cout);
    cin >> ignore_to(string("[MAQ]"));cin.get(); //Para retorno carro
    PPLPrecioMaq prec_maq;
    while(prec_maq.LeeStd(cin))
      prec_maq.EscribeBc3(cout);
    cin >> ignore_to(string("[MAT]"));cin.get(); //Para retorno carro
    PPLPrecioMat prec_mat;
    while(prec_mat.LeeStd(cin))
      prec_mat.EscribeBc3(cout);
    cin >> ignore_to(string("[DES]"));cin.get(); //Para retorno carro
    PPLPrecioCompuesto prec_cmp;
    while(prec_cmp.LeeStd(cin))
      prec_cmp.EscribeBc3(cout);

    /*
    cin >> ignore_to(string("[MED]"));cin.get(); //Para retorno carro
    PPLCapitulo cap;
    while(cap.LeeStd(cin))
      cap.EscribeBc3(cout);
    */
    proy.LeeStd(cin);
    proy.EscribeBc3(cout);
    return 0;
  }
