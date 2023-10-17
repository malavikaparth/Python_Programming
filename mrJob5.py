'''
 TASK 2: no of followers

'''

from mrjob.job import MRJob
from mrjob.step import MRStep


class countofNum(MRJob):

    def mapper1(self,_,line):
        '''
        This will split the file based on tab character as a delimiter.
        This will give us a list of all users. The split will get only
        the users.This is considered as key.
        '''
        key = line.split('\t')[:1]
        #This line contain all followers
        users = line.split('\t')[1:]
        if(users != []):
            value = users[0].split(',')
        else:
            #To deal with the problem of having a user with no following
            value = []
        values = len(value)
        yield key, values

    '''
    First reducer which gives key as none and 
    value as a tuple of key and sum(value)
    '''
    def reducer1(self, key, value):
        yield None,(sum(value),key)

    '''
    This reducer takes a key value pair as input. Here key is a dummy value
    and value as uder id and the number of followers.
    This will then sort them in descending order based on the number of followers. 
    '''

    def reducer2(self, _, value):
        sorted_values = sorted(value, reverse= True)
        yield sorted_values,_

    '''
    The steps for running the mrJob
    '''
    def steps(self):
        return[
            MRStep(mapper=self.mapper1, reducer = self.reducer1),
            MRStep(reducer = self.reducer2)
        ]


if __name__ == '__main__':
    countofNum.run()