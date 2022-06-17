# -*- coding: utf-8 -*-
'''Trivial PyCost test.''' 
from __future__ import division
from __future__ import print_function

import os
import pylatex
from pycost.structure import obra
from pycost.structure.chapter import Chapter
from pycost.structure.unit_price_quantities import UnitPriceQuantities
from pycost.utils import pylatex_utils

exec(open("test_estimates.py").read())

# Store text int pylatex doc.
doc= pylatex.Document(documentclass= 'book')
doc.packages.append(pylatex.Package('babel', options = ['spanish']))
doc.packages.append(pylatex.Package('aeguill'))
doc.packages.append(pylatex.Package('minitoc'))
doc.preamble.append(pylatex.Command('selectlanguage', 'spanish'))
# doc.append(pylatex.Command('doparttoc'))
# doc.append(pylatex.Command('parttoc'))
obra.writePartialBudgetsIntoLatexDocument(doc)

# Generate LaTeX file.
outputFilesBaseName= 'partial_estimates_01'
doc.generate_tex(outputFilesBaseName)

# Remove temporary files.
pylatex_utils.removeLtxTemporaryFiles(outputFilesBaseName)
