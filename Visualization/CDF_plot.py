import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from RTT_results import *

CDN = []
countries = []

results = RTT(directory)

for country in results.keys():
    countries.append(country)

for cdn in results[countries[1]].keys():
    CDN.append(cdn)

print(countries)
print(CDN)

num_bins = 20

for country in countries:
    for cdn in CDN:
        if results[country]!={}:
            data = results[country][cdn]
            counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)
            cdf = np.cumsum(counts)
            plt.plot(bin_edges[1:], cdf/cdf[-1], label = cdn)

            #Print median
    ##        for q in [50, 90, 95, 100]:
    ##           print ("{}%% percentile: {}".format (q, np.percentile(data, q)))

    plt.grid(True)
    plt.legend(loc='lower right')
    plt.xlabel('RTT (milliseconds)')
    plt.ylabel('Cumulative fraction')        
    plt.title("Cumulative Distribution function of the latency in " + country)

    plt.savefig(country +".png")
    plt.show()
