import logging
logging.basicConfig(filename="list1.log",level = logging.DEBUG,format=("%(name)s %(levelname)s %(asctime)s %(message)s"))

class list_again:
    def __init__(self,l):
        self.l = l

    def extracting_list(self,l):
        """helps in extracting list entity"""
        output_list=[]
        try:
            for i in self.l:
                if type(i)==list:
                    output_list.append(i)
            logging.info(output_list)
        except Exception as e:
            logging.error(e)

    def extracting_dict(self,l):
        """helps in extracting dict entity"""
        output_list = []
        try:
            for i in self.l:
                if type(i)==dict:
                    output_list.append(i)
            logging.info(output_list)
        except Exception as e:
            logging.error(e)

    def extracting_tuple(self,l):
        """extarcting tuple"""
        output_list = []
        try:
            for i in self.l:
                if type(i) == tuple:
                    output_list.append(i)
            logging.info(output_list)
        except Exception as e:
            logging.error(e)

    def extracting_numeric_data(self,l):
        """this helps in extarcting numeric data from any data types"""
        output_list=[]
        try:
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            output_list.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int:
                            output_list.append(k)
                        if type(v)==int:
                            output_list.append(v)
            logging.info(output_list)

        except Exception as e:
            logging.error(e)

    def summation_of_numneric_data(self,l):
        """this gives us summation of all the numeric data present"""
        output_list=[]
        try:
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            output_list.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            output_list.append(k)
                        if type(v) == int:
                            output_list.append(v)
            logging.info(sum(output_list))

        except Exception as e:
            logging.error(e)

    def extarcting_odds(self,l):
        """this helps in extracting all the odd values"""
        output_list=[]
        odd_numbers=[]
        try:
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            output_list.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            output_list.append(k)
                        if type(v) == int:
                            output_list.append(v)
            for s in output_list:
                if s%2 != 0:
                    odd_numbers.append(s)
            logging.info(odd_numbers)
        except Exception as e:
            logging.error(e)

    def extracting_ineuron(self,l):
        output_list=[]
        try:
            for i in self.l:
                if type(i) == str or type(i) == list:
                    for j in i:
                        if type(j) == str:
                            if j == "ineuron":
                                output_list.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str:
                            if k == "ineuron":
                                 output_list.append(k)
                        if type(v) == str:
                            if v == "ineuron":
                                 output_list.append(v)
            logging.info(output_list)

        except Exception as e:
            logging.error(e)

    def number_of_occurence(self,l):
        output_list=[]
        try:
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        output_list.append(j)
                if type(i)==dict:
                    for k,in i.items():
                        output_list.append(k)
                        output_list.append(v)
            for s in set(output_list):
                logging.info(f'{s} -- > {output_list.count(s)}')
        except Exception as e:
            logging.error(e)
        else:
            logging.info("waw congartulations you have done it without any error")
        finally:
            logging.info("good luck and have a nice day ahead mam/sir")

    def no_of_keys(self,l):
        output_list=[]
        try:
            for i in self.l:
                if type(i)==dict:
                    for k in i.items():
                        output_list.append(k)
                        logging.info(len(output_list))
        except Exception as e:
            logging.error(e)
        else:
            logging.info("keep going")
        finally:
            logging.info("have a nice day")
