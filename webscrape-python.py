# url to scrape data from 
url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'
  #run this too to update the page text value of this path is null. That is, the issue has in path. Do you want to fix the path?
#Sure.. I gotta drop soon unfortunately.. how long could it take to fix? for fix the path? yes. I have to know the scrap data that you'd lijke towantt    
# path to particular element . after this path, length of path is null...

#Got it... sorry man... gotta leave... but it's the data in pop up box of this tooltip

#Have a good one.
path = '/html/body/div[7]/main/div[3]/div/div[3]/div[2]'
# path = '/html/body/div[7]/main/div[3]/div/div[3]/div[2]/div/div[1]/div/div[2]/ul'

  
# get response object 
response = requests.get(url) 
  
# get byte string 
byte_data = response.content 
  
# get access to the raw bytes of the response payload
source_code = html.fromstring(byte_data) 
  
# jump to preferred html element 
tree = source_code.xpath(path)

# url to scrape data from 
url2 = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'

# path to particular element 
path2 = '/html/body/div[7]/main/div[3]/div/div[3]/div[1]/div/p[1]/span'

# jump to preferred html element 
tree2 = source_code.xpath(path2)
print(len(tree))

  
# print texts in first element in list
d = datetime. datetime. today()
d = d.strftime('%m-%d-%Y')
print('As of '+str(d)+', the coronavirus impact on the US is:')