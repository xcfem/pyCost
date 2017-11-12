# -*- coding: utf-8 -*-
#InformeMediciones.py


import InformeUdObra as iuo

class InformeMediciones(dict):

    def Inserta(self, iu):
        i = find(iu.Unidad())
        if i!=end():
            (i).second+= iu.Medicion()
        else:
            (self)[iu.Unidad()]= iu.Medicion()

    def Merge(self, otro):
        for i in otro:
            Inserta(InformeUdObra((i).first,(i).second))

    def ImprLtx(self, os):
        if(size()<1): return
        os.write("\\begin{longtable}{|l|p{4cm}|r|r|}" + '\n'
           + "\\hline" + '\n'
           + "Código & Descripción & Medición & Precio \\\\"
           + "\\hline" + '\n'
           + "\\endhead" + '\n'
           + "\\hline" + '\n'
           + "\\multicolumn{" + 4 + "}{|r|}{../..}\\\\\\hline" + '\n'
           + "\\endfoot" + '\n'
           + "\\hline" + '\n'
           + "\\endlastfoot" + '\n')
        for i in self:
            iu= iuo.InformeUdObra((i).first,(i).second)
            iu.ImprLtx(os)
            os.write( "\\\\" + '\n')

        os.write("\\end{longtable}" + '\n')

