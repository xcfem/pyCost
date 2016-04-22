//xEntBC3.cxx

#include "../fiebdc3.h"


int main(void)
  {
    EntBC3 e("cod","tit");
    e.EscribeConceptoBC3(cout);
    CompBC3 c(e,1.0,2.0);
    c.EscribeBC3(cout); 
    cout << endl;
    CompuestoBC3 cmp("cod","tit");
    cmp.Agrega(c);
    cmp.Agrega(c);
    cmp.Agrega(c);
    cmp.EscribeBC3(cout);
    Medible m("cod","tit","m2");
    m.EscribeConceptoBC3(cout);
    cout << endl;
    Elemento alb("O00001","Peón de albañil","h.",1200);
    alb.EscribeConceptoBC3(cout);
    Elemento lad("P00001","Ladrillo hueco","Ud",13);
    lad.EscribeConceptoBC3(cout);
    Elemento mor("P00002","Mortero de cemento","M3",7000);
    mor.EscribeConceptoBC3(cout);
    UdObra tab("E04001","Tabique de ladrillo hueco","M2");
    tab.Agrega(alb,1,1.5);
    tab.Agrega(lad,1,68);
    tab.Agrega(mor,1,0.03);
    tab.EscribeBC3(cout);
    cout << endl << endl << endl;

    RegMedicion rm("En cocina",2,1,2,3);
    MedUdObra muo(tab);
    muo.Agrega(rm);
    muo.Agrega(rm);
    //muo.EscribeBC3(cout);
    Capitulo cap41("C0401","Tabiques");
    cap41.Agrega(muo);
    cap41.Agrega(muo);
    //cap41.EscribeBC3(cout);
    Capitulo cap42("C0402","Otros");
    cap42.Agrega(cap41);
    //cap42.EscribeBC3(cout);
    Capitulo cap4("C04","Albañileria");
    cap4.Agrega(cap41);
    cap4.Agrega(cap42);
    cap4.EscribeBC3(cout);
    cout << cap4.BuscaSubcapitulo("2\\1")->Codigo() << endl;

    return 0;
  }
