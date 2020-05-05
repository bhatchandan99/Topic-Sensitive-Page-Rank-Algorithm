import sys, string, math
from math import log
from math import modf
import operator

import numpy as np

final = {}
datam={}
topic_array = []
d = 0.85

stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'no', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

for word in open('input_topic.txt', 'r').readline().split():
    topic_array.append(word)

def parse_file():
    #print(datam)
    for word in topic_array:
        for key in datam.keys():
            if key  not in final:
                if word in datam[key]:

                    final[key]= datam[key]
                    final[key].remove(word)

    rows,cols = (len(final),len(final))
    arr = [[0 for i in range(cols)] for j in range(rows)]

    final_s= {}
    for x in sorted(final):
        final_s[x] = final[x]

    i =  0
    j  = 0

    for key1 in final_s:
        j = 0
        for key2 in final_s:

            arr[i][j] = float(len([value for value in final_s[key1] if value in final_s[key2]]))/float(len(final_s[key2]))
            if j<len(final_s):
                j = j+1
        if i< len(final_s):
            i= i+1

    col_sum = list(sum(z) for z in zip(*arr))
    i =  0
    j  = 0
    for key1 in final_s:
        j = 0
        for key2 in final_s:

            arr[i][j]= arr[i][j]/float(col_sum[i])

            if j<len(final_s):
                j = j+1
        if i< len(final_s):
            i= i+1

    arr= np.array(arr)

    arr = d*arr

    r = [1.0/float(len(final_s)) for i in range(len(final_s))]

    r_random = [1.0/float(len(final_s)) for i in range(len(final_s))]
    r_random = np.array(r_random)
    r_random = (1-d)*r_random
    #print(r_random)
    it = 0
    while(it<20):

        r = np.dot(arr,r)
        r= r+r_random
        print(r)

        it = it+1


    r = np.array(r)


    maximum= np.max(r)
    ans_index= np.argmax(r, axis=0)


    print("Final Ranks")
    print(r)
    print("Page with highest rank:",ans_index)
    #print(final[ans_index])
#######################################################################
if __name__ == "__main__":

        f = open('sample_data_used_for_this.txt', 'r')

        data = f.read()
        splat = data.split("\n\n")

        ind = 0
        for para in splat:

            datam[ind]=  list(np.setdiff1d([word.lower() for word in para.split()],stop_words))
            if(ind > -1):
                ind= ind+1


        parse_file()
