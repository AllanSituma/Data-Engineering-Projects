from gaussian import Gaussian


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


    def get_results(self,val):

        """Switcher function to get results per user input

        Args:
            val(string) : string that is applied to the switcher,
                         to return any calculation.We may need to add a prompt 

        """
        
        return{ 'mean':self.get_mean(),
                'standard_dev':self.get_stdev(),
                'histogram':self.histogram(),
                'histogram_pdf':self.histogram_pdf()
                }.get(val)


if __name__== '__main__':
    file_name = input('')
    calculate = PDCalculator(file_name)
    calculation = input('')
    calculate.get_results(calculation)