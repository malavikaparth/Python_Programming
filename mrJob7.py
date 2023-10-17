'''
 TASK 1: Average

'''

from mrjob.job import MRJob

class averageOfFollowers(MRJob):

    def mapper(self,_,line):
        '''
        This will split the file based on tab character as a delimiter.
        This will give us a list of all users
        '''
        users = line.split('\t')[1:]
        '''
        If the user have followers which is a comma separated numbers,
        then it will be split into values based on the comma.
        '''
        if(users != []):
            value = users[0].split(',')
        else:
            '''
            If the user do not have any followers then the variable value is assigned to 
            a empty list.
            '''
            #To deal with the problem of having a user with no following
            value = []
        values = len(value)
        '''
        This will give us result of null as key and  as the number of followers and 1 as value.
        1 is added along so as to get the number of users to find the average.
        The number of users will always be 1, thus replacing it by 1 will allow us for easy calculation.
        '''
        yield None, (values,1)

    '''
    The reducer function here takes none as key and list of values as input.
    '''
    def reducer(self,key,value):
        #This is the variable to get the sum of all lengths
        value_sum = 0
        #This is the variable to get the total number of users
        key_sum = 0
        #This is the variable to assign the final average
        avg = 0
        for i,j in value:
            value_sum += i
            key_sum += j
        avg = value_sum/key_sum
        yield None,avg


if __name__ == '__main__':
    averageOfFollowers.run()