from mrjob.job import MRJob
from mrjob.step import MRStep
#To count the the number of words in a text file
class countWords(MRJob):
    count = 0
    '''
    In the context of Mrjob, the yield keyword is used to indicate that the function
     will produce one or more key-value pairs as output. These key-value pairs can then 
     be processed by other parts of the MapReduce job, such as the reducer function
     '''
    def mapper(self, _, line):
        for words in line.split():# Splits at space
            if len(words) > 0:
                yield words,1

    def reducer(self,words,count):
        yield words,sum(count)
'''
    def configure_args(self):
        super(countWords, self).configure_args()
        self.add_file_arg('--input', help='Input file')
        self.add_passthru_arg('--output', type=str, help='Output file')
'''
task0 = countWords(args = [])
with open('example', 'r') as fi:
    row = [line for line in fi]
    output = list(MRJob.runJob(row, task0))
    output = sorted(output, key=lambda x: -x[1])
#if __name__ == '__main__':
#    countWords.run()


