import csv,requests,json

res={}
resList=[]
words={}
if __name__=="__main__":
    count=0
    with open ("final.csv",mode="w")as csvfile:
        colNames = ['url', 'keyword', 'position', 'search_volume', 'cpc', 'traffic_index', 'traffic_potential', 'tix_delta', 'seo_value', 'seo_value_potential', 'seva_delta']
        writer = csv.DictWriter(csvfile,fieldnames=colNames)
        writer.writeheader()
        
        
    with open("data.csv") as csvfile:
        readCsv = csv.reader(csvfile,delimiter=',')
        for row in readCsv:

            queryURL = row[0]
        
            url = "http://api.searchmetrics.com/v3/ResearchContentGetListUrlKeywordRankings.json?url="+queryURL+"&countrycode=de&offset=0&limit=25&access_token=bec91b378bdcd185b024ec0d569e4fc9dd44b908"

            response=requests.get(url)

            if response.status_code == 200:

                res[queryURL]=response.json()
                jsonResponse=response.json()
                newList=jsonResponse["response"]
                for d in newList:
                    if d.keys().__contains__("similar"):
                
                        tmpd = d['similar']
                        del d['similar']
                
                        for i in range(0,len(tmpd)):
                            newList.append(tmpd[i])


                newList.sort(key=lambda item: item.get("position"),reverse=True)
                top5=newList[:5]
                with open('final.csv', 'a',encoding="utf-8") as csvFile:
                    writer = csv.writer(csvFile,lineterminator='\n')
                    for entry in top5:
                        writer.writerow([row[0]]+list(entry.values()))
                
                csvFile.close()
               
                                #writing to a csv

# =============================================================================
#                      with open ("final.csv",mode="w")as csvfile:
#                 colNames = ['url']
#                 for entry in top5[0]:
#                     colNames.append(entry)
#              #Write dictionary to CSV
#             
#                 print(colNames)
#                 writer = csv.DictWriter(csvfile,fieldnames=colNames)
#                 
#                 writer.writeheader()
# =============================================================================
            
# =============================================================================
#     for k,v in res.items():
#         writer.writerow({'url':k, 'response':v})
# =============================================================================





#http://api.searchmetrics.com/v3/ResearchContentGetListUrlKeywordRankings.json?url=https://www.ebay.com/b/Hockey-Tickets/173633/bn_18750301&countrycode=de&offset=0&limit=25&access_token=8e80b88ad095f4e7131bcb37ce305b5264e34f5d
