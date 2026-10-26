
def split_and_join(line):
    # write your code here
    words=line.split()
    hyphenated_string='-'.join(words)
    return hyphenated_string
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)