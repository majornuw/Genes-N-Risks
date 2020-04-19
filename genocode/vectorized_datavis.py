"""
This file contains vectorized functions which can be used to visualize the graphical
representation of the statistical data generated by DTC genetic tests. It gives
a better understanding of the risk of genotypes posed by the phenotypes in a
person.
"""

import math
from statistics import NormalDist
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def se_to_sd(serror, size):
    """
    Converts Standard Error to Standard deviation.
    Parameters:
        serror (float, required): The standard error of the data to be
            generated.
        size (float, required): The size of the population.
    Returns:
        float: A float value for the standard deviation.
    """
    sdev = serror*math.sqrt(size)
    return sdev

def ci_to_sd(lowerci, upperci, cival=95.0, size=100):
    """
    Converts Confidence interval to Mean and Standard deviation.
    Parameters:
        lowerci (float, required): The lower bound of the confidence
            interval.
        upperci (float, required): The upper bound of the confidence
            interval.
        cival (float, optional): The confidence level.
            It must be one of the following values.
            [99.9,99.5,99.0,95.0,90.0,85.0,80.0]
            The default value is 95 for 95% confidence interval.
        size (int, optional): The size of the sample to be generated.
            The default value is 100.
    Returns:
        float: A float value for Standard deviation.
    """
    zvals = {99.9:3.291, 99.5:2.807, 99.0:2.807, 95.0:1.960, 90.0:1.645, \
            85.0:1.645, 80.0:1.282}
    zscore = zvals[float(cival)]
    sdev = math.sqrt(size)*(upperci-lowerci)/zscore
    return sdev

def datagen(mean=None, sdev=None, serror=None, lowerci=None, upperci=None, \
            cival=95.0, size=100):
    """
    Generates random standard distribution data from mean and standard
    deviation.
    Parameters:
        mean(float, required): The mean of the data to be generated.
        sdev (float, optional): The standard deviation of the data to be
            generated.
        serror (float, optional): The standard error of the data to be
            generated.
        lowerci (float, required): The lower bound of the confidence
            interval.
        upperci (float, required): The upper bound of the confidence
            interval.
        cival (float, optional): The confidence level.
            It must be one of the following values.
            [99.9,99.5,99.0,95.0,90.0,85.0,80.0]
            The default value is 95 for 95% confidence interval.
        size (int, optional): The size of the sample to be generated.
            The default value is 100.
    Returns:
        numpy.ndarray: A numpy array with random standard distribution
        data.
    """
    if isinstance(upperci, float):
        sdev = ci_to_sd(lowerci, upperci, cival, size)
        if isinstance(mean, None):
            mean = (upperci+lowerci)/2
    if isinstance(serror, float):
        sdev = se_to_sd(serror, size)
    randdata = np.random.normal(mean, sdev, size)
    return randdata

def correctdatatype(mean=None, sdev=None, serror=None, upperci=None, \
                    lowerci=None):
    """
    Returns float values for each statistical parameter.
    Parameters:
        mean(int/str, optional): The mean.
        sdev (int/str, optional): The standard deviation of the data to be
            generated.
        serror (int/str, optional): The standard error of the data to be
            generated.
        lowerci (int/str, required): The lower bound of the confidence
            interval.
        upperci (int/str, required): The upper bound of the confidence
            interval.
    Returns:
        float: A float value for mean.
        float: A float value for sd.
        float: A float value for se.
        float: A float value for lowerci.
        float: A float value for upperci.
    """
    if isinstance(mean, int):
        fmean = float(mean)
    elif isinstance(mean, str):
        fmean = float(mean)
    else:
        fmean = mean
    if isinstance(sdev, int):
        fsdev = float(sdev)
    elif isinstance(sdev, str):
        fsdev = float(sdev)
    else:
        fsdev = sdev
    if isinstance(serror, int):
        fserror = float(serror)
    elif isinstance(serror, str):
        fserror = float(serror)
    else:
        fserror = serror
    if isinstance(upperci, int):
        fuci = float(upperci)
    elif isinstance(upperci, str):
        fuci = float(upperci)
    else:
        fuci = upperci
    if isinstance(lowerci, int):
        flci = float(lowerci)
    elif isinstance(lowerci, str):
        flci = float(lowerci)
    else:
        flci = lowerci
    return fmean, fsdev, fserror, fuci, flci

def compounddata(mean=None, sdev=None, serror=None, upperci=None, \
                lowerci=None, cival=95.0, size=1000):
    """
    A partial wrapper function to generate three datasets of similar
    attributes.
    Parameters:
        mean (numpy.ndarray, optional): The means.
        sdev (numpy.ndarray, optional): The standard deviations of the
            data to be generated.
        serror (numpy.ndarray, optional): The standard error of the
            data to be generated.
        lowerci (numpy.ndarray, optional): The lower bounds of the
            confidence interval.
        upperci (numpy.ndarray, optional): The upper bounds of the
            confidence interval.
        cival (float, optional): The confidence level.

    Returns:
        numpy.ndarray: A numpy array with all the random standard
            distribution data.
    """
    if isinstance(mean, np.ndarray):
        count = len(mean)
        if isinstance(sdev, np.ndarray):
            serror = np.empty(count, dtype=object)
        elif isinstance(serror, np.ndarray):
            sdev = np.empty(count, dtype=object)
        upperci = np.empty(count, dtype=object)
        lowerci = np.empty(count, dtype=object)
    elif isinstance(upperci, np.ndarray):
        count = len(upperci)
        mean = np.empty(count, dtype=object)
        sdev = np.empty(count, dtype=object)
        serror = np.empty(count, dtype=object)
    datagenerated = np.empty(count, dtype=object)

    for i in range(count):
        flmean, flsdev, flserror, flupperci, fllowerci = correctdatatype(\
                                                                    mean[i], \
                                                                    sdev[i], \
                                                                    serror[i], \
                                                                    upperci[i], \
                                                                    lowerci[i])
        datagenerated[i] = datagen(mean=flmean, sdev=flsdev, serror=flserror, \
                            upperci=flupperci, lowerci=fllowerci, \
                            cival=cival, size=size)

    return datagenerated

def databinning(datagenerated, bins_list):
    """
    A function to create 3 histogram bins.
    Parameters:
        datagenerated (numpy.ndarray, required): A numpy array with
            random standard distribution data.
        bins_list(numpy.ndarray, required): A numpy array listing the
            edges of the bins.
    Returns:
        numpy.ndarray: The values of all the histograms.
    """
    count = len(datagenerated)
    yhist = np.empty(count, dtype=object)
    for i in range(count):
        yhist[i], _ = np.histogram(a=datagenerated[i], bins=bins_list)
    return yhist

def histplotting(datagenerated, \
                bins_list=None):
    """
    A function to plot 3 overlapping histograms
    Parameters:
        datagenerated (numpy.ndarray, required): A numpy array with
            random standard distribution data.
        bins_list(numpy.ndarray, required): A numpy array listing the
            edges of the bins.
    Returns:
        None.
    """
    a4_dims = (12, 9)
    _, axes = plt.subplots(figsize=a4_dims)
    count = len(datagenerated)
    for i in range(count):
        sns.distplot(ax=axes, a=datagenerated[i], bins=bins_list, color='blue', \
                    label='Wild')

    plt.xlabel('BMI (kg/m$^2$)', fontsize=20)
    plt.ylabel('Probability Density', fontsize=20)
    plt.title('Normal Distribution Curves of Each Genotype', fontsize=20)

    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)

    plt.legend(fontsize=20)

    return None

def pdfgen(mean, sdev, bins_list):
    """
    A function to generate 3 probability density function data
    Parameters:
        mean1 (numpy.ndarray, required): The means of the datasets.
        sdev1 (numpy.ndarray,1 required): The standard deviation of
            the dataset
        bins_list(numpy.ndarray, required): A numpy array listing the
            edges of the bins.
    Returns:
        None.
    """
    count = len(mean)
    pdf = np.empty(count, dtype=object)
    for i in range(count):
        pdf[i] = 1/(sdev[i] * np.sqrt(2 * np.pi)) * np.exp(- (bins_list - mean[i])**2 / \
            (2 * sdev[i]**2))

    return pdf

def pdfplotting(mean, sdev, bins_list):
    """
    A function to plot 3 overlapping probability density function
    curves.
    Parameters:
        datagenerated (numpy.ndarray, required): A numpy array with
            random standard distribution data.
        bins_list(numpy.ndarray, required): A numpy array listing the
            edges of the bins.
    Returns:
        None.
    """
    count = len(mean)
    plt.figure(figsize=(12, 9))
    pdf = pdfgen(mean, sdev, bins_list)
    for i in range(count):
        plt.plot(bins_list, pdf[i], linewidth=2, color='b') #We can't have labels here


    #plt.plot(bins_list, pdf2, linewidth=2, color='orange', \
    #                label='Single SNP')
    #plt.plot(bins_list, pdf3, linewidth=2, color='g', label='Double SNP')

    plt.xlabel('BMI (kg/m$^2$)', fontsize=20)
    plt.ylabel('Probability Density', fontsize=20)
    plt.title('Normal Distribution Curves of Each Genotype', fontsize=20)

    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)

    plt.legend(fontsize=20)

    return None

def violinplotting(datagenerated):
    """
    A function to plot 3 consecutive violin plots
    Parameters:
        datagenerated (numpy.ndarray, required): A numpy array with
            random standard distribution data.
        bins_list(numpy.ndarray, required): A numpy array listing the
            edges of the bins.
    Returns:
        None.
    """

    plt.figure(figsize=(12, 9))
    count = len(datagenerated)
    for i in range(count):
        plt.violinplot(datagenerated[i], positions=[i], showmeans=True)


    plt.xlabel('Genotype', fontsize=20)
    plt.ylabel('BMI (kg/m$^2$)', fontsize=20)
    plt.title('Effect of Genotype on Phenotype', fontsize=20)

    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=15)

    #locs, labels = plt.xticks()
    locs = np.arange(count)
    #labels = ['TT', 'AT', 'AA']
    plt.xticks(locs)#, labels)

    return None

def percent_overlap(mean=None, sdev=None):
    """
    A function to estimate the percentage of overlap between multiple
    normally distributed data.
    Parameters:
        mean (numpy.ndarray, required): The means of the data sets.
        sdev1 (numpy.ndarray, required): The standard deviations of
            the data sets.
    Returns:
        numpy.ndarray: An array with float values showing the
            percentage overlap between 1st and the other data sets.
    """
    count = len(mean)
    overlap_perc_1w = np.empty(count, dtype=object)
    for i in range(count):
        overlap_perc_1w[i] = 'The overlap between dataset 1 and dataset '\
                            +str(i)+' is {0:1.2%}'.format(NormalDist(mu=mean[i]\
                            , sigma=sdev[i]).overlap(NormalDist(mu=mean[i], \
                            sigma=sdev[i])))

    return overlap_perc_1w
