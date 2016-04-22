//Capitulo.h

#ifndef CAPITULO_H
#define CAPITULO_H

#include "MedsCap.h"
#include "EntFR.h"
#include "Subcapitulos.h"
#include "CuaPre.h"


class Capitulo: public EntBC3
{
private:
    EntFR fr;
    MedsCap mediciones;
protected:
    CuaPre precios; //Para precios elementales y descompuestos clasificados por capítulos.
    Subcapitulos subcapitulos;

    friend class Subcapitulos;
    void LeeBC3Elementales(const Codigos &elementos);
    void LeeBC3DescompFase1(const Codigos &descompuestos);
    Descompuestos::set_pendientes LeeBC3DescompFase2(const Codigos &descompuestos);

public:
    Capitulo(const std::string &cod= "CapSinCod",const std::string &tit= "CapSinTit",
             const float &factor= 1.0,const float &rendimiento= 1.0);
    Capitulo(const Capitulo &otro);
    Capitulo &operator=(const Capitulo &otro);

    virtual std::string CodigoBC3(void) const;
    const CuaPre &CuadroPrecios(void) const;
    CuaPre &CuadroPrecios(void);

    void AgregaPartida(const Partida &m);
    CompBC3 GetCompBC3(void) const;

    Capitulo *BuscaSubcapitulo(regBC3_ruta &ruta);
    Capitulo *BuscaSubcapitulo(const std::string &lst);
    const Capitulo *BuscaCodigo(const std::string &mnb) const;
    Capitulo *BuscaCodigo(const std::string &mnb);
    inline bool TieneElementales(void) const
    {
        return precios.TieneElementales();
    }
    size_t NumDescompuestos(void) const
    {
        return precios.NumDescompuestos()+subcapitulos.NumDescompuestos();
    }
    inline bool TieneDescompuestos(void) const
    {
        return NumDescompuestos()> 0;
    }
    inline BuscadorDescompuestos GetBuscadorDescompuestos(void)
    {
        return precios.GetBuscadorDescompuestos();
    }
    const Medible *BuscaPrecio(const std::string &cod) const;

    const Subcapitulos &getSubcapitulos(void) const
    {
        return subcapitulos;
    }
    Subcapitulos &getSubcapitulos(void)
    {
        return subcapitulos;
    }
    const MedsCap &getMediciones(void) const
    {
        return mediciones;
    }
    MedsCap &getMediciones(void)
    {
        return mediciones;
    }

    virtual long double Precio(void) const;
    virtual ppl_precio PrecioR(void) const;

    void EscribeMediciones(std::ostream &os,const std::string &pos="") const
    {
        mediciones.Escribe(os,CodigoBC3(),pos);
    }
    void EscribeSubCapitulos(std::ostream &os,bool primero= "false",const std::string &pos="") const
    {
        subcapitulos.EscribeBC3(os,primero,pos);
    }
    void EscribePreciosBC3(std::ostream &os) const;
    void EscribeDescompBC3(std::ostream &os) const;
    void EscribeBC3(std::ostream &os,bool primero=false,const std::string pos="") const;

    static std::string SectionLtx(const std::string &sect);
    void ImprCompLtxMed(std::ostream &os,const std::string &sect,const Capitulo &otro) const;
    void ImprLtxMed(std::ostream &os,const std::string &sect) const;
    void ImprLtxCP1(std::ostream &os,const std::string &sect) const;
    void ImprLtxCP2(std::ostream &os,const std::string &sect) const;
    void ImprLtxJustPre(std::ostream &os,const std::string &sect) const;
    void ImprLtxResumen(std::ostream &os,const std::string &sect,bool recurre= true) const;
    void ImprCompLtxPre(std::ostream &os,const std::string &sect,const Capitulo &otro) const;
    void ImprLtxPre(std::ostream &os,const std::string &sect) const;
    void EscribeHCalcMed(std::ostream &os,const std::string &sect) const;
    void EscribeHCalcPre(std::ostream &os,const std::string &sect) const;
    InformeMediciones GetInformeMediciones(void) const;
};

#endif
