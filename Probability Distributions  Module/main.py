from gaussian import Gaussian
from dataclasses import dataclass


class PDCalculator(Gaussian):
    """ class that calculates statistics of different probability distributions 
    
    Currently on works for only gaussian distributions

    Attributes:
        distribution - Defines the distribution of the data
        Defining distributin : Gaussian 
    
    """

    def __init__(self,path_to_file,mu = 0,sigma = 1,distribution = None):
        super().__init__(path_to_file,mu,sigma)
        self.pdf = distribution


    def get_statistics(self):

        mean = self.get_mean()

        return mean


if __name__== '__main__':
    file_name = input('')
    calculate = PDCalculator(file_name)
    calculate.get_statistics()