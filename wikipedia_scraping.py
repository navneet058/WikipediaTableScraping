import pandas as pd
import wikipedia as wiki

 

 #Get the html page source based on keywords

html = wiki.page("List of IIT in india").html().encode("UTF-8")

#Get second table data
df = pd.read_html(html)[1]

#Write the table data to csv

df.to_csv('wiki_table.csv',header=0,index=False)

#print data frame

print(df)