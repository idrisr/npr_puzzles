import cProfile
import pstats
import os
DEBUG = False

def permutate(seq):
    #    print 'at top of function'
    """permutate a sequence and return a list of the permutations
    WARNING: if len(seq) > 10, expect significant amounts of time for full calculation"""
    
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            if DEBUG:
                print seq,'\t', 
                print k,'\t',
                print seq[:k],'\t',
                print seq[k+1:],'\t',
                print part, '\t'

            #print k, part  # test
            for m in permutate(part):
                x=seq[k:k+1] + m
                temp.append(x)
                #print m, seq[k:k+1], temp  # test
        return temp

def main(s_len) :
        s = 'a'*s_len
        if DEBUG:
            print 's','\t', 'k','\t', 's[:k]', '\t', 's[k+1:', '\t', 'part'
            print '-'*45

        l_perm = permutate(s)
        s_perm = set( l_perm )
        print 'Number of permutations with duplicates: %d' %len(l_perm)
        print 'Number of permutations without duplicates: %d' %len(s_perm)

def profile(num):
    path = 'output.txt'
    prof_path = 'profiles/'
    f = open(path, 'w')
    for i in range(0, num):
        exec_str = 'main(%d)' % i
        path = prof_path + str(i)
        cProfile.run( exec_str, path )
        p = pstats.Stats( path )

def check_wiki(s, path):
    """takes string 's' and path 'path'. Returns number of lines in 'path' which have only s on that line: grep ^s$ """
    command = 'grep -i ^%s$ %s' % (s, path)
    fp = os.popen(command).read().splitlines()
    return len(fp)

def check_string(l_anagrams, min_len, d):
    l = list()
    for anagram in l_anagrams:
        for split in range(min_len, len(anagram) - min_len+1):
            word1 = anagram[:split].lower()
            word2 = anagram[split:].lower()
            if word1 in d:
                if word2 in d:
                    l.append( word1 + ' ' + word2 )
    return l

def load_dict(path):
    f = open(path, 'r')
    d = dict()
    for line in f.readlines():
        d[line.lower().strip()] = None
    return d


if __name__ == '__main__':
    #num = 12 
    #profile(num)
    
    s = "Waynemanor"
    print "Creating Permutations"
    l_perm = permutate(s)
    s_perm = set( l_perm)

    print "Loading Dictionary"
    path = '/home/idris/work/npr_puzzle/12_12_waynemanor/wiki_title_dl.txt'
    #path = '/home/idris/work/npr_puzzle/12_12_waynemanor/wiki_test.txt'
    d = load_dict(path)

    print "Checking for existence"
    l_answers = check_string(s_perm, 3, d)
    s_answers = set( l_answers)
    l_answers = list(s_answers)
    l_answers.sort()
    print "combos found: %d" % len(l_answers)
    print "unique combos found: %d" % len(s_answers)
    p = 'output.txt'
    f = open(p, 'w')
    for item in l_answers:
        f.write(item+'\n')
    f.close()
