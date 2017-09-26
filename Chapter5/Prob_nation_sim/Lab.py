# About Data structure
import sys
sys.path.append("D:\Python\Matrix")

from matutil import *
from vecutil import *
from mat import Mat
from vec import Vec

# About File I/O
import pickle

def readFile2lists(f_name):
    try:
        with open(f_name,'r') as buf:
            # 'value' = the content of each line
            lists=[value.split(maxsplit=1) for value in buf]

            # each[0] is name of country, each[1] is list of vote
            for each in lists:
                # each[1] is originally str
                # So to calculate similarity, we should change str to int
                each[1]=[int(i) for i in each[1].split()]
            # lists is list that consists of name of country and list of vote
            return lists
                                # By maxsplit=1, it return list that have elements which are 2-elements list
    except IOError as ioe:
        print(str(ioe))
        return None

def votingList2coldict(lists): return {each[0]:
                    Vec(set(range(len(each[1]))),{d:f for d,f in zip(range(len(each[1])),each[1]) })
                for each in lists }

def writeResult2File(results):
    try:
        with open('vote_similarity_result.txt','w') as buf:
            # Before write to the File, sorting executed
            print('Pickling started')
            print(sorted( [ (value,key) for value,key in results.f.items() ] ),file=buf)
            # pickle.dump(sorted( [ (value,key) for value,key in results.f.items() ] ),buf)
    except IOError as ioe:
        print(str(ioe))
        return None

