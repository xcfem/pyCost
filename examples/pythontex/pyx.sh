#!/bin/sh
# Run pythontex on a suitable LaTeX file

pdflatex $1
pythontex $1
pdflatex $1
