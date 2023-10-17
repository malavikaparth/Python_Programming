'''
A job to count the number of e in the text
'''

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"['e']+")

class countofE(MRJob):
    def mapper(self,_,line):
        for word in WORD_RE.findall(line):
            yield word,1

#This will print all words in the text with value 1 next to it like

    def combiner(self,word,count):
        yield word,sum(count)

    def reducer(self,word, count):
        yield None, (sum(count), word)

if __name__ == '__main__':
    countofE.run()