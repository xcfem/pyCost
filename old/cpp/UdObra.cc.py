#UdObra.cxx

#include "UdObra.h"
#include "bibXCBasica/src/texto/en_letra.h"

#not  @brief Para unidades de obra sin descomposición de las que
#not  sólo se conoce el precio.
def GetSindesco(self, &rendimiento, &bp):
    ComptesBC3 retval
    BuscadorPtros *be= bp["elementos"]
     EntBC3 &ent= *( Elemento *)be.Busca("SINDESCO")
    retval.push_back(CompBC3(ent,1.0,rendimiento))
    return retval


#not  @brief Obtiene los punteros a los precios de la descomposición.
def ObtienePunteros(self, &descBC3, &bp, &error):
    ComptesBC3 retval
    BuscadorPtros *be= bp["elementos"]
    BuscadorPtros *bd= bp["ud_obra"]
     EntBC3 *ent= NULL
    i = descBC3.begin()
    for(; i!=descBC3.end(); i++)
        ent= static_cast< EntBC3 *>(be.Busca((*i).codigo))
        if not ent:
            ent= static_cast< EntBC3 *>(bd.Busca((*i).codigo))
        if not ent:
            if(self.verbosityLevel>6) #Puede no ser un error.
                std.cerr << "UdObra.ObtienePunteros; No se encontró la componente: " << (*i).codigo << std.endl
            error= True
            continue

        else:
            retval.push_back(CompBC3(*ent,(*i).factor,(*i).rendimiento))
            error= False


    return retval

def LeeBC3Fase2(self, &r, &bp):
    error = False
    if r.Datos().desc.size():
        tmp = ObtienePunteros(r.Datos().desc,bp,error)
        if not error:
            lista= tmp
        else:
            std.cerr << "Error al leer descomposición de la unidad: " << Codigo() << std.endl

    else:
        lista= GetSindesco(r.Datos().Precio(),bp)
    return error


def EscribeSpre(self, &os):
    os << Codigo() << '|'
       << Unidad() << '|'
       << Titulo() << '|'
    lista.EscribeSpre(os)


def EscribeBC3(self, &os):
    Medible.EscribeBC3(os)
    lista.EscribeBC3(Codigo(),os)


#not  @brief Toma la descomposición de otra unidad de obra.
#not  sin alterar el precio de ésta.
long double UdObra.SimulaDescomp( UdObra &otra)
     long objetivo = Precio()
    lista= otra.lista
    return lista.FuerzaPrecio(objetivo)


def ImprLtxJustPre(self, &os):
    os << "\\begin{tabular}{l r l p{4cm} r r}" << std.endl
    #Cabecera
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ltx_multicolumn(ltx_datos_multicolumn("4","p{7cm}",ascii2latex(TextoLargo()))) << ltx_fin_reg << std.endl
    os << "Código & Rdto. & Ud. & Descripción & Unit. & Total"
       << ltx_fin_reg << std.endl << ltx_hline << std.endl
    #Descomposición
    lista.ImprLtxJustPre(os,True); #XXX Aqui porcentajes acumulados.
    os << "\\end{tabular}" << std.endl

def ImprLtxCP1(self, &os):
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(TextoLargo()) << " & "
    lista.ImprLtxCP1(os,True,False); #XXX Aqui género.
    os << "\\\\" << std.endl

def ImprLtxCP2(self, &os):
    os << "\\begin{tabular}{l r p{5.5cm} r}" << std.endl
    #Cabecera
    os << "Código & Ud. & Descripción & Importe"
       << ltx_fin_reg << std.endl << ltx_hline << std.endl
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(TextoLargo()) << " & " << ltx_fin_reg << std.endl << ltx_fin_reg << std.endl
    #Descomposición
    lista.ImprLtxCP2(os,True); #XXX Aqui porcentajes acumulados.
    os << "\\end{tabular}" << std.endl

def EscribeHCalc(self, &os):
    os << Codigo() << tab
       << ascii2latex(Unidad()) << tab
       << '"' << ascii2latex(TextoLargo()) << '"' << tab
       << '"' << StrPrecioEnLetra(True) << '"' << tab
       << StrPrecio() << std.endl


