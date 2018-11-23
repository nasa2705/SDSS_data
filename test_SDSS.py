from class_spectra import Spectrum


test_file="/Users/pagrawal/SciCoder-2018-Melbourne/Data Files/spectra/spec-4055-55359-0001.fits"
def test_1():
   spec=Spectrum(test_file)
   assert spec.header_card('NAME') == 3, "Unexpected number of HDUs found in file."