from burnman import Mineral, PerplexMaterial, Composite, Layer, Planet
from burnman import minerals

material = minerals.SE_2015.bcc_iron()
print(material.params)