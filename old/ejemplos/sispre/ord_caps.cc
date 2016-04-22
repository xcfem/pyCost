#include "../ppl.h"
#include "streams/omanip.h"

void procesa_titulo(istream &is)
  {
    int vacio= 0;
    char linea_titulo[128];
    cin.getline(linea_titulo,sizeof(linea_titulo),char(13));cin.get(); //Para retorno de carro.
    char linea_orden[128];
    cin.getline(linea_orden,sizeof(linea_titulo),'|');
    if(char(cin.peek()) == '|') vacio= 1;
    cout << linea_orden << '|' << linea_titulo << endl_msdos;
    if(vacio)
      {
        cin >> ignore_to(char(26));
        cin.putback(char(26));
      }
    else
      cout << linea_orden << '|';
  }

int main(void)
  {
    procesa_titulo(cin);
    while(cin.ipfx(1))
      {
        int c= cin.get();
        cout << char(c);
        if(c==26)
          {
            cout << endl_msdos;
            cin.get(); cin.get(); //Retorno de carro.
            procesa_titulo(cin);
          }
      }
    return 0;
  }
