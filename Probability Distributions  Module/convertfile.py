class ConvertFile:

    """Class that takes in a file and converts it into a list

    Attributes:
        file - A text file with a list of floats

    """

    def __init__(self,path_to_file):
        self.file_name = path_to_file
        self.data_list = []

    def return_list(self):
        
        """Method that returns a list of floats
            from a text file

            Args: None

            Returns: a list of floats
        """

        with open(self.file_name) as file:
            list_nums = self.data_list
            line = file.readline()
            while line:
                list_nums.append(int(line))
                line = file.readline()
        file.close()
        return  list_nums
