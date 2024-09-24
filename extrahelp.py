from py_ecc.bn128 import curve_order
import galois
GF = galois.GF(curve_order, primitive_element=5, verify=False)

#speed up compuration for galois cal on elptic curve
