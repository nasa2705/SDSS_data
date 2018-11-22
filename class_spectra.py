#!/usr/bin/python

'''
creates class for reading in fits file
'''

from astropy.io import fits


class Spectrum(object):
    def __init__(self, filename):
        self.data = fits.open(filename)

    @property
    def wavelength(self):
        """Wavelength binning, linear bins."""
        if getattr(self, '_wavelength', None) is None:
            self._wavelength = 10**self.data[1].data['loglam']
        return self._wavelength

    @property
    def flux(self):
        if getattr(self, '_flux', None) is None:
            self._flux = self.data[1].data['flux']
        return self._flux

    def header_card(self, keyword):
        """
        Return the value of the header card with the given keyword.

        Parameters
        ----------
        keyword: str
            The keyword to look up in the FITS headers. Astropy allows case-
            insensitive strings, but should ideally be all-caps to encourage
            good practice and conformace with the FITS standard.

        Returns
        -------
        str
            The value of the header card with the keyword.
        """
        return self.data[0].header[keyword]

