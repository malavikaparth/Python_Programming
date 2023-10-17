from mrjob.job import MRJob
from mrjob.step import MRStep

'''
The mapper processes the input data and emits (key, value) pairs, 
and the reducer processes the output from the mapper and produces the final output for this step.
The key and value arguments are the key and value of the input (key, value) pair being processed by the mapper. 
In MRJob, the input data is automatically read from the input file and parsed into (key, value) pairs, 
where the key and value are strings by default. 
The mapper1() method processes each (key, value) pair and emits zero or more (key, value) pairs as output
'''
class myFirstMRJob(MRJob):
    def mapper1(self, key, value):



    def reducer1(self, key, values):


    '''
    The mapper processes the output from the first step and emits (key, value) pairs,
    and the reducer processes the output from the mapper and produces the final output for this step
    '''
    def mapper2(self, key, value):

    # process the output from reducer1 and emit (key, value) pairs

    def reducer2(self, key, values):

    # process the output from mapper2 and produce the final output for this step
    '''
    The third and final step has a mapper, mapper3, and a reducer, reducer3.
    The mapper processes the output from the second step and emits (key, value) pairs,
    and the reducer processes the output from the mapper and produces the final output for the entire MRJob.
    '''
    def mapper3(self, key, value):

    # process the output from reducer2 and emit (key, value) pairs

    def reducer3(self, key, values):

    # process the output from mapper3 and produce the final output for this step

    #implement the steps() method to define the steps of your MRJob
    #the steps() method defines three steps for the MRJob
    def steps(self):
        return[
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2),
            MRStep(mapper=self.mapper3, reducer=self.reducer3)
        ]