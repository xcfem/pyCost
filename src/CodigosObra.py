#CodigosObra.py




import Codigos

class CodigosObra
    Codigos caps; #capitulos.
    Codigos elementos
    Codigos mediciones
    Codigos udsobr
    Codigos resto
    static std.set<std.string> codigos_capitulos
     Trocea( int &verborrea)
public:
    CodigosObra() {
    bool ExisteConcepto( cod)
    std.string StrTablaConcepto( cod)
    Codigos.const_iterator BuscaConcepto( cod)

     Codigos &GetDatosElementos()
     Codigos &GetDatosUnidades()
     Codigos GetDatosObra()
     Codigos &GetDatosCaps()
     std.set<std.string> &GetCodigosCapitulos()

    Codigos.reg_capitulo GetDatosCapitulo( Codigos.mapa.const_iterator &i)
    Codigos FiltraPrecios( regBC3_d &descomp, &precios)
    Codigos FiltraElementales( regBC3_d &descomp)
    Codigos FiltraDescompuestos( regBC3_d &descomp)

     Codigos &GetDatosMeds()
     BorraElementales( Codigos &els)
     BorraDescompuestos( Codigos &uds)
     LeeBC3(std.istream &is, &verborrea= 0)

    friend operator<<(os, &co)



#CodigosObra.cxx

import CodigosObra

std.set<std.string> CodigosObra.codigos_capitulos

 Codigos &CodigosObra.GetDatosElementos()
    return elementos


 Codigos &CodigosObra.GetDatosUnidades()
    return udsobr


 Codigos CodigosObra.GetDatosObra()
    return caps.GetObra()


#not  @brief Devuelve los registros correspondientes a los capítulos
#not  de la obra.
 Codigos &CodigosObra.GetDatosCaps()
    return caps


#not  @brief Devuelve los códigos de los capítulos de la obra.
 std.set<std.string> &CodigosObra.GetCodigosCapitulos()
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
        std.cerr + "Quedaron " + resto.size() + " conceptos sin importar" + '\n'
        if verborrea>4:
            std.cerr + resto + '\n'


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
            std.clog + "Leyendo registro: " + count + '\n'
        reg= elimina_car(reg,char(13))
        reg= elimina_car(reg,'\n')
        if len(reg)>2:
             tipo = reg[0]
            if(tipo == 'M') #Las mediciones las insertamos directamente.
                mediciones.InsertaReg(reg,verborrea,count)
            else:
                resto.InsertaReg(reg,verborrea,count)


    std.clog + "  leídas " + mediciones.size() + " mediciones." + '\n'
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
 Codigos &CodigosObra.GetDatosMeds()
    return mediciones


def BorraElementales(self, &els):
    elementos.Borra(els)


def BorraDescompuestos(self, &uds):
    udsobr.Borra(uds)


operator<<(os, &co)
    os.write("Obra: " + '\n' + co.GetDatosObra() + '\n'
       + "Capítulos: " + '\n' + co.caps + '\n'
       + "Elementos:" + '\n' + co.elementos.write('\n'
       + "Descompuestos:" + '\n' + co.udsobr + '\n'
       + "Mediciones:" + '\n' + co.mediciones + '\n'
       + "Quedan: " + '\n' + co.resto + '\n'
    return os

