//ppl.cxx

#include "DatosPpl.hxx"
#include "ppl.h"


int main(void)
  {

    DatosPpl d_ppl("PR","Prueba");
    d_ppl.LeeCmd(std::cin);

    std::cerr << "Simulando descompuestos" << std::endl;


    std::string origen;
    std::string destino;
    std::string resto;

     ifstream is("claves.txt");
     while(is)
       {
         getline(is,destino,',');
         if(!is) break;
         getline(is,origen,',');
         if(!is) break;
         getline(is,resto,'\n');
         if(!is) break;
         d_ppl.SimulaDescomp(origen,destino);        
       }

//     ifstream is("claves_casares.txt");
//     while(is)
//       {
//         getline(is,destino,',');
//         if(!is) break;
//         getline(is,origen,',');
//         if(!is) break;
//         getline(is,resto,'\n');
//         if(!is) break;
//         d_ppl.SimulaDescomp(origen,destino);        
//       }

//     ifstream is2("claves_guadix.txt");
//     while(is2)
//       {
//         getline(is2,destino,',');
//         if(!is2) break;
//         getline(is2,origen,',');
//         if(!is2) break;
//         getline(is2,resto,'\n');
//         if(!is2) break;
//         d_ppl.SimulaDescomp(origen,destino);        
//       }

//     ifstream is3("claves_molinos.txt");
//     while(is3)
//       {
//         getline(is3,destino,',');
//         if(!is3) break;
//         getline(is3,origen,',');
//         if(!is3) break;
//         getline(is3,resto,'\n');
//         if(!is3) break;
//         d_ppl.SimulaDescomp(origen,destino);        
//       }

    ifstream temp("temp.ppl");
    d_ppl.LeeCmd(temp);


    return 0;
  }
