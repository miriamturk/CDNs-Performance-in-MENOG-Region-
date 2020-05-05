import json
import os

directory = "..../menog-rtt-cdn-measure/measurements/data"

with open(".../menog-rtt-cdn-measure/asn_prefix.json","r") as file:
    probes = json.load(file)


def getAllResults(directory):
    results = {}
    d = directory
    for country in os.listdir(directory):
        if country != ".DS_Store":
            results[country] = {}
            d = directory + "/" + country
            for cdn in os.listdir(d):
                if cdn != ".DS_Store":
                    dd = d + "/" + cdn
                    dico = {}
                    for site in os.listdir(dd):
                        jfile = dd + "/" + site
                        dico = getResultsPerFile(jfile,dico)
                    results[country][cdn] = dico
    return results       


def getResultsPerFile(f, d):
    with open(f, 'r') as file:
        res = json.load(file)
    for dico in res:
        probe = dico["prb_id"]
        if dico["min"] == -1:
            continue
        if probe in d.keys():
            d[probe] = min(d[probe],dico["min"])
        else:
            d[probe] = dico["min"]
    return d

def weighedAvgRTT(directory):
    results = getAllResults(directory)
    for country in results.keys():
        for cdn in results[country].keys():
            value = 0
            total_prefixes = 0
            for probe in results[country][cdn].keys():
                value += probes[str(probe)][1]*results[country][cdn][int(probe)]
                total_prefixes += probes[str(probe)][1]
            value = value/total_prefixes
            results[country][cdn] = value
    return results



            
