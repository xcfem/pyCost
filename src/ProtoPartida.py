#ProtoPartida.py
#Algo capaz de devolver mediciones de una unidad de obra.




import InformeUdObra
import Mediciones
import basic_types

class ProtoPartida (EntPyCost):
     Measurable *ud
     WriteBC3RegM(os, cap_padre="", pos="")
public:
    ProtoPartida():ud(None) {
    ProtoPartida( Measurable &u):ud(&u) {
    inline virtual ~ProtoPartida() {
    virtual ProtoPartida *Copia() const= 0; #Constructor virtual.
     std.string CodigoUdObra()
        return ud.Codigo()

     std.string UnidadMedida()
        return ud.Unidad()

     std.string TextoLUdObra()
        return ud.TextoLargo()

    long double PrecioUd()
        return ud.Precio()

    ppl_precio PrecioRUd()
        return ud.PrecioR()

    virtual long double Total() const= 0
    virtual ppl_dimension TotalR() const= 0
    InformeUdObra Informe()
        return InformeUdObra(ud,Total())

    std.string StrPrecioUd()
        return ud.StrPrecio()

    std.string StrPrecioLtxUd()
        return ud.StrPrecioLtx()

    long double Precio()
        return Total()*PrecioUd()

    ppl_precio PrecioR()
        return ppl_precio(double(TotalR())*double(PrecioRUd()))

    std.string StrPrecioLtx()
        return PrecioR().EnHumano()

    virtual Mediciones Meds() const= 0
    def WriteBC3(os, cap_padre="", pos=""):
    #Latex.
     ImprLtxCabecera(os, totalr, ancho)
    static  ImprLtxLeyenda(os)
    static  ImprLtxPie(os, totalr)
     ImprCompLtxMed(os, otra)
     ImprCompLtxMed(os)
     ImprLtxMed(os)
     ImprLtxCabeceraPre(os, totalr, ancho)
     ImprCompLtxPre(os, otra)
     ImprCompLtxPre(os)
     ImprLtxPre(os)
     WriteHCalcMed(os)
     WriteHCalcPre(os)



#ProtoPartida.cxx

import ProtoPartida
import Obra

#not  @brief Imprime la cabecera para la partida.
def ImprLtxCabecera(self, os, totalr, ancho):
    os.write(ascii2latex(CodigoUdObra()) + ltx_ampsnd
       + totalr + ' ' + ascii2latex(UnidadMedida()) + ltx_ampsnd
       + ltx_multicolumn(ltx_datos_multicolumn("4",ancho,ascii2latex(TextoLUdObra())))


#not  @brief Imprime la partida.
def ImprCompLtxMed(self, os, otra):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
    os.write(linea_en_blanco + '\n'
     totalr_otra = otra.TotalR().EnHumano()
    otra.ImprLtxCabecera(os,totalr_otra,"p{4.5cm}|")
    os.write(ltx_ampsnd
     totalr_esta = TotalR().EnHumano()
    ImprLtxCabecera(os,totalr_esta,"p{4.5cm}")
    os.write(ltx_fin_reg + '\n'
    ImprLtxLeyenda(os)
    os.write(ltx_ampsnd
    ImprLtxLeyenda(os)
    os.write(ltx_fin_reg + '\n'
       + ltx_hline + '\n'
    Meds().ImprCompLtx(os,otra.Meds())
    ImprLtxPie(os,totalr_otra)
    os.write(ltx_ampsnd
    ImprLtxPie(os,totalr_esta)
    os.write(ltx_fin_reg + '\n'
    os.write(ltx_hline + '\n'
    os.write(linea_en_blanco + '\n'


#not  @brief Imprime la partida.
def ImprCompLtxMed(self, os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
    os.write(linea_en_blanco + '\n'
    os.write(media_linea_en_blanco
     totalr = TotalR().EnHumano()
    ImprLtxCabecera(os,totalr,"p{4.5cm}")
    os.write(ltx_fin_reg + '\n'
    #ImprLtxLeyenda(os)
    #os.write(ltx_ampsnd
    os.write(media_linea_en_blanco
    ImprLtxLeyenda(os)
    os.write(ltx_fin_reg + '\n'
       + ltx_hline + '\n'
    Meds().ImprCompLtx(os)
    os.write(media_linea_en_blanco
    ImprLtxPie(os,totalr)
    os.write(ltx_fin_reg + '\n'
    os.write(ltx_hline + '\n'
    os.write(linea_en_blanco + '\n'


def ImprLtxCabeceraPre(self, os, totalr, ancho):
    os.write(ascii2latex(CodigoUdObra()) + ltx_ampsnd
       + totalr + " " + ascii2latex(UnidadMedida()) + ltx_ampsnd
       + ltx_multicolumn(ltx_datos_multicolumn("1",ancho,ascii2latex(TextoLUdObra())))

def ImprCompLtxPre(self, os, otra):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
    os.write(linea_en_blanco + '\n'
     totalr_otra = otra.TotalR().EnHumano()
    otra.ImprLtxCabeceraPre(os,totalr_otra,"p{2.5cm}")
    os.write(ltx_ampsnd
       + otra.StrPrecioLtxUd() + ltx_ampsnd
       + otra.StrPrecioLtx() + ltx_ampsnd
     totalr_esta = TotalR().EnHumano()
    ImprLtxCabeceraPre(os,totalr_esta,"p{2.5cm}")
    os.write(ltx_ampsnd
       + StrPrecioLtxUd() + ltx_ampsnd
       + StrPrecioLtx() + ltx_fin_reg + '\n'
    os.write(linea_en_blanco + '\n'

def ImprCompLtxPre(self, os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
    os.write(linea_en_blanco + '\n'
    os.write(media_linea_en_blanco
     totalr_med = TotalR().EnHumano()
    ImprLtxCabeceraPre(os,totalr_med,"p{2.5cm}")
    os.write(ltx_ampsnd
       + StrPrecioLtxUd() + ltx_ampsnd
       + StrPrecioLtx() + ltx_fin_reg + '\n'
    os.write(linea_en_blanco + '\n'

def ImprLtxPre(self, os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     totalr_med = TotalR().EnHumano()
    ImprLtxCabeceraPre(os,totalr_med,"p{5cm}")
    os.write(ltx_ampsnd
       + StrPrecioLtxUd() + ltx_ampsnd
       + StrPrecioLtx() + ltx_fin_reg + '\n'
    os.write(linea_en_blanco + '\n'

#HCalc
def WriteHCalcMed(self, os):
    os.write(CodigoUdObra() + tab
       + en_humano(Total(),3) + tab + ascii2latex(UnidadMedida()) + tab
       + '"' + ascii2latex(TextoLUdObra()) + '"' + '\n'
       + "Texto" + tab
       + "Unidades" + tab
       + "Largo" + tab
       + "Ancho" + tab
       + "Alto" + tab
       + "Parcial" + '\n'
    Meds().WriteHCalc(os)

def WriteHCalcPre(self, os):
    os.write(CodigoUdObra() + tab
       + Total() + tab + UnidadMedida() + tab + TextoLUdObra() + tab
       + StrPrecioUd() + tab
       + Precio() + '\n'


def WriteBC3RegM(self, os, cap_padre, pos):
    os.write("~M|" + cap_padre + '\\' + CodigoUdObra() + '|'
       + pos.write('|'
       + Total() + '|'


def WriteBC3(self, os, cap_padre, pos):
    WriteBC3RegM(os,cap_padre,pos)
    Meds().WriteBC3(os)
    os.write('|' + endl_msdos


def ImprLtxLeyenda(self, os):
    os.write("Texto" + ltx_ampsnd
       + "Unidades" + ltx_ampsnd
       + "Largo" + ltx_ampsnd
       + "Ancho" + ltx_ampsnd
       + "Alto" + ltx_ampsnd
       + "Parcial"


def ImprLtxPie(self, os, totalr):
    os.write(ltx_multicolumn(ltx_datos_multicolumn("5","r","Suma "+ ltx_ldots)) + ltx_ampsnd
       + ltx_textbf(totalr)


def ImprLtxMed(self, os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
    os.write(linea_en_blanco + '\n'
     totalr = TotalR().EnHumano()
    ImprLtxCabecera(os,totalr,"p{6cm}")
    os.write(ltx_fin_reg + '\n'
    ImprLtxLeyenda(os)
    os.write(ltx_fin_reg + '\n'
       + ltx_hline + '\n'
    Meds().ImprLtx(os)
    ImprLtxPie(os,totalr)
    os.write(ltx_fin_reg + '\n'
    os.write(ltx_hline + '\n'
    os.write(linea_en_blanco + '\n'


