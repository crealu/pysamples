
def findLongestWord(str):
    arr = str.split()
    lengths = []
    for ar in arr:
        lengths.append(len(ar))
    lengths.sort()
    largest = lengths[len(lengths) - 1]
    return largest

findLongestWord('I am not a whale')
