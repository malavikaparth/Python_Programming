'''
 Task 4: Temperature in Belgium
'''

from mrjob.job import MRJob
from mrjob.step import MRStep

class maxAndMinTemp(MRJob):

    def mapper(self,_,line):
        '''
        Splitting the input line using , as delimiter.
        '''
        data = line.split(',')
        #Declaring an empty List
        #To not consider the first 3 lines
        if(data[0] == "Variable:" or data[0] == "Country:" or data[0] == ""):
            return
        #To extract only year from the whole data.
        year = data[0]
        # To extract temperatures from the whole data.
        temperatures = data[1:]
        yield year,temperatures


    def reducer(self,key,value):
        temp = list(value)
        diff = []
        diff1 = []
        diff2 = []
        maxmin = []
        for i in temp:
            for j in range(0,len(i)):
                diff.append(i[j])

        diff1 = diff[:12]
        diff2 = diff[12:]

        for i in range(0,len(diff1)):
            maxmin.append(float(diff1[i]) - float(diff2[i]))

        yield key,maxmin




if __name__ == '__main__':
    maxAndMinTemp.run()