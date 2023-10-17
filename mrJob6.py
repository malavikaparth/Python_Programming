'''
 TASK 3: Common Following
'''


from mrjob.job import MRJob

class averageFollowers(MRJob):

    def mapper(self,_,line):
        '''
        This will split the file based on tab character as a delimiter.
        This will give us a list of all users. The split will get only
        the users.This is considered as key.
        '''
        key = line.split('\t')[:1]
        users = line.split('\t')[1:]
        if(users != []):
            value = users[0].split(',')
        else:
            #To deal with the problem of having a user with no following
            value = []
        #Trying to group values on keys
        for i in value:
            yield i,key


    def reducer(self,key,value):
        res = []
        '''
        Here key : contain all the followings
        value : contain the users id's
        '''
        for i in value:
            res.append(i)

        '''
        this will give the list of users and the follower common in them
        '''
        if(len(list(res)) > 1):
                yield res,key





if __name__ == '__main__':
    averageFollowers.run()