#CodigosObra.cxx

#include "CodigosObra.h"

std.set<std.string> CodigosObra.codigos_capitulos

 Codigos &CodigosObra.GetDatosElementos(void)
    return elementos


 Codigos &CodigosObra.GetDatosUnidades(void)
    return udsobr


 Codigos CodigosObra.GetDatosObra(void)
    return caps.GetObra()


#not  @brief Devuelve los registros correspondientes a los capítulos
#not  de la obra.
 Codigos &CodigosObra.GetDatosCaps(void)
    return caps


#not  @brief Devuelve los códigos de los capítulos de la obra.
 std.set<std.string> &CodigosObra.GetCodigosCapitulos(void)
    return codigos_capitulos


#not  @brief Devuelve verdadero si existe el concepto cuyo código se pasa como parámetro.
def ExisteConcepto(self, &cod):
    if caps.find(cod) != caps.end():
        return True
    elif elementos.find(cod) != elementos.end():
        return True
    elif mediciones.find(cod) != mediciones.end():
        return True
    elif udsobr.find(cod) != udsobr.end():
        return True
    elif resto.find(cod) != resto.end():
        return True
    else:
        return False


#not  @brief Devuelve una cadena de caracteres que identifica la
#not  tabla en la que esta guardado el concepto.
def StrTablaConcepto(self, &cod):
    if caps.find(cod) != caps.end():
        return "capitulo"
    elif elementos.find(cod) != elementos.end():
        return "elementos"
    elif mediciones.find(cod) != mediciones.end():
        return "mediciones"
    elif udsobr.find(cod) != udsobr.end():
        return "descompuestos"
    elif resto.find(cod) != resto.end():
        return "resto"
    else:
        return "ninguna"


#@ brief Devuelve un iterador al concepto cuyo código se pasa como parámetro.
def BuscaConcepto(self, &cod):
    retval = caps.find(cod)
    if retval != caps.end():
        return retval
    elif (retval= elementos.find(cod)) != elementos.end():
        return retval
    elif (retval= mediciones.find(cod)) != mediciones.end():
        return retval
    elif (retval= udsobr.find(cod)) != udsobr.end():
        return retval
    else return resto.find(cod)


#@ brief Separa los registros según sean capítulos, mediciones, descompuestos, etc.
def Trocea(self, &verborrea):
    obra = resto.GetObra(); #Obtiene los registros que corresponden a la obra.
    caps.InsertaCods(obra)
    #resto.Borra(obra)
    caps+= resto.GetCapitulos()
    resto.Borra(caps)
    elementos= resto.GetElementos()
    resto.Borra(elementos)
    udsobr= resto.GetDescompuestos()
    resto.Borra(udsobr)
    if resto.size()>0:
        std.cerr << "Quedaron " << resto.size() << " conceptos sin importar" << std.endl
        if verborrea>4:
            std.cerr << resto << std.endl


    codigos_capitulos= caps.GetCodigos()


#@ brief Devuelve los datos del capítulo al que apunta el iterador.
def GetDatosCapitulo(self, &i):
    return caps.GetDatosCapitulo(i)


#not  @brief Carga las líneas de BC3 "resto" y después llama a la rutina "Trocea"
def LeeBC3(self, &is, &verborrea):
    reg = ""
    count = 0
    while(not is.eof())
        getline(is,reg,'~')
        count++
        if verborrea>6:
            std.clog << "Leyendo registro: " << count << std.endl
        reg= elimina_car(reg,char(13))
        reg= elimina_car(reg,'\n')
        if reg.length()>2:
             tipo = reg[0]
            if(tipo == 'M') #Las mediciones las insertamos directamente.
                mediciones.InsertaReg(reg,verborrea,count)
            else:
                resto.InsertaReg(reg,verborrea,count)


    std.clog << "  leídas " << mediciones.size() << " mediciones." << std.endl
    Trocea(verborrea)


#not  @brief Devuelve los registros de la descomposicion que corresponden a
#not  precios elementales.
def FiltraElementales(self, &descomp):
    return FiltraPrecios(descomp,elementos)


#not  @brief Devuelve los registros de la descomposicion que corresponden a
#not  precios descompuestos.
def FiltraDescompuestos(self, &descomp):
    return FiltraPrecios(descomp,udsobr)


#not  @brief Devuelve los registros de la descomposicion que corresponden a los
#not  precios que se pasan como parámetros.
def FiltraPrecios(self, &descomp, &precios):
    Codigos retval
    for(i = 0; i<descomp.size(); i++)
        p = precios.find(descomp[i].codigo)
        if( (p!=precios.end()) ) #Encontró el precio
            retval[(*p).first]= (*p).second

    return retval


#not  @brief Devuelve los registros correspondientes a mediciones.
 Codigos &CodigosObra.GetDatosMeds(void)
    return mediciones


def BorraElementales(self, &els):
    elementos.Borra(els)


def BorraDescompuestos(self, &uds):
    udsobr.Borra(uds)


std.ostream &operator<<(std.ostream &os, &co)
    os << "Obra: " << std.endl << co.GetDatosObra() << std.endl
       << "Capítulos: " << std.endl << co.caps << std.endl
       << "Elementos:" << std.endl << co.elementos << std.endl
       << "Descompuestos:" << std.endl << co.udsobr << std.endl
       << "Mediciones:" << std.endl << co.mediciones << std.endl
       << "Quedan: " << std.endl << co.resto << std.endl
    return os

