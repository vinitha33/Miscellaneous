class StringCheck():
    def checkLower(self, s):
        '''
        :param
         s (string): A string taken as input
        :return:
         Returns the string in lowercase
        '''
        try:
            if s.islower():
                print(s)
            else:
                print(s.lower())
        except Exception as E:
            print("Exception occured as ", E)


    def checkUpper(self, s):
        '''
        :param
         s (string): A string taken as input
        :return:
         Returns the string in uppercase
        '''
        try:
            if s.isupper():
                print(s)
            else:
                print(s.upper())
        except Exception as E:
            print("Exception occured as:", E)

    def stringSplit(self, s):
        '''
        :param
         s (string): A string indicating full name
        :return:
         Splits the original string and returns 3 string as first, middle and last name
        '''
        try:
            full_name = s.split()
            print("First name:", full_name[0])
            print("Middle name:", full_name[1])
            print("Last name:", full_name[2])
        except Exception as E:
            print("Exception occured as", E)


    def checkVowels(self, s):
        '''
        :param
         s (string): A string value
        :return:
         Check if it has vowels or not and prints output accordingly
        '''
        vowel_set = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(len(s)):
            if s[i] in vowel_set:
                count = count + 1
            else:
                continue
        if count > 0:
            print("String has vowels")
        else:
            print("String has no vowels")


my_name = "Vinitha Muralidharan Nair"
my_name1 = 123
obj = StringCheck()
print("*****1*****")
print(obj.checkLower.__doc__)
obj.checkLower(my_name)
print("*****2*****")
print(obj.checkUpper.__doc__)
obj.checkUpper(my_name)
print("*****3*****")
print(obj.stringSplit.__doc__)
obj.stringSplit(my_name)
print("*****4*****")
print(obj.checkVowels.__doc__)
obj.checkVowels(my_name)

