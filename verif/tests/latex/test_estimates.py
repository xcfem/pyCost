'''Test data.'''
from pycost.structure import obra
from pycost.structure.chapter import Chapter
from pycost.structure.unit_price_quantities import UnitPriceQuantities

obra= obra.Obra(cod="test", tit="Test title")

# Read data from file.
pth= os.path.dirname(__file__)
# print("pth= ", pth)
if(not pth):
    pth= '.'
obra.readFromYaml(pth+'/../data/test_03_prices.yaml')

ch01= obra.subcapitulos.newChapter(Chapter(cod= '01', tit= 'Test'))

# Measurements
## MAACE0201 quantities.
rebarMeasurements= UnitPriceQuantities(obra.getUnitPrice('MAACE0201'))
q1units= 2
q1l= 10.0
rebarMeasurements.appendMeasurement(textComment='test A', nUnits= q1units, length= q1l, width=None, height=None)
ch01.appendUnitPriceQuantities(rebarMeasurements)

## ACERO0103 quantities.
reinfMeasurements= UnitPriceQuantities(obra.getUnitPrice('ACERO0103'))
q2units= 20
q2l= 25.0
reinfMeasurements.appendMeasurement(textComment='test B', nUnits= q2units, length= q2l, width=None, height=None)
ch01.appendUnitPriceQuantities(reinfMeasurements)
