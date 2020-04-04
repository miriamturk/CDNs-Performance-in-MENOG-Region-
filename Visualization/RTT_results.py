import json
import os

directory = "C:/Users/Mariam Al-Turk/Desktop/Sem4/Ecosystemes/Ptojet_CDNs in MENOG Region/CDNs-Performance-in-MENOG-Region-/atlas-measurement CDN/measurements/data"

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
    l_rtt ={}
    d = directory
    for country in os.listdir(directory):
        if country != ".DS_Store":
            l_rtt[country]={}
            d = directory + "/" + country
            for cdn in os.listdir(d):
                if cdn != ".DS_Store":
                    dd = d + "/" + cdn
                    l=[]
                    for site in os.listdir(dd):
                        jfile = dd + "/" + site
                        l = getRTT(jfile)
                        if l != []:
                            l_rtt[country][cdn] = l
    return l_rtt

                
RTT(directory)
