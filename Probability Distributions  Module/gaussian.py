import math
import matplotlib.pyplot as plt
from convertfile import ConvertFile


class Gaussian(ConvertFile):

    """
    Gaussian Distribution class for calculating distribution
    statistics and visualizing the gaussian distribution

    Attributes:
        mean(float) - mean value of the distribution
        stdev(float) - standard deviation of the distribution
        data_list(list of floats) a list of floats extracted from a datafile
    """

    def __init__(self,path_to_file,mu = 0 ,sigma = 1):
        super().__init__(path_to_file)
        self.mean = mu
        self.standard_deviation = sigma

    def get_mean(self):

        """Method to calculate the mean of the data set

        Args: None

        Returns: mean(float) of the data set
        """
        num_list = self.return_list()

        mean_list = 1.0 * sum(num_list)/len(num_list)

        self.mean = mean_list

        return self.mean

    def get_stdev(self,sample=True):
        """ Method that calculates the standard deviation

        Args:
            sample(bool): whether the data represents sample population

        Returns:
            standard deviation (float) of the data

        """
        num_list = self.return_list()
        
        mean = self.get_mean()

        if sample:
            n = len(num_list) - 1
        else:
            n = len(num_list)

        for i in num_list:
            sigma += (i-mean)**2
        
        stdev = math.sqrt(sigma/n)
        
        self.standard_deviation = stdev
        
        return self.standard_deviation

