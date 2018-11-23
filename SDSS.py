#import SDSSdata
from astropy.io import fits

filename="spec-10000-57346-0019.fits"

hdu_list=fits.open(filename)

#print(len(hdu_list))
#print(hdu_list[0].header)
#print(hdu_list.info())

for key, value in hdu_list[0].header.items():
 print("{0}={1}".format(key,value))