import pandas as pd
import seaborn as sns; sns.set()
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from weighedMeanRTT import *

CDN = ["akamai", "amazonCloudfront", "azure", "cloudflare", "facebookcdn", "fastly", "googleCloud"]
countries = ["AE", "BH", "EG", "IQ", "IR", "KW", "LB", "QA", "SA", "TR"]
d = "graphs/results.csv"

df = pd.read_csv(d)

#BOXPLOT 
for country in countries:
    d1 = "graphs/BoxPlot/" + country + ".png"
    groupbycountry = 'country == "' + country + '"'
    df1=df.query(groupbycountry)
    sns.boxplot(y='values', x = 'cdn', data=df1)
    plt.ylabel ("RTT values in milliseconds", size =12)
    plt.xlabel("CDN", size=12)
    plt.title("BoxPlot for latency measures in " + country)
    plt.savefig(d1)

#CDF PLOT
for country in countries:
    for cdn in CDN:
        n_bins = 20
        groupbycountry = 'country == "' + country + '"'
        groupbycdn = 'cdn == "' + cdn + '"'
        df1=df.query(groupbycountry)
        df2 = df1.query(groupbycdn)
        counts, bin_edges = np.histogram(df2['values'], bins=n_bins, normed=True)
        cdf = np.cumsum(counts)
        plt.plot(bin_edges[1:], cdf/cdf[-1], label=cdn)
    plt.grid(True)
    plt.legend(loc='lower right')
    plt.xlabel('RTT(milliseconds)')
    plt.ylabel('Cumulative fraction')        
    plt.title("Cumulative Distribution function of the latency in " + country)
    d2 = "graphs/CDF/" + country + ".png"
    plt.savefig(d2)
    plt.show()

#CLUSTERMAP
data = weighedAvgRTT(directory)
ax = sb.clustermap(data, method="single", figsize=(6,6), cmap="YlGnBu")
ax.ax_row_dendrogram.set_visible(False)
plt.savefig('graphs/clustermap.png')
plt.show()

