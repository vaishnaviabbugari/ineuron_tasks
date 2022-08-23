import logging

logging.basicConfig(filename="abc.log",  level= logging.INFO ,format=("%(name)s %(levelname)s %(asctime)s %(message)s"))

class string:
    """these are all string related modules"""

    def string_extraction(self,s):
        """this function helps in extracting the given list from index 1 to 300 with a jump of 3"""
        self.s= s
        try:
            logging.info("string extraction is succesfull and given string is ; %s",  self.s )
            self.s= s[0:300:3]
            return self.s
        except Exception as e:
            logging.error(e)

    def string_reverse(self,s):
        """this function helps in string reversion"""
        self.s = s
        try:
            logging.info("string reverse is successfull and %s",self.s)
            self.s= s[::-1]
            return self.s
        except Exception as e:
            logging.error(e)

    def string_split(self,s):
         """this function helps in splitting of string"""
         self.s = s
         try:
            logging.info("string splitting is is succesfull and %s" , self.s)
            self.s = s.upper()
            self.s = s.split()
            return self.s
         except Exception as e:
            logging.error(e)

    def string_lower(self,s):
        """this function helps in convert the whole string into lower case"""
        self.s = s
        try:
            logging.info("string lowering is done and given string is %s",self.s)
            self.s = s.lower()
            return self.s
        except Exception as e:
            logging.error(e)

    def string_capitalization(self,s):
        """this function helps in capitalization of whole string"""
        self.s = s
        try:
            logging.info("string capitalization is done and given string is %s " ,self.s)
            self.s = s.capitalize()
            return self.s
        except Exception as e:
            logging.error(e)

    def string_expandtabs(self,s):
        """string expand tabs"""
        self.s = s
        try:
            logging.info("expand tabs is done and given string is %s" , self.s.expandtabs())
            self.s = s.expandtabs()
            return self.s
        except Exception as e:
            logging.error(e)


    def string_replacement(self,s):
        """this function helps in string replacement"""
        self.s = s
        try:
            logging.info("trying string repplacement")
            val = self.s.replace("python","java").replace("class","hahaha")
            return val
        except Exception as e:
            logging,error(e)

    def filter_out_vowels(self,s):
        """this func helps in filtering out vowels"""
        self.s = s
        try:
            logging.info("filtering out vowels is in process")
            i = 0
            v = 'aeiou'
            s = s.lower()
            while i < len(s):
                if s[i] in v:
                    print(s[i])
                i = i + 1
        except Exception as e:
            logging.error(e)


s = "this is My First Python programming class and i am learNING python string and its function"
obj =string()
print(obj.string_extraction(s))
print(obj.filter_out_vowels(s))
print(obj.string_replacement(s))
print(obj.string_lower(s))
print(obj.string_expandtabs(s))
print(obj.string_capitalization(s))
print(obj.string_split(s))
print(obj.string_reverse(s))
