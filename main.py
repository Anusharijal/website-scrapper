import requests
from bs4 import BeautifulSoup
url= "https://codewithharry.com" 
r= requests.get(url)
htmlContent = r.content
#print(htmlContent)
soup= BeautifulSoup(htmlContent, 'html.parser')
#print(soup)
#print(soup.prettify)
title = soup.title
#print(type(title.string))
#get al the paragraphs from the page
paras = soup.find_all('p')
#print(paras)
# get all the anchors from the page
anchors = soup.find_all('a')
# print(anchors)
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
            linkTest = "https://codewithharry.com" +link.get('href')

        #print(link.get('href'))

 #Get first element in the Html page
#print(soup.find('p'))

 #Get classes of any element in the HTML  page
#print(soup.find('p')['class'])

 #find all the elements with class lead
#print(soup.find_all("p",class_="lead"))

 #Get the text from the tags/soup
#  print(soup.find_all('p').get_text())
#  print(soup.get_text())




navbarSupportedContent  = soup.find(id='navbarSupportedContent')
# for elem in navbarSupportedContent.contents:
#     print(elem)

for item in navbarSupportedContent.stripped_strings:
   print(item)
