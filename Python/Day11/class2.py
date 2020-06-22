class SortCheck:
    def is_sorted(self, s):
        '''
        :param
         s (list): List containing int or str values
        :return:
         Returns True if the list is sorted, False otherwise
        '''
        if s == sorted(s):
            return True
        else:
            return False
        # for i in range(len(s)):
        #     if s[i] < s[i + 1]:
        #         return True
        #     else:
        #         return False
list1 = [1,2,3,4]
list2 = [4,3,5,6,8,2]
list3 = ['a','b','c']
list4 = ['a','h','c','i']

obj = SortCheck()
# print(obj.is_sorted.__doc__)
print(obj.is_sorted(list1))