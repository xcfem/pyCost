import re
from pycost.structure import obra
from pycost.prices import elementary_price
from pycost.utils import basic_types
from pycost.prices import unit_price

presup=obra.Obra(cod="paramConcp", tit="Parametric concepts")
# Lee base de precios.
basePrecios= './base_precios_adif_julio_2022.json'
bp=presup.readFromJson(basePrecios)

def load_param_prices(lstCod):
    ''' Load parametric prices from full codes in the list given as parameter
    '''
    optIds=['a','b','c','d','e','f','g','h','i']
    for cod in lstCod:
        splCod=re.split('(\d+)',cod)
        selectOptions=splCod[-1]
        rootCode=str()
        for c in splCod[:-1]:
            rootCode+=str(c)
        rootCode+='$'
        pConcept=presup.precios.unidades.getParametricConcept(key=rootCode)
        optLabels=list(pConcept.parameters.parameterLabelLetters.keys())
        optLabelStat=pConcept.parameters.parameterLabelStatements
        opt2import=list()
        cont=0
        for i,optId in enumerate(selectOptions):
            optIndex=optIds.index(optId)
            optKey=optLabels[cont]
            selOpt=optLabelStat[optKey][optIndex]
            opt2import.append([optKey,selOpt])
            cont+=1
        # Create unit price with the options in selOpt.
        unitPrice= pConcept.getUnitPrice(code= cod, options= opt2import, rootChapter= presup)
        # Append the price to the root chapter price table.
        presup.precios.unidades.Append(unitPrice)


lstCod=['OCA090bdcdc']#,'OAC070abcd','OAC010abcdc','OHC010aacdc','OHC010bacdc','OCH050bcdc']
load_param_prices(lstCod)
