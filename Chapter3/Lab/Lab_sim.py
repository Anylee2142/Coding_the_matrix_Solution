import time

most_sim_val=46
least_sim_val=-46

def list_dot(u,v): return sum([a*b for (a,b) in zip(u,v)])
#def list_dot(u,v): return sum([1 if (a,b)=0,0 else a*b in zip(u,v)])

def readFile2lists(f_name):
    try:
        with open(f_name,'r') as buf:
            # 'buf' consists of each line
            return [each.split(maxsplit=3) for each in [each for each in buf]]
    except IOError as ioe:
        print(str(ioe))
        return None

def create_voting_dict(strlist):
    # 'each_line' = [1, 1, -1 ,...]
    return { each_line[0] : [int(each) for each in each_line[3].split()] for each_line in strlist}

def create_voting_dict_state(strlist):
    # 'each_line' = [1, 1, -1 ,...]
    return { each_line[2] : [int(each) for each in each_line[3].split()] for each_line in strlist}

def policy_compare(sen_a, sen_b, voting_dict):
    return list_dot(voting_dict[sen_a],voting_dict[sen_b])

def most_similar(sen,voting_dict):
    name_list=[each for each in voting_dict.keys()]
    name_list.remove(sen)

    # start value 'sim' shouldn't be lower than 'least_sim_val'
    (close_sen, sim) = 0, least_sim_val

    for each in name_list:
        each_sim=policy_compare(sen,each,voting_dict)
        if each_sim>sim: (close_sen,sim) = each, each_sim

    return close_sen

def least_similar(sen,voting_dict):
    name_list = [each for each in voting_dict.keys()]
    name_list.remove(sen)

    # start value 'sim' shouldn't be higher than 'most_sim_val'
    (close_sen, sim) = 0, most_sim_val

    for each in name_list:
        each_sim = policy_compare(sen, each, voting_dict)
        if each_sim < sim: (close_sen, sim) = each, each_sim

    return close_sen

# a[0]*x + a[1]*x + a[2]*x + ...
def find_average_similarity(sen,sen_set,voting_dict):
    each_sim=[policy_compare(sen,each,voting_dict) for each in sen_set]
    return sum(each_sim)/len(sen_set)

# (a[0]+a[1]+a[2]+ ...)*x
def find_average_record(sen_set,voting_dict):
    sen_voting=[voting_dict[each] for each in sen_set]

    (vote_count, sen_count) = len(sen_voting[0]) , len(sen_set)

    return [sum( [sen_voting[opinion][each] for opinion in range(sen_count)] ) / sen_count
            for each in range(vote_count)]

def bitter_rivals(voting_dict):
    (rival_a, rival_b, sim)=None, None, most_sim_val

    for each in voting_dict.keys():
        far_from_each=least_similar(each,voting_dict)
        rival_sim=policy_compare(each, far_from_each,voting_dict)
        # print('\t'+each,far_from_each)
        if rival_sim < sim :
            (rival_a, rival_b, sim) = each, far_from_each, rival_sim
            print(rival_a, rival_b, sim)

    print('Bitter rivals are '+rival_a+' and '+rival_b)

def tendencyCheck(sen):
    Republic_list = {each[0] for each in voting_list if each[1] == 'R'}
    Democrats_list = {each[0] for each in voting_list if each[1] == 'D'}

    average_Republic_record = find_average_record(Republic_list, voting_dict)
    average_Democrats_record = find_average_record(Democrats_list, voting_dict)

    return [list_dot(voting_dict[sen],average_Democrats_record), list_dot(voting_dict[sen],average_Republic_record)]

def findClosest2DemocratsOrRepublic(dict,voting_list,StateOrSenator,party):
    # StateOrSenator:
    #   0 = Senator
    #   2 = State

    # party: below chars are up to txt files, check its format
    #   'R' = Republic
    #   'D' = Democrats
    list={each[StateOrSenator] for each in voting_list if each[1]==party}

    average_record=find_average_record(list,dict)

    (close, sim)= None, least_sim_val
    for each in dict.keys():
        each_sim = list_dot(dict[each],average_record)
        if each_sim > sim:
            (close, sim) = each, each_sim
    return close
