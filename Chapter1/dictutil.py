def dict2list(dct,keylist): return [val
                                    for (key,val) in dct.items()
                                    for each in keylist
                                    if key is each]

def list2dict(L,keylist): return { key:set(val.split())
                                   for (key,val) in list(zip(keylist,L))}

def listrange2dict(L): return list2dict(L,range(len(L)))

def makeInverseIndex(f_name):
    try:
        with open(f_name,'r') as buf:
            lists=[each for each in buf]
            return listrange2dict(lists)
    except IOError as ioe:
        print(str(ioe))
        return None
#

def storeInverseIndex(dct):
    try:
        with open('InverseIndex.txt','w') as buf:
            for (k,v) in dct.items():
                print(k,v,file=buf)
    except IOError as ioe:
        print((str(ioe)))
        return None

def orSearch(inverseIndex,query):
    return {k for (k,v) in inverseIndex.items() for each_qry in query if each_qry in v}

def andSearch(inverseIndex,query):
    return {k for (k,v) in inverseIndex.items() if set(query) & v == set(query)}

dct=makeInverseIndex('stories_small.txt')

# storeInverseIndex(dct)

# example
print(orSearch(dct,['Derrick']))
print(andSearch(dct,['Harvard-educated','unfolded']))