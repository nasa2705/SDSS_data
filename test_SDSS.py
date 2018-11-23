from class_spectra import Spectrum


test_file="/Users/pagrawal/SciCoder-2018-Melbourne/Data Files/spectra/spec-4055-55359-0001.fits"
def test_hdu_numbers():
   spec=Spectrum(test_file)
   assert len(spec.data) == 4, "Unexpected number of HDUs found in file."
   
def test_ra:
	pass
