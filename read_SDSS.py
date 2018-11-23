from class_spectra import Spectrum
import argparse
import astropy
from astropy.io import fits
import matplotlib.pyplot as plt
import re

parser = argparse.ArgumentParser(description="This program reads a given SDSS"+
                                 " spectrum and plots it.",
                                 usage="read_SDSS.py <filename>")

parser.add_argument('-f', '--file',
                    help="File to open.")
args = parser.parse_args()

# filematch=re.match("\S+/([a-zA-Z]+)\-([0-9]+)\-([0-9]+)\-([0-9]+).fits",args.file)
# 
# assert filematch is not None, "The filename is not correct."

spec1 = Spectrum(args.file)



plt.figure()
x = spec1.wavelength
y = spec1.flux
n = spec1.header_card('NAME')
ra= spec1.header_card('RA')
dec= spec1.header_card('DEC')



plt.plot(x,y,label="NAME={},RA={},DEC={}".format(n, ra, dec))

plt.xlabel("Wavelength (Angstroms)")
plt.ylabel("Flux (erg/cm^2/s/Ang)")

plt.legend(loc='upper center', fontsize=7)

plt.show()
