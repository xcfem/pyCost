//Mediciones.cxx

#include "Mediciones.h"

//! @brief Devuelve el total de unidades de la medición.
double Mediciones::TotalUnidades(void) const
{
    double t= 0.0;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades();
    return t;
}

//! @brief Devuelve el total del largo de la medición.
double Mediciones::TotalLargo(void) const
{
    double t= 0.0;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()*(*i).Largo();
    return t;
}

//! @brief Devuelve el total del ancho de la medición.
double Mediciones::TotalAncho(void) const
{
    double t= 0.0;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()*(*i).Ancho();
    return t;
}

//! @brief Devuelve el total del alto de la medición.
double Mediciones::TotalAlto(void) const
{
    double t= 0.0;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()*(*i).Ancho();
    return t;
}

long double Mediciones::Total(void) const
{
    long double t= 0.0;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        t+=(*i).Total();
    return t;
}
ppl_dimension Mediciones::TotalR(void) const
{
    ppl_dimension t= 0.0;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        t+=(*i).TotalR();
    return t;
}

//| @brief Lee la lista de mediciones.
void Mediciones::LeeBC3(const regBC3_lista_med &m)
{
    RegMedicion rm;
    for(regBC3_lista_med::const_iterator i= m.begin(); i!=m.end(); i++)
    {
        rm.LeeBC3(*i);
        push_back(rm);
    }
}

void Mediciones::EscribeBC3(std::ostream &os) const
{
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        (*i).EscribeBC3(os);
}
void Mediciones::ImprCompLtx(std::ostream &os,const Mediciones &otra) const
{
    const std::string linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg;
    const std::string media_linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd;
    dq_reg_med::const_iterator i=begin();
    dq_reg_med::const_iterator j=otra.begin();
    for(; ((i!=end()) && (j!=otra.end())); i++,j++)
    {
        (*j).ImprLtx(os,"p{1.5cm}");
        os << ltx_ampsnd;
        (*i).ImprLtx(os,"p{1.5cm}");
        os << ltx_fin_reg << std::endl;
    }
    if(i!=end())
        for(; i!=end(); i++)
        {
            os << media_linea_en_blanco;
            os << ltx_ampsnd;
            (*i).ImprLtx(os,"p{1.5cm}");
            os << ltx_fin_reg << std::endl;
        }
    else if(j!=end())
        for(; j!=otra.end(); j++)
        {
            (*j).ImprLtx(os,"p{1.5cm}");
            os << media_linea_en_blanco << ltx_fin_reg << std::endl;
        }
    os << linea_en_blanco << std::endl;
}
void Mediciones::ImprCompLtx(std::ostream &os) const
{
    const std::string linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg;
    const std::string media_linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd+ltx_ampsnd;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
    {
        os << media_linea_en_blanco;
        (*i).ImprLtx(os,"p{1.5cm}");
        os << ltx_fin_reg << std::endl;
    }
    os << linea_en_blanco << std::endl;
}
void Mediciones::ImprLtx(std::ostream &os) const
{
    const std::string linea_en_blanco= ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg;
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
    {
        (*i).ImprLtx(os,"p{3.5cm}");
        os << ltx_fin_reg << std::endl;
    }
    os << linea_en_blanco << std::endl;
}
void Mediciones::EscribeHCalc(std::ostream &os) const
{
    dq_reg_med::const_iterator i;
    for(i=begin(); i!=end(); i++)
        (*i).EscribeHCalc(os);
    os << ",,,,Suma ..." << tab << Total() << std::endl << std::endl;
}
