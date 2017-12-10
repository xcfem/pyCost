# _*_ coding:utf-8 _*_
#pylatex_utils.py

'''Things that are not yet implemented in pylatex.'''


import pylatex

class Part(pylatex.section.Section):
    '''A class that represents a part.'''

class Chapter(pylatex.section.Section):
    '''A class that represents a chapter.'''

class SmallCommand(pylatex.base_classes.CommandBase):
    '''
    small LaTeX command.
    '''

    _latex_name = 'small'

def getLatexSection(parentSection):
    ''' Returns the section to use from this of its ancestor.'''
    if(parentSection == 'root'):
        return 'chapter'
    elif(parentSection == 'chapter'):
        return 'section'
    elif(parentSection == 'section'):
        return 'subsection'
    elif(parentSection == 'subsection'):
        return 'subsubsection'
    elif(parentSection == 'subsubsection'):
        return 'paragraph'
    elif(parentSection == 'paragraph'):
        return 'subparagraph'
    else:
        return 'xxx'

ltx_porciento= "\\%"
ltx_ldots= "\\ldots"
def ltx_symbol(doc,s):
    doc.append("\\symbol{" + s + '}')

# Tipos de letra
ltx_tiny= "\\scriptsize"
ltx_scriptsize= "\\scriptsize"
ltx_small= "\\small"
ltx_normalsize= "\\normalsize"
ltx_large= "\\large"
def ltx_textbf(str):
    return '\\textbf{' + str + '}'
def ltx_emph(doc, str):
    return '\\emph{' + str + '}'

# Entornos
def ltx_begin(doc, str):
    doc.append("\\begin{" + str + '}')
def ltx_end(doc, str):
    doc.append("\\end{" + str + '}')

# Varios
ltx_newpage= "\\newpage"
def ltx_input(doc, str):
    doc.append("\\input{" + str + '}')

# Estructura
ltx_parttoc= "\\parttoc"

def ltx_part(doc,  str):
    doc.append("\\part{" + str + '}')
def ltx_star_part(doc,  str):
    doc.append("\\part*{" + str + '}')
def ltx_chapter(doc,  str):
    doc.append("\\chapter{" + str + '}')
def ltx_star_chapter(doc,  str):
    doc.append("\\chapter*{" + str + '}')
def ltx_section(doc,  str):
    doc.append("\\section{" + str + '}')
def ltx_subsection(doc,  str):
    doc.append("\\subsection{" + str + '}')
def ltx_subsubsection(doc,  str):
    doc.append("\\subsubsection{" + str + '}')
def ltx_paragraph(doc,  str):
    doc.append("\\paragraph{" + str + '}')

# Listas
ltx_beg_itemize= "\\begin{itemize}"
ltx_item= "\\item "
ltx_end_itemize= "\\end{itemize}"

# Tablas
ltx_ampsnd= " & "
ltx_fin_reg= " \\\\"
ltx_hline= "\\hline"
ltx_endhead= "\\endhead"
ltx_endfoot= "\\endfoot"
ltx_endlastfoot= "\\endlastfoot"
def ltx_cline(doc,  str):
    doc.append("\\cline{" + str + "}")
def ltx_datos_multicolumn( num_campos, just, texto):
    return ("{" + num_campos + "}{" + just + "}{" + texto + "}")
def ltx_multicolumn(str):
    return '\\multicolumn' + str

def ascii2latex(s):
    '''Return the equivalent latex code.'''
    if type(s) == str:
        # Ignore errors even if the string is not proper UTF-8 or has
        # broken marker bytes.
        # Python built-in function unicode() can do this.
        tmp= unicode(s, encoding= "utf-8", errors="ignore")
    else:
        # Assume the value object has proper __unicode__() method
        tmp= unicode(s)
    #tmp= s.encode('ascii',errors='replace') #unicode(s, errors='replace')
    if(tmp.find('\\')): # Tiene escape.
     tmp.replace('\\(','(')
    if(tmp.find('\\')):
     tmp.replace('\\)',')')
    if(tmp.find('\\')):
     tmp.replace('\\[','[')
    if(tmp.find('\\')):
     tmp.replace('\\]',']')
    retval= ''
    for c in tmp:
        if(c=='_'): retval+= '\\'
        if(c=='%'): retval+= '\\'
        if(c=='$'): retval+= '\\'
        if(c=='&'): retval+= '\\'
        if(c=='>'):
            retval+= '$>$'
            continue
        retval+= c
    return retval
