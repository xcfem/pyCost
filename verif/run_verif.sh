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
python tests/test_02.py
python tests/test_03.py
python tests/test_extract_concepts.py
python tests/test_extract_concepts_regex.py
python tests/test_merge_concepts_01.py
python tests/test_merge_concepts_02.py
echo "$BLEU" "  FieBDC3 read tests." "$NORMAL"
python tests/bc3/test_read_bc3_01.py
python tests/bc3/test_read_bc3_02.py
python tests/bc3/test_read_bc3_03.py
python tests/bc3/test_read_bc3_04.py
#python tests/bc3/test_read_bc3_05.py
echo "$BLEU" "  YAML read tests." "$NORMAL"
python tests/yaml/test_read_yaml_01.py
python tests/yaml/test_read_yaml_02.py
python tests/yaml/test_read_yaml_03.py
python tests/yaml/test_read_yaml_04.py
#python tests/yaml/test_read_yaml_05.py
python tests/yaml/test_read_yaml_06.py
echo "$BLEU" "  pickle read/write tests." "$NORMAL"
python tests/pickle/test_write_pickle.py
python tests/pickle/test_read_pickle.py
python tests/pickle/test_yaml_to_pickle.py


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
