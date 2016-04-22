//CuaPre.h

#ifndef CUAPRE_H
#define CUAPRE_H

#include "Elementos.h"
#include "Descompuestos.h"

class CuaPre: public EntPpl
{
private:
    Elementos elementos; //Precios elementales.
    Descompuestos unidades; //Unidades de obra.

public:
    const Elementos &Elementales(void) const
    {
        return elementos;
    }
    Elementos &Elementales(void)
    {
        return elementos;
    }
    const Descompuestos &UdsObra(void) const
    {
        return unidades;
    }
    inline bool TieneElementales(void) const
    {
        return (elementos.size()>0);
    }
    inline size_t NumDescompuestos(void) const
    {
        return unidades.size();
    }
    inline bool TieneDescompuestos(void) const
    {
        return (unidades.size()>0);
    }
    inline BuscadorDescompuestos GetBuscadorDescompuestos(void)
    {
        return unidades.GetBuscador();
    }
    const UdObra *BuscaUdObra(const std::string &cod) const;
    const Elemento *BuscaElemento(const std::string &cod) const;
    const Medible *BuscaPrecio(const std::string &cod) const;
    void AgregaComponente(const std::string &cod_ud,const std::string &cod_el,const float &r, const float &f= 1.0)
    {
        unidades.AgregaComponente(elementos,cod_ud,cod_el,r,f);
    }

    void EscribeSpre(void) const;
    void EscribeBC3(std::ostream &os) const;
    void LeeSpre(std::istream &is);
    inline void LeeBC3Elementales(const Codigos &elem)
    {
        elementos.LeeBC3(elem);
    }
    inline void LeeBC3DescompFase1(const Codigos &descomp)
    {
        unidades.LeeBC3Fase1(descomp);
    }
    Descompuestos::set_pendientes LeeBC3DescompFase2(const Codigos &descomp);
//     inline void LeeBC3Fase1(const CodigosObra &c)
//       {
//         LeeBC3Elementales(c.GetDatosElementos());
//         LeeBC3DescompFase1(c.GetDatosUnidades());
//       }
//     inline void LeeBC3Fase2(const CodigosObra &c)
//       { LeeBC3DescompFase2(c.GetDatosUnidades());  }
    void ImprLtxElementales(std::ostream &os) const;
    void ImprLtxJustPre(std::ostream &os) const;
    void ImprLtxCP1(std::ostream &os) const;
    void ImprLtxCP2(std::ostream &os) const;
    void ImprLtxCP(std::ostream &os) const;
    void EscribeHCalc(std::ostream &os) const;
    void SimulaDescomp(const std::string &origen, const std::string &destino);
};

#endif
