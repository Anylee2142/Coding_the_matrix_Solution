from Lab import *

voting_list=readFile2lists('voting_record_dump109.txt')
voting_dict=create_voting_dict(voting_list)
state_dict=create_voting_dict_state(voting_list)

# for k,v in voting_dict.items():
#     print(k,v)
#
# for k,v in state_dict.items():
#     print(k,v)

#
# sen='Obama'
# print(sen+"'s most, least similar senator")
# print('\t'+most_similar(sen,voting_dict))
# print('\t'+least_similar(sen,voting_dict))
#
# print("Chafee's most similar senator")
# print('\t'+most_similar('Chafee',voting_dict))
# print("Santorum's least similar senator")
# print('\t'+least_similar('Santorum',voting_dict))
# for each in voting_list:
#     print(each)

# # 3.12.4  ------------------------------------------------------
# Democrats_list={each[0] for each in voting_list if each[1]=='D'}
# Full_list={each[0] for each in voting_list}
# Republic_list={each[0] for each in voting_list if each[1]=='R'}
#
# print(find_average_similarity('Obama',Democrats_list, voting_dict))
# print(find_average_similarity('Obama',Republic_list, voting_dict))

# part of 'most_similar'
# start=time.time()
# (close_sen, sim) = None, least_sim_val
# for name in voting_dict.keys():
#     each_sim = find_average_similarity(name,Democrats_list,voting_dict)
#     if each_sim > sim: (close_sen, sim) = name, each_sim
# print(close_sen) # most similar senator with 'Democrats_list'
# print(time.time()-start)

# # 3.12.8  ------------------------------------------------------
# start=time.time()
# average_Democrats_record=find_average_record(Democrats_list,voting_dict)
# (close_sen, sim) = None, least_sim_val
# for name in voting_dict.keys():
#     each_sim = list_dot(voting_dict[name],average_Democrats_record)
#     if each_sim > sim:
#         (close_sen, sim) = name, each_sim
# print(close_sen) # most similar senator with 'Democrats_list'
# print(time.time()-start)

'''------------------------------------------------------------
Above 2, '3.12.4' and '3.12.8' are functioning same
But how it functions is different

3.12.4 = a[0]*x+a[1]*x+...+a[n]*x = O(n**2)
3.12.8 = (a[0]+a[1]+...+a[n])*x   = O(n)
You can check it with execution time.
'''#------------------------------------------------------------

# # Finding bitter rivals
# bitter_rivals(voting_dict)

# # who is the closest senator to Republic?
# print(findClosest2DemocratsOrRepublic(voting_dict,voting_list,0,'R'))

# # who is the closest senator to Democrats?  = # 3.12.8
# print(findClosest2DemocratsOrRepublic(voting_dict,voting_list,0,'D'))

# # which state is the closest one to Republic
# print(findClosest2DemocratsOrRepublic(state_dict,voting_list,2,'R'))

## which state is the closest one to Democrats
# print(findClosest2DemocratsOrRepublic(state_dict,voting_list,2,'D'))

# # Is John McCain really independent to party?
# print(tendencyCheck('McCain'))

# # Is Barack Obama really drastic?
# print(tendencyCheck('Obama'))

# # which two senators are bitter-rivals?
#bitter_rivals(voting_dict)

# # which senator has the worst rival ? (lowest dot product)
# same as just above
bitter_rivals(voting_dict)
