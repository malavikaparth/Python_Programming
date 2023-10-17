from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+") # match words


class MRMostUsedWord(MRJob):

    def mapper_get_words(self, _, line):
        '''
        this mapper yields each word in the line
        :param _: None
        :param line: one line from the input file
        :return: (word, 1)
        '''
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        '''
        this combiner sums the words we've seen so far
        :param word: word obtained from the mapper
        :param counts: 1
        :return: (word, sum)
        '''
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        '''
        this reducer sends all (num_occurrences, word) pairs to the same final reducer.
        num_occurrences is so we can easily use Python's max() function.
        :param word: word obtained from the combiner
        :param counts: the number of occurrences of the word from the result of the combiner
        :return: (None, (sum(counts), word))
        '''
        yield None, (sum(counts), word)

    def reducer_find_max_word(self, _, word_count_pairs):
        '''
        this final reducer gets the most commonly used word
        :param _: discard the key; it is just None
        :param word_count_pairs: each item of word_count_pairs is (count, word),
        :return: (key=counts, value=word)
        '''
        yield max(word_count_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]


if __name__ == '__main__':
    MRMostUsedWord.run()   # where MRMostUsedWord is your job class
