"""
These are unit tests for the datavis module
"""

import numpy as np
import sys

sys.path.append('..')

import datavis

def test_se_to_sd():
    """
    Test that the value returned is a float value
    """
    sdev = datavis.se_to_sd(0.5, 1000)
    assert isinstance(sdev, float),\
    "Returned data type is not a float number"

def test_ci_to_sd():
    """
    Test that the value returned is a float value
    """
    sdev = datavis.ci_to_sd(0.2, 0.4)
    assert isinstance(sdev, float),\
    "Returned data type is not a float number"

def test_datagen():
    """
    Test that the data returned is a numpy.ndarray
    """
    randdata = datavis.datagen(25, 0.2, 0.4)
    assert isinstance(randdata, np.ndarray),\
    "Returned data type is not a numpy.ndarray"

def test_correctdatatype():
    """
    Test that the statistical parameters returned are float numbers
    """
    fmean = datavis.correctdatatype(0.2, 0.4)[0]
    assert isinstance(fmean, float),\
    "Returned data type is not a float number"

def test_compounddata():
    """
    Test that the data returned are numpy.ndarrays
    """
    datagenerated1 = datavis.compounddata\
    (mean1=24.12, sdev1=3.87, mean2=24.43, sdev2=3.94, mean3=24.82, sdev3=3.95, size=1000)[0]
    assert isinstance(datagenerated1, np.ndarray),\
    "Returned data are not numpy.ndarrays"

def test_databinning():
    """
    Test that the data returned are numpy.ndarrays
    """
    datagenerated1, datagenerated2, datagenerated3 = \
    datavis.compounddata\
    (mean1=24.12, sdev1=3.87, mean2=24.43, sdev2=3.94, mean3=24.82, sdev3=3.95, size=1000)
    bins = np.linspace(10, 40, num=30)
    yhist1 = datavis.databinning\
    (datagenerated1, datagenerated2, datagenerated3, bins_list=bins)[0]
    assert isinstance(yhist1, np.ndarray),\
    "Returned data are not numpy.ndarrays"

def test_pdfgen():
    """
    Test that the data returned are numpy.ndarrays
    """
    bins = np.linspace(10, 40, num=30)
    mean1 = 24.12
    sdev1 = 3.87
    mean2 = 24.43
    sdev2 = 3.94
    mean3 = 24.82
    sdev3 = 3.95
    pdf1 = datavis.pdfgen\
    (mean1, sdev1, mean2, sdev2, mean3, sdev3, bins_list=bins)[0]
    assert isinstance(pdf1, np.ndarray),\
    "Returned data are not numpy.ndarrays"

def test_percent_overlap():
    """
    Test that the data returned is a tuple
    """
    mean1 = 24.12
    sdev1 = 3.87
    mean2 = 24.43
    sdev2 = 3.94
    mean3 = 24.82
    sdev3 = 3.95
    assert isinstance\
    (datavis.percent_overlap\
     (mean1, sdev1, mean2, sdev2, mean3, sdev3), tuple),\
    "Returned data is not a tuple"
