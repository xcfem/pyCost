# -*- coding: utf-8 -*-
#Descompuestos.py




import elementary_price_container
import unit_price
from pycost.utils import concept_dict

class Descompuestos(concept_dict.ConceptDict):
    '''Unidades de obra.'''

    def AgregaComponente(self, el, cod_ud, cod_el, r, f):
        i= Busca(cod_ud)
        j= el.Busca(cod_el)
        if not j:
            lmsg.error("Elemento: " + cod_el
                      + " no encontrado en unidad de obra: " + cod_ud + '\n')
            exit(1)

        i.Append(j,f,r)


    def GetBuscador(self):
        return BuscadorDescompuestos(self)


    def LeeBC3Fase1(self, cds):
        '''Lee las unidades de obra a falta de la descomposición.'''
        ud= UnitPrice()
        for i in cds:
            reg = cds.getUnitPriceData(i)
            ud.LeeBC3Fase1(reg)
            Append(ud)


    def LeeBC3Fase2(self, cds, bp):
        '''Lee la descomposición de las unidades.'''
        ud=None
        error= False
        retval= set_pendientes
        for i in cds:
            reg = cds.getUnitPriceData(i)
            ud= Busca(reg.Codigo())
            error= ud.LeeBC3Fase2(reg,bp)
            if error:
                retval.insert(reg.Codigo())
        return retval

    def WriteSpre(self, os):
        for j in self:
            (j).second.WriteSpre(os)

    def AsignaFactor(self, f):
        for j in self:
            (j).second.AsignaFactor(f)

    def LeeSpre(self, iS, elementos):
        if iS.peek()!= 26:
            while(True):
                cod= ''
                getline(iS,cod,'|')
                ud= ''
                getline(iS,ud,'|')
                if ud.find('%')<len(ud):
                    cod= "%" + cod
                    ud= ""

                tit= ''
                getline(iS,tit,'|')
                unidad= UnitPrice(cod,tit,ud)
                unidad.texto_largo= tit
                Append(unidad)
                perc= '' #percentage
                getline(iS,perc,'|')
                descomp= '' #descomposición
                getline(iS,descomp,'\n')
                #istrstream istr(descomp.c_str(),descomp.leng.py())
                while(True):
                    pos2 = descomp.find('|')
                    cod_el = descomp.substr(0,pos2)
                    descomp.replace(0,pos2+1,"")
                    pos3 = descomp.find('|')
                    cantidad= ''
                    if pos3<1000:
                        cantidad= descomp.substr(0,pos3)
                        descomp.replace(0,pos3+1,"")

                    else:
                        cantidad= descomp.substr(0,len(descomp)-1)
                    if(elementos.find("%" + cod_el)!=elementos.end()): #Corresponds to a percentage.
                        cod_el = "%"+cod_el
                    AgregaComponente(elementos,cod,cod_el,atof(cantidad.c_str()))
                    if(pos3>len(descomp)): break

                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')


    def ImprLtxCP1(self, os):
        if(size()<1): return
        linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
        num_campos = 5
        os.write(ltx_small + '\n')
        os.write("\\begin{longtable}{|l|l|p{4cm}|p{3cm}|r|}" + '\n'
           + ltx_hline + '\n'
           + "Código & Ud. & Denominación & \\multicolumn{2}{|c|}{Precio}\\\\"
           + " & & & en letra & en cifra \\\\" + '\n'
           + ltx_hline + '\n'
           + ltx_endhead + '\n'
           + ltx_hline + '\n'
           + "\\multicolumn{" + num_campos + "}{|r|}{../..}\\\\\\hline" + '\n'
           + ltx_endfoot + '\n'
           + ltx_hline + '\n'
           + ltx_endlastfoot + '\n')
        j = begin()
        for j in self:
            os.write(linea_en_blanco + '\n')
            (j).second.ImprLtxCP1(os)
            os.write(linea_en_blanco + '\n')

        os.write("\\end{longtable}" + '\n')
        os.write(ltx_normalsize + '\n')

    def ImprLtxJustPre(self, os):
        os.write(ltx_small + '\n')
        os.write("\\begin{longtable}{l}" + '\n')
        for j in self:
            (j).second.ImprLtxJustPre(os)
            os.write(ltx_fin_reg + '\n')
            os.write(ltx_fin_reg + '\n')

        os.write("\\end{longtable}" + '\n')
        os.write(ltx_normalsize + '\n')

    def ImprLtxCP2(self, os):
        if(size()<1): return
        #os.write(ltx_star_.pyapter("Cuadro de precios no. 2") + '\n'
        os.write(ltx_small + '\n')
        os.write("\\begin{longtable}{l}" + '\n')
        for j in self:
            (j).second.ImprLtxCP2(os)
            os.write(ltx_fin_reg + '\n')
            os.write(ltx_fin_reg + '\n')

        os.write("\\end{longtable}" + '\n')
        os.write(ltx_normalsize + '\n')

    def WriteHCalc(self, os):
        os.write("Código" + tab
           + "Ud." + tab
           + "Denominación" + tab
           + "Precio en letra" + tab
           + "Precio en cifra" + '\n')
        for j in self:
            (j).second.WriteHCalc(os)



