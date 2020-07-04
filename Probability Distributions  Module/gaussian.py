import math
from convertfile import ConvertFile
from graphs import GraphCreator


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

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return (1.0/(self.standard_deviation * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.standard_deviation) ** 2)
    
    def histogram(self):

        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            Histogram chart
        """
        x = 2

        data = self.return_list()

        pdf = self.pdf(x)

        graph = GraphCreator(data,pdf)
        
        chart = graph.plot_histogram()
        
        return chart

    def histogram_pdf(self):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        x = 2

        data = self.return_list()

        pdf = self.pdf(x)

        graph = GraphCreator(data,pdf)
        
        chart = graph.plot_histogram_pdf()
        
        return chart

