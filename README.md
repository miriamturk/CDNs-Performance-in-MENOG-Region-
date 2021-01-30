Team Members:
=============
Michel Khalaf  
Miriam Turk  
Yara Yammine  

# CDNs Performance in MENOG Region


Several studies present analyzes of the performance of CDNs on an international scale. CDNs (Content Delivery Network) are content delivery networks that not only provide a faster experience but also help prevent sites from crashing during heavy congestion or even increased traffic. In our project, we seek to do this performance study on a more limited scope, in the Middle East region, in the group of Middle East Network Operators Group (MENOG).


CDNs Concept |  Middle East Region
:-------------------------:|:-------------------------:
![](https://www.themexpert.com/images/easyblog_articles/273/b2ap3_large_cdn_cover.png)  |  ![](https://lh3.googleusercontent.com/proxy/LaPohduRZtqSvCdHR-YbcbiUSRbS-8FmlioVn8sKg4XzpjEXgypD9zQAoC8blmqD8wNXuagkysbLoFKUYuJGxDeZy_v5ZKFtr7Ffv_dI6YfmFYbF2IFFLfqS1K0jK_-OmDHlP8KSAHA)

Nowadays, many companies seek to guarantee a consistent experience for all their users, regardless of their geographic location. This is why many use a CDN to serve static assets as close as possible to their end users.

To know more about our results, how we did our code and visualizations:

 - An easy README is given in the *"menog-rtt-cdn-measure"* folder for you to follow

 - Results are visualized in the *"menog-rtt-cdn-analytics"* folder as:

    - A clustermap

    - BoxPlot Figures

    - CDF Figures

## Plot Codes

- rttCompute : All RTT results of each country and each CDN are computed and saved in a csv file
- weighedmeanRTT : Code to compute weighed mean RTT for each CDN in each country
- rttPlot : Code to visualize and save all graphs and figures for the analysis

__N.B.__: If you want to execute the RTT Computation and Figures don't forget to add the right directory where this project is cloned.

