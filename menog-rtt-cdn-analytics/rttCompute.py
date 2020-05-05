import json
import os
import pandas as pd
import copy

directory = "C:/Users/Mariam Al-Turk/Desktop/2eme Telecom/Sem4/Ecosystemes/Ptojet_CDNs in MENOG Region/CDNs-Performance-in-MENOG-Region-/menog-rtt-cdn-measure/measurements/data"

def getRTT(f):
    results = []
    with open(f, 'r') as file:
        res = json.load(file)
    for dico in res:
        for rtt in dico['result']:
            if 'rtt' in rtt.keys():
                if rtt['rtt']:
                    results.append(rtt['rtt'])
    return results

def RTT(directory):
    l_rtt =[]
    d = directory
    for country in os.listdir(directory):
        if country != ".DS_Store":
            dico = {}
            dico ['country'] = country
            d = directory + "/" + country
            for cdn in os.listdir(d):
                dico['cdn']=cdn
                if cdn != ".DS_Store":
                    dd = d + "/" + cdn
                    l=[]
                    for site in os.listdir(dd):
                        jfile = dd + "/" + site
                        l = getRTT(jfile)
                        if l != []:
                            for value in l:
                                dico['values'] = value
                                dico_copy = copy.deepcopy(dico)
                                l_rtt.append(dico_copy)
    return l_rtt


results = RTT(directory)
print (results, file=open('output.txt', "a"))

rtt_results = RTT(directory)
csv_columns = ['country','cdn', 'values']
df = pd.DataFrame(rtt_results, columns = csv_columns)
df.to_csv('graphs/results.csv')
