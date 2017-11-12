#UdObra.py



import Elementos
import ComptesBC3

class UdObra(Measurable):
private:
    ComptesBC3 lista
    static ComptesBC3 ObtienePunteros( regBC3_d &descBC3, &bp, &error)
    ComptesBC3 GetSindesco( double &rendimiento, &bp)
public:
    UdObra( cod="", &tit="", &ud="")
        : Measurable(cod,tit,ud) {
    def tipo_concepto Tipo():
        return mat;    #XXX provisional.

    def Precio():
        return lista.Precio()

     AsignaFactor( float &f)
        lista.AsignaFactor(f)

     Agrega( Elemento &e, &f, &r)
        lista.append(CompBC3(e,f,r))

    #not  @brief Lee la unidad a falta de la descomposición
     LeeBC3Fase1( Codigos.reg_udobra &r)
        Measurable.LeeBC3(r)

    bool LeeBC3Fase2( Codigos.reg_udobra &r, &bp)
     WriteSpre(os)
     WriteBC3(os)
     ImprLtxJustPre(os)
     ImprLtxCP1(os)
     ImprLtxCP2(os)
     WriteHCalc(os)
    long double SimulaDescomp( UdObra &otra)



#UdObra.cxx

import UdObra
import bibXCBasica/src/texto/en_letra

#not  @brief Para unidades de obra sin descomposición de las que
#not  sólo se conoce el precio.
def GetSindesco(self, &rendimiento, &bp):
    ComptesBC3 retval
    BuscadorPtros *be= bp["elementos"]
     EntBC3 &ent= *( Elemento *)be.Busca("SINDESCO")
    retval.append(CompBC3(ent,1.0,rendimiento))
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
            if(verborrea>6) #Puede no ser un error.
                std.cerr + "UdObra.ObtienePunteros; No se encontró la componente: " + (*i).codigo + '\n'
            error= True
            continue

        else:
            retval.append(CompBC3(*ent,(*i).factor,(*i).rendimiento))
            error= False


    return retval

def LeeBC3Fase2(self, &r, &bp):
    error = False
    if r.Datos().desc.size():
        tmp = ObtienePunteros(r.Datos().desc,bp,error)
        if not error:
            lista= tmp
        else:
            std.cerr + "Error al leer descomposición de la unidad: " + Codigo() + '\n'

    else:
        lista= GetSindesco(r.Datos().Precio(),bp)
    return error


def WriteSpre(self, &os):
    os.write(Codigo() + '|'
       + Unidad() + '|'
       + Titulo() + '|'
    lista.WriteSpre(os)


def WriteBC3(self, &os):
    Measurable.WriteBC3(os)
    lista.WriteBC3(Codigo(),os)


#not  @brief Toma la descomposición de otra unidad de obra.
#not  sin alterar el precio de ésta.
long double UdObra.SimulaDescomp( UdObra &otra)
     long objetivo = Precio()
    lista= otra.lista
    return lista.FuerzaPrecio(objetivo)


def ImprLtxJustPre(self, &os):
    os.write("\\begin{tabular}{l r l p{4cm} r r}" + '\n'
    #Cabecera
    os.write(ascii2latex(Codigo()) + " & "
       + ascii2latex(Unidad()) + " & "
       + ltx_multicolumn(ltx_datos_multicolumn("4","p{7cm}",ascii2latex(TextoLargo()))) + ltx_fin_reg + '\n'
    os.write("Código & Rdto. & Ud. & Descripción & Unit. & Total"
       + ltx_fin_reg + '\n' + ltx_hline + '\n'
    #Descomposición
    lista.ImprLtxJustPre(os,True); #XXX Aqui porcentajes acumulados.
    os.write("\\end{tabular}" + '\n'

def ImprLtxCP1(self, &os):
    os.write(ascii2latex(Codigo()) + " & "
       + ascii2latex(Unidad()) + " & "
       + ascii2latex(TextoLargo()) + " & "
    lista.ImprLtxCP1(os,True,False); #XXX Aqui género.
    os.write("\\\\" + '\n'

def ImprLtxCP2(self, &os):
    os.write("\\begin{tabular}{l r p{5.5cm} r}" + '\n'
    #Cabecera
    os.write("Código & Ud. & Descripción & Importe"
       + ltx_fin_reg + '\n' + ltx_hline + '\n'
    os.write(ascii2latex(Codigo()) + " & "
       + ascii2latex(Unidad()) + " & "
       + ascii2latex(TextoLargo()) + " & " + ltx_fin_reg + '\n' + ltx_fin_reg + '\n'
    #Descomposición
    lista.ImprLtxCP2(os,True); #XXX Aqui porcentajes acumulados.
    os.write("\\end{tabular}" + '\n'

def WriteHCalc(self, &os):
    os.write(Codigo() + tab
       + ascii2latex(Unidad()) + tab
       + '"' + ascii2latex(TextoLargo()) + '"' + tab
       + '"' + StrPrecioEnLetra(True) + '"' + tab
       + StrPrecio() + '\n'


