#!/bin/sh
# 
#   Copyright (C)  Luis C. Pérez Tato
# 
#   XC utils is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
# 
#   This software is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.  
# 
#  You should have received a copy of the GNU General Public License 
#  along with this program.
#  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------

ERT="\\033[1;32m"
NORMAL="\\033[0;39m"
ROUGE="\\033[1;31m"
ROSE="\\033[1;35m"
BLEU="\\033[1;34m"
BLANC="\\033[0;02m"
BLANCLAIR="\\033[1;08m"
JAUNE="\\033[1;33m"
CYAN="\\033[1;36m"

echo ""

START=$(date +%s.%N)

# Misc. tests
echo "$BLEU" "PyCost tests." "$NORMAL"
python tests/test_01.py
python tests/test_read_bc3_01.py
python tests/test_read_bc3_02.py
python tests/test_read_bc3_03.py

END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo $DIFF seconds
NT=$(grep -c '^python' $0)
echo ${NT} tests
Q=$(echo "$DIFF / $NT" | bc -l)
echo $Q seconds/test

# Clean garbage if any

rm -f -r ./annex
rm -f -r ./tmp
