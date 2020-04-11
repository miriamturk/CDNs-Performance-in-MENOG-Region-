import json
import requests
import glob
import os
import ntpath
from ripe.atlas.cousteau import Probe


                    
def get_asn_prefix(asn):

    api_url = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource={}'.format(asn)

    response = requests.get(api_url)

    if response.status_code == 200:
        asn_prefix_list = json.loads(response.content.decode('utf-8'))
        nb_prefixes = len(asn_prefix_list["data"]["prefixes"])
        return nb_prefixes
    else:
        return None
    

#This code outputs a dictionary in the form {"probe_id":("asn_num","prefix_count")} 
with open('destinationNetworks.json', 'r') as f:
    networks = json.load(f)
with open('countries.json', 'r') as f:
    countries = json.load(f)

res={}
i=1
while(i<=2):
    for countries_code in countries["countries{}".format(i)].values():
        for cdn_name in networks.keys():
            path="measurements/data/{}/{}/*.json".format(countries_code,cdn_name)
            for filepath in glob.iglob(path):
                with open(filepath) as f:
                    data = json.load(f)
                for val in data:
                    if (not val["prb_id"]in res):
                        asn=Probe(id=val["prb_id"]).asn_v4
                        res[val["prb_id"]]=(asn,get_asn_prefix(asn))
    i=i+1
with open("asn_prefix.json","w") as f:
    json.dump(res,f,indent=4, sort_keys=True)
