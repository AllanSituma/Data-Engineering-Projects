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

