#MedsCap.py
#Mediciones de un capítulo.




import Partida
import InformeMediciones
import bibXCBasica/src/stl/poli_deque
#import Pieza


class MedsCap(poli_deque<ProtoPartida>, EntPyCost):
    typedef poli_deque<ProtoPartida> dq_med
public:
    long double Precio()
    ppl_precio PrecioR()
    std.string StrPrecioLtx()
        return PrecioR().EnHumano()

     Write(os, &cod, &pos="")
     WriteDescompBC3(os, &cod)
     ImprCompLtxMed(os, &otra)
     ImprLtxMed(os)
     ImprCompLtxPre(os, &tit, &otra, &tit_otra)
     ImprLtxPre(os, &tit)
    #Imprime presupuestos parciales.
     WriteHCalcMed(os)
     WriteHCalcPre(os)
    InformeMediciones GetInformeMediciones()



#MedsCap.cxx

import MedsCap


long double MedsCap.Precio()
    long t = 0.0
    const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Precio()
    return t

def PrecioR(self, ):
    ppl_precio t(0.0)
    const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).PrecioR()
    return t

def Write(self, &os, &cod, &pos):
    const_iterator i
    contador = 1
    for(i=begin(); i!=end(); i++,contador++)
        pos_med = pos + num2str(contador,0) + '\\'
        (*i).WriteBC3(os,cod,pos_med)


def WriteDescompBC3(self, &os, &cod):
    if(size()<1) return
    os.write("~D" + '|' #Antes estaba con ~Y (daba problemas)
       + cod + '|'
    for(i = begin(); i!=end(); i++)
        os.write((*i).CodigoUdObra() + "\\1\\" #factor 1
           + (*i).Total() + '\\'
    os.write('|' + endl_msdos

def ImprCompLtxMed(self, &os, &otra):
    if size():
        os.write(ltx_tiny + '\n'
        os.write(ltx_begin("longtable}{lrrrrr|lrrrrr") + '\n'
           + "\\multicolumn{6}{c|}{\\normalsize\\textbf{Proyecto de construcción}\\tiny} &"
           + "\\multicolumn{6}{c}{\\normalsize\\textbf{Proyecto modificado}\\tiny} \\\\"
           + '\n' + ltx_hline + '\n'
           + ltx_endhead + '\n'
           + "\\multicolumn{12}{r}{../..}\\\\" + '\n'
           + ltx_endfoot + '\n'
           + ltx_endlastfoot + '\n'
        const_iterator i
        for(i=begin(); i!=end(); i++)
             cod = (*i).CodigoUdObra()
            const_iterator j
            for(j=otra.begin(); j!=otra.end(); j++)
                if(cod == (*j).CodigoUdObra()) break
            if(j!=otra.end()) #La encotró
                (*i).ImprCompLtxMed(os,*(*j))
            else:
                (*i).ImprCompLtxMed(os)

        os.write("\\end{longtable}" + '\n'
        os.write(ltx_normalsize + '\n'


def ImprLtxMed(self, &os):
    if size():
        os.write(ltx_small + '\n'
        os.write("\\begin{longtable}{lrrrrr}" + '\n'
           + "\\multicolumn{6}{r}{../..}\\\\" + '\n'
           + "\\endfoot" + '\n'
           + "\\endlastfoot" + '\n'
        const_iterator i
        for(i=begin(); i!=end(); i++)
            (*i).ImprLtxMed(os)
        os.write("\\end{longtable}" + '\n'
        os.write(ltx_normalsize + '\n'


def ImprCompLtxPre(self, &os, &tit, &otra, &tit_otra):
    if size():
        os.write(ltx_tiny + '\n'
        os.write(ltx_begin("longtable}{lrlrr|lrlrr") + '\n'
           + "\\multicolumn{5}{c|}{\\normalsize\\textbf{Proyecto de construcción}\\tiny} &"
           + "\\multicolumn{5}{c}{\\normalsize\\textbf{Proyecto modificado}\\tiny} \\\\"
           + '\n' + ltx_hline + '\n'
           + "Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{P. unitario} & Importe & Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{P. unitario} & Importe \\\\" + '\n'
           + ltx_hline + '\n'
           + ltx_endhead + '\n'
           + "\\multicolumn{10}{r}{../..}\\\\" + '\n'
           + ltx_endfoot + '\n'
           + ltx_endlastfoot + '\n'
        const_iterator i
        for(i=begin(); i!=end(); i++)
             cod = (*i).CodigoUdObra()
            const_iterator j
            for(j=otra.begin(); j!=otra.end(); j++)
                if(cod == (*j).CodigoUdObra()) break
            if(j!=otra.end()) #La encotró
                (*i).ImprCompLtxPre(os,*(*j))
            else:
                (*i).ImprCompLtxPre(os)

        os.write("\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
           + tit_otra + "}} & \\textbf{" + otra.StrPrecioLtx() + "} & " + '\n'
        os.write("\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
           + tit + "}} & \\textbf{" + StrPrecioLtx() + "}\\\\" + '\n'
        os.write("\\end{longtable}" + '\n'
        os.write(ltx_normalsize + '\n'


def ImprLtxPre(self, &os, &tit):
#Imprime presupuestos parciales.
    if size():
        os.write(ltx_small + '\n'
        os.write("\\begin{longtable}{lrlrr}" + '\n'
           + "Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{Precio unitario} & Importe \\\\" + '\n'
           + "\\hline" + '\n'
           + "\\endhead" + '\n'
           + "\\multicolumn{5}{r}{../..}\\\\" + '\n'
           + "\\endfoot" + '\n'
           + "\\endlastfoot" + '\n'
        for(const_iterator i=begin(); i!=end(); i++)
            (*i).ImprLtxPre(os)
        os.write("\\multicolumn{4}{p{8cm}}{\\textbf{Total: " + tit + "}} & \\textbf{" + StrPrecioLtx() + "}\\\\" + '\n'
        os.write("\\end{longtable}" + '\n'
        os.write(ltx_normalsize + '\n'


def WriteHCalcMed(self, &os):
    if size():
        const_iterator i
        for(i=begin(); i!=end(); i++)
            (*i).WriteHCalcMed(os)


def WriteHCalcPre(self, &os):
    if size():
        const_iterator i
        for(i=begin(); i!=end(); i++)
            (*i).WriteHCalcPre(os)



def GetInformeMediciones(self, ):
    InformeMediciones retval
    for(i = begin(); i!=end(); i++)
        retval.Inserta((*i).Informe())
    return retval

