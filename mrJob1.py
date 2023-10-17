from mrjob.job import MRJob
'''
The mapper() method takes a key and a value as args 
here the key is ignored by using _ and a single line of text input is the value
output : yields as many key-value pairs as it likes
'''
class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        yield "chars", len(line) #the numbers of characters including space
        yield "words", len(line.split()) #the numbers of words
        yield "lines", 1 ##the numbers of lines

    def reducer(self, key, values):
        yield key, sum(values)

#We write step when we have more than one mapper reducer. It is not needed to write when we have just one.

#The final required component of a job file is these two lines at the end of the file, every time:
#Without them, your job will not work
if __name__ == '__main__':
    MRWordFrequencyCount.run()