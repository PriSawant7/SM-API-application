# SM-API-application

The application fetches the data for each url from the data.csv and then fetches the top 5 keywords for the url. The keywords are ranked based on the traffic index. It also takes into account the simalar keywords when choosing the top five.

Then the top five keyword information is written to the final.csv. all the headers are put as column names in the csv file.

The csv is then pulled in tableau to create dashboards for better understanding of the data. 
The Dashbord contains two charts one is the table that shows the urls and the corresponding top5 keywords and the other is the chart for the top 5 keywords for each url.
When you click on the url the bar chart changes as per the data of the url.
