#ListaJustPre.pyxx




import ListaRegJustPre
import basic_types

class ListaJustPre(EntCmd):
    bool porcentajes_acumulados
    ListaRegJustPre mano_de_obra
    ListaRegJustPre materiales
    ListaRegJustPre maquinaria
    ListaRegJustPre otros
    ListaRegJustPre porcentajes
public:
    ListaJustPre( bool &pa, &mano, &mater, &maqui, &otr, &porc)
    ppl_precio3 Base()
    ppl_precio3 Total()
    ppl_precio3 Redondeo()
    ppl_precio3 TotalRnd()
    ppl_precio2 TotalCP1()
    std.string StrPrecioLtx()
    std.string StrPrecioEnLetra( bool &genero)
    size_t size()
     ImprLtxJustPre(os)
     ImprLtxCP1(os, &genero)
     ImprLtxCP2(os)



#ListaJustPre.cc

import ListaJustPre
import bibXCBasica/src/texto/latex

ListaJustPre.ListaJustPre( bool &pa, &mano, &mater, &maqui, &otr, &porc)
    : porcentajes_acumulados(pa),mano_de_obra(mano), materiales(mater), maquinaria(maqui), otros(otr), porcentajes(porc)
    ppl_precio3 base(Base())
    if porcentajes_acumulados:
        porcentajes.SetBaseAcum(base)
    else:
        porcentajes.SetBase(base)


def Base(self, ):
    ppl_precio3 retval(mano_de_obra.Total())
    retval+= materiales.Total()
    retval+= maquinaria.Total()
    retval+= otros.Total()
    return retval


def Total(self, ):
    ppl_precio3 retval(Base())
    retval+= porcentajes.Total()
    return retval

def Redondeo(self, ):
    #return -Total().Redondeo()
    #XXX Redondeo para 2 decimales.
    tmp = Total()
    tmp*= 100.0
    ppl_precio3 rnd=tmp.Redondeo()
    rnd/=100
    return rnd

def TotalRnd(self, ):
    return Total() + Redondeo()

def TotalCP1(self, ):
    return ppl_precio2(double(TotalRnd()))

def StrPrecioLtx(self, ):
    return TotalCP1().EnHumano()

def StrPrecioEnLetra(self, &genero):
    return TotalCP1().EnLetra(genero)

def size(self, ):
    return mano_de_obra.size()+materiales.size()+maquinaria.size()+otros.size()+porcentajes.size()


def ImprLtxJustPre(self, &os):
    total = Total()
    rnd = Redondeo()
    total_rnd = TotalRnd()
    if size()<2:
        os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Sin descomposición"))
           + " & & " + ltx_fin_reg + '\n' + ltx_fin_reg + '\n'
        #Total
        os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","TOTAL")) + " & "
           + ltx_multicolumn(ltx_datos_multicolumn("2","r","\\textbf{"+total.EnHumano()+"}"))
           + ltx_fin_reg + '\n'

    else:
        mano_de_obra.ImprLtxJust(os)
        materiales.ImprLtxJust(os)
        maquinaria.ImprLtxJust(os)
        otros.ImprLtxJust(os)
        porcentajes.ImprLtxJust(os)
        #Suma
        os.write(ltx_fin_reg + '\n'
        os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Suma"+ltx_ldots)) + " & "
           + ltx_multicolumn(ltx_datos_multicolumn("2","r",total.EnHumano()))
           + ltx_fin_reg + '\n'
        #Redondeo
        os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","Redondeo"+ltx_ldots)) + " & "
           + ltx_multicolumn(ltx_datos_multicolumn("2","r",rnd.EnHumano()))
           + ltx_fin_reg + '\n'
        #Total
        os.write(ltx_multicolumn(ltx_datos_multicolumn("4","r","TOTAL")) + " & "
           + ltx_multicolumn(ltx_datos_multicolumn("2","r","\\textbf{"+total_rnd.EnHumano()+"}"))
           + ltx_fin_reg + '\n'


def ImprLtxCP2(self, &os):
    total = Total()
    rnd = Redondeo()
    total_rnd = TotalRnd()
    if size()<2:
        os.write(" & & " + "Sin descomposición"
           + " & " + ltx_fin_reg + '\n'
        #Total
        os.write(" & & " + ltx_textbf("TOTAL") + " & "
           + "\\textbf{"+total.EnHumano()+"}"
           + ltx_fin_reg + '\n'

    else:
        mano_de_obra.ImprLtxCP2(os)
        materiales.ImprLtxCP2(os)
        maquinaria.ImprLtxCP2(os)
        otros.ImprLtxCP2(os)
        porcentajes.ImprLtxCP2Porc(os)
        #Suma
        os.write(ltx_fin_reg + '\n'
        os.write(" & & " + "Suma" + ltx_ldots + " & "
           + total.EnHumano() + ltx_fin_reg + '\n'
        #Redondeo
        os.write(" & & " + "Redondeo" + ltx_ldots + " & "
           + rnd.EnHumano() + ltx_fin_reg + '\n'
        #Total
        os.write(ltx_cline("4-4") + '\n'
        os.write(" & & " + ltx_textbf("TOTAL") + " & "
           + "\\textbf{"+total_rnd.EnHumano()+"}"
           + ltx_fin_reg + '\n'



def ImprLtxCP1(self, &os, &genero):
    os.write(StrPrecioEnLetra(genero) + " & "
       + StrPrecioLtx()


