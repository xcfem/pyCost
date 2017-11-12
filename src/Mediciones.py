#Mediciones.py



import RegMedicion

#not  @brief Mediciones de una unidad de obra
class Mediciones(std.deque<RegMedicion>, EntPyCost):
public:
    typedef std.deque<RegMedicion> dq_reg_med

    double TotalUnidades()
    double TotalLargo()
    double TotalAncho()
    double TotalAlto()
    long double Total()
    ppl_dimension TotalR()

     LeeBC3( regBC3_lista_med &m)
     WriteBC3(os)
     ImprCompLtx(os, otra)
     ImprCompLtx(os)
     ImprLtx(os)
     WriteHCalc(os)



#Mediciones.cxx

import Mediciones

#not  @brief Devuelve el total de unidades de la medición.
def TotalUnidades(self):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        t+=(i).Unidades()
    return t


#not  @brief Devuelve el total del largo de la medición.
def TotalLargo(self):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        t+=(i).Unidades()*(i).Largo()
    return t


#not  @brief Devuelve el total del an.pyo de la medición.
def TotalAncho(self):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        t+=(i).Unidades()*(i).Ancho()
    return t


#not  @brief Devuelve el total del alto de la medición.
def TotalAlto(self):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        t+=(i).Unidades()*(i).Ancho()
    return t


long double Mediciones.Total()
    long t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        t+=(i).Total()
    return t

def TotalR(self):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        t+=(i).TotalR()
    return t


#| @brief Lee la lista de mediciones.
def LeeBC3(self, m):
    RegMedicion rm
    for(i = m.begin(); i!=m.end(); i+= 1)
        rm.LeeBC3(i)
        append(rm)



def WriteBC3(self, os):
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        (i).WriteBC3(os)

def ImprCompLtx(self, os, otra):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd
    dq_reg_med.const_iterator i=begin()
    dq_reg_med.const_iterator j=otra.begin()
    for(; ((i!=end()) and (j!=otra.end())); i+= 1,j+= 1)
        (j).ImprLtx(os,"p{1.5cm}")
        os.write(ltx_ampsnd
        (i).ImprLtx(os,"p{1.5cm}")
        os.write(ltx_fin_reg + '\n'

    if i!=end():
        for(; i!=end(); i+= 1)
            os.write(media_linea_en_blanco
            os.write(ltx_ampsnd
            (i).ImprLtx(os,"p{1.5cm}")
            os.write(ltx_fin_reg + '\n'

    elif j!=end():
        for(; j!=otra.end(); j+= 1)
            (j).ImprLtx(os,"p{1.5cm}")
            os.write(media_linea_en_blanco + ltx_fin_reg + '\n'

    os.write(linea_en_blanco + '\n'

def ImprCompLtx(self, os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        os.write(media_linea_en_blanco
        (i).ImprLtx(os,"p{1.5cm}")
        os.write(ltx_fin_reg + '\n'

    os.write(linea_en_blanco + '\n'

def ImprLtx(self, os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        (i).ImprLtx(os,"p{3.5cm}")
        os.write(ltx_fin_reg + '\n'

    os.write(linea_en_blanco + '\n'

def WriteHCalc(self, os):
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i+= 1)
        (i).WriteHCalc(os)
    os.write(",,,,Suma ..." + tab + Total() + '\n' + '\n'

