#!/usr/bin/python

'''
creates class for reading in fits file
'''

class Spectra(object):
	def __init__(self,*args,**kwargs):
		self.header=None
		self.data=None

	@property
    def wavelength(self):
        """Wavelength binning, linear bins."""
        if getattr(self,'_wavelength',None) is None:
            self._wavelength = 10**self.data[1].data['loglam']
        return self._wavelength

    @property
    def flux(self):
        if getattr(self,'_flux',None) is None:
            self._flux = self.data[1].data['flux']
        return self._flux
        
    