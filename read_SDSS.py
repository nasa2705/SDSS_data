from .class_spectra import Spectra
import argparse
import astropy
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="This program does stuff",
                                 usage="name_of_script ...",
                                 epilog="this is text added to the end of the help")

parser.add_argument('-f', '--file',
                    help="File to open.",
                    type=argparse.FileType('r'))
args = parser.parse_args()


spec1 = Spectrum(args.file)


plt.figure()
x = spec1.wavelength
y = spec1.flux

plt.plot(x,y)

plt.xlabel("Wavelength")
plt.yalbel("Flux")
