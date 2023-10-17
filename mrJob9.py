from mrjob.job import MRJob

class MaxMonthlyTempDiff(MRJob):
    def mapper(self, _, line):
        # Split the line into fields
        fields = line.split(',')

        # Skip the first three lines
        if fields[0] == "Variable:" or fields[0] == "Country:" or fields[0] == "":
            return

        # Get the year and the monthly temperatures
        year = fields[0]
        temps = list(map(float, fields[1:]))

        # Compute the temperature difference for each month
        diffs = [max(temps[i], temps[i+1]) - min(temps[i], temps[i+1]) for i in range(0, 11)]

        # Yield the year and the maximum temperature difference
        yield year, max(diffs)

    def reducer(self, year, diffs):
        # Find the maximum temperature difference for the year
        max_diff = max(diffs)

        # Yield the year and the maximum temperature difference
        yield year, max_diff

if __name__ == '__main__':
    MaxMonthlyTempDiff.run()