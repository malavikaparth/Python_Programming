'''
a job that calculates the occurence of a word in a text file
'''
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class commonWord(MRJob):
    def mapper(self,_,line):
        for word in WORD_RE.findall(line):
            yield word,1

#This will print all words in the text with value 1 next to it like

    def combiner(self,word,count):
        yield word,sum(count)

    '''
    def reducer(self,word, count):
        yield None, (sum(count), word)
'''
if __name__ == '__main__':
    commonWord.run()
'''
NOTE
"a"     1
"while" 1
"finding"       1
"that"  1
"nothing"       1
"more"  1
"happened"      1
"she"   1
"decided"       1
"on"    1

'''

