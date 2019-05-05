from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uclient = uReq(my_url) # create connection and open the web_ul given(in this case: flipkart.com)

page_html = uclient.read() # the read() fun. gather all the data from the site and dump it to given variable(page_html)

uclient.close() # close connection

page_soup = soup(page_html,'html.parser') # Parsing the html page recieved

#container = page_soup.find_all("div",{"class" : "bhgxx2 col-12-12"}) # finding all the div with class specified
container = page_soup.find_all("div",{"class" : "_1-2Iqu row"}) # finding all the div with class specified
#print(len(container)) # listing the total nos. of product from the current page of url, in this case nos. of iphones from flipkart

# now we make the use of prettify function to
#print(soup.prettify(container[1]))

# Attributes are always written in square brackets[]
#test = container[0]
#print(container.text) # for the name of the product from the conatiner array
# for i in range(10):
#     test = container[i]
#     print(test.text)
#     print("===============================\n")

# finding the required values individually
# name = test.find('div',{'class': '_3wU53n'})
# print(name.text)
#
# rating = test.find('div',{"class" : "hGSR34"})
# print(rating.text)
#
# price = test.find('div',{"class" : '_1vC4OE _2rQ-NK'})
# print(price.text)

#====================================================
# Finding the required values for all the products available
# at the first page...

def generate():
    for i in range(len(container)):
        test = container[i]
        name = test.find('div', {'class': '_3wU53n'})
        rating = test.find('div', {"class": "hGSR34"})
        price = test.find('div', {"class": '_1vC4OE _2rQ-NK'})
        print(i+1," => ",name.text," || ",rating.text," || ",price.text,"\n")

#generate()
# Now save these details to a csv files

file = open("Apple_products.csv",'w+')
# Creating header for the csv file
# A CSV file has header variable seperated with ,
header ="ProductName,Rating,Price\n"
file.write(header)
# now define a function in which we write

def generateToCsv():
    for i in container:
       # test = container[i]
        name = i.find('div', {'class': '_3wU53n'})
        rating = i.find('div', {"class": "hGSR34"})
        price = i.find('div', {"class": '_1vC4OE _2rQ-NK'})
        # print(type(name.text))
        # print(type(rating.text))
        # print(type(price.text))
        print((name.text + "," + rating.text + "," + price.text + "\n"))
        #file.write((name.text.replace(",","|") + "," + rating.text + "," + price.text.replace(",","") + "\n"))

generateToCsv()
#file.write("apple"+","+"4.6"+","+"46000")
file.close()
