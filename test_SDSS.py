"""
Script to test the code for reading SDSS spectra.
"""

import os
from class_spectra import Spectrum
from pathlib import Path

test_file_dir = Path(os.environ['TEST_FILE_DIR'])

assert test_file_dir.exists(), '$TEST_FILE_DIR does not exist.'

test_file = test_file_dir / "spec-4055-55359-0001.fits"

assert test_file.exists(), 'Test file does not exist.'


def test_read_spectrum():
    spec = Spectrum(test_file)
    assert len(spec.data) == 4,\
        "Unexpected number of HDUs found in file."
