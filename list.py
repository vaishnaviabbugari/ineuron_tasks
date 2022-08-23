import logging

logging.basicConfig(filename="list.log",level = logging.DEBUG,format=("%(name)s %(levelname)s %(asctime)s %(message)s"))

class list:
    def __init__(self, l):
        self.l = l

    def reverse_list(self,l):
        """this function helps in reversing the whole list"""
        try:
            val = self.l[::-1]
            logging.info(val)
            return val
        except Exception as e:
            logging.error(e)

    def accesing_234(self,l):
       """this func helps in accesing 234"""
       output_list=[]
       try:
           for i  in self.l:
               if type(i)==list or type(i)==tuple:
                   for j in i:
                       if type(j)==int:
                           if j == 234:
                               output_list.append(j)
               if type(i)==dict:
                   for k,v in i.items():
                       if k == int:
                           if k == 234:
                               output_list.append(k)
           logging.info(output_list)
       except Exception as e:
           logging.error(e)

    def access_456_in_data(self,l):
       '''This function access 456'''
       dummy_list = []
       try:
           for i in self.l:
               if type(i) == list or type(i) == tuple:
                   for j in i:
                       if type(j) == int:
                           if j == 456:
                               dummy_list.append(j)
               if type(i) == dict:
                   for k, v in i.items():
                       if type(k) == int:
                           if k == 456:
                               dummy_list.append(k)
           logging.info(dummy_list)
       except Exception as e:
            logging.exception(e)

    def extracting_sudh(self,l):
        """helps in extracting sudh from list entity"""
        dummy_list=[]
        try:
            for i in self.l:
                if type(i)==list or type(i)==tuple:
                    for j in i :
                        if type(j)!= int :
                            if j == "sudh":
                                dummy_list.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k) != int or type(v) != int:
                            if k == "sudh" or v == "sudh":
                                dummy_list.append(v)
            logging.info(dummy_list)
        except Exception as e:
            logging.error(e)

    def extracting_values(self,l):
        """extracting values from dict entity"""
        dummy_list=[]
        try:
            for i in self.l:
                if type(i)==dict:
                    for k,v in i.items():
                        dummy_list.append(v)
            logging.info(dummy_list)
        except Exception as e:
            logging.error(e)

    def extracting_keys(self,l):
        """extracting keys frm dict entity"""
        dummy_list=[]
        try:
            for i in self.l:
                if type(i)==dict:
                    for k , v in i.items():
                        dummy_list.append(k)
            logging.info(dummy_list)
        except Exception as e:
            logging.error(e)
