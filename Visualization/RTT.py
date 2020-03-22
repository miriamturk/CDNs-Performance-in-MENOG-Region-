import json
import os

directory = "/Users/mariannejbeyli/Documents/ESIB/Semestre 4/Ecosystemes et evolution de l'internet/projet/data"

def avg(l):
    if(len(l)==0): return 0
    return sum(l)/len(l)

def getRTTaverage(f):
    results = []
    with open(f, 'r') as file:
        res = json.load(file)
    for dico in res:
        for rtt in dico['result']:
            if 'rtt' in rtt.keys():
                if rtt['rtt']:
                    results.append(rtt['rtt'])
    return avg(results)

def totalAverage(directory):
    avgs = {}
    d = directory
    for country in os.listdir(directory):
        if country != ".DS_Store":
            avgs[country] = {}
            d = directory + "/" + country
            for cdn in os.listdir(d):
                if cdn != ".DS_Store":
                    dd = d + "/" + cdn
                    l = []
                    for site in os.listdir(dd):
                        jfile = dd + "/" + site
                        l.append(getRTTaverage(jfile))
                        if avg(l) != 0:
                            avgs[country][cdn] = avg(l)
    return avgs

            
        
                
