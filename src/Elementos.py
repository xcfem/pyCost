# -*- coding: utf-8 -*-
#Elementos.py




import Elemento
import MapaConceptos
import ComptesBC3
import Codigos

#not  @brief Tabla de precios elementales.
class Elementos(MapaConceptos):

    def WriteHCalc(os):
        lmsg.error("Elementos.WriteHCalc no implementada." + '\n')

    def __init__(self):
        super(Elementos,self).__init__()
        
    @staticmethod
    def ImprLtxCabecera(self, tipo, os):
        str_tipo = ""
        if(tipo==mdo):
            str_tipo= "mano de obra"
        elif(tipo==maq):
            str_tipo= "maquinaria"
        elif(tipo==mat):
            str_tipo= "materiales"
        else:
            str_tipo= "sin clasificar"

        os.write(ltx_begin("center") + '\n')
        os.write(ltx_large + " Precios elementales de " + str_tipo + ' '
           + ltx_normalsize + '\n')
        os.write(ltx_end("center") + '\n')
        os.write(ltx_small + '\n')
        os.write("\\begin{longtable}{|l|l|p{4cm}|r|}" + '\n'
           + ltx_hline + '\n'
           + "Código & Ud. & Denominación & Precio\\\\" + '\n'
           + ltx_hline + '\n'
           + ltx_endhead + '\n'
           + ltx_hline + '\n'
           + "\\multicolumn{" + 4 + "}{|r|}{../..}\\\\\\hline" + '\n'
           + ltx_endfoot + '\n'
           + ltx_hline + '\n'
           + ltx_endlastfoot + '\n')


    def LeeMdoSpre(self, iS):
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
                precios= ''
                getline(iS,precios,'\n')
                pre= ''
                pos = precios.find('|')
                if pos<len(precios):
                    pre= precios.substr(0,pos)
                else:
                    pre= precios.substr(0,len(precios)-1)
                elem= Elemento(cod,tit,ud,atof(pre.c_str()),mdo)
                elem.texto_largo= tit
                Agrega(elem)
                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')

    def LeeMaqSpre(self, iS):
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
                precios= ''
                getline(iS,precios,'\n')
                pre= ''
                pos = precios.find('|')
                if pos<1000:
                    pre= precios.substr(0,pos)
                else:
                    pre= precios.substr(0,len(precios)-1)
                elem= Elemento(cod,tit,ud,atof(pre.c_str()),maq)
                elem.texto_largo= tit
                Agrega(elem)
                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')

    def LeeMatSpre(self, iS):
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
                precios= ''
                getline(iS,precios,'\n')
                pre= ''
                pos = precios.find('|')
                if pos<1000:
                    pre= precios.substr(0,pos)
                else:
                    pre= precios.substr(0,len(precios)-1)
                elem= Elemento(cod,tit,ud,atof(pre.c_str()),mat)
                elem.texto_largo= tit
                Agrega(elem)
                if(iS.peek() == 26): break

        resto= ''
        getline(iS,resto,'\n')


    def WriteSpre(self):
        ofs_mdo= std.ofstream("MDO001.std",std.ios.out)
        ofs_maq= std.ofstream("MAQ001.std",std.ios.out)
        ofs_mat= std.ofstream("MAT001.std",std.ios.out)
        for i in self:
            tipo= (i).second.Tipo()
            if(tipo==mdo):
                (i).second.WriteSpre(ofs_mdo)
                break
            elif(tipo==maq):
                (i).second.WriteSpre(ofs_maq)
                break
            elif(tipo==mat):
                (i).second.WriteSpre(ofs_mat)
                break
            else:
                (i).second.WriteSpre(ofs_mdo)
                break

        ofs_mdo.close()
        ofs_maq.close()
        ofs_mat.close()


    def LeeSpre(self, iS):
        Str= ''
        getline(iS,str,'\n')
        if(Str.find("[MDO]")<len(Str)): LeeMdoSpre(iS)
        getline(iS,Str,'\n')
        if(Str.find("[MAQ]")<len(Str)): LeeMaqSpre(iS)
        getline(iS,Str,'\n')
        if(Str.find("[MAT]")<len(Str)): LeeMatSpre(iS)

    def LeeBC3(self, els):
        if not els.empty():
            if verborrea>2:
                logging.info("Cargando precios elementales." + '\n')
            sz_inicial= len(self)
            el= Elemento()
            for i in self:
                el.LeeBC3(els.GetDatosElemento(i))
                Agrega(el)

            num_agregados = len(self)-sz_inicial
            if num_agregados != els.size():
                lmsg.error("¡Errornot , pasaron: " + els.size()
                          + " precios elementales y se cargaron "
                          + num_agregados+ '\n')
            if verborrea>2:
                logging.info("Cargados " + els.size() + " precios elementales. " + '\n')


    def ImprLtxTipo(self, tipo, os):
        ImprLtxCabecera(tipo,os)
        el= None
        for i in self:
            el= ((i).second)
            if el.Tipo() == tipo:
                el.ImprLtx(os)

        os.write("\\end{longtable}" + '\n')
        os.write(ltx_normalsize + '\n')

    def ImprLtx(self, os):
        ImprLtxTipo(mdo,os)
        os.write(ltx_newpage + '\n')
        ImprLtxTipo(maq,os)
        os.write(ltx_newpage + '\n')
        ImprLtxTipo(mat,os)

