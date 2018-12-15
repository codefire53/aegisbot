'''Importing necessary modules'''
from urllib.parse import quote
import urllib
import requests
from bs4 import BeautifulSoup
'''Function to search word/phrase on oxford dictionary'''
def define(word):
    #Oxford dictionary search query url
    url='https://en.oxforddictionaries.com/definition/'+quote(word)
    #Parse the html file
    test=urllib.request.urlopen(url)
    soup=BeautifulSoup(test,'html.parser')
    #Initialize definition list
    lst=[]
    #Find all the elements of the definitions of the keyword section, and looping through them
    meanings=soup.find_all('section',{'class':'gramb'})
    for row in meanings:
        #Obtain the definition type
        types=row.find('h3',{'class':'ps pos'})
        ulist=row.find('ul',{'class':'semb'})
        #find the li tag which contains list of the definitions
        word_defs=ulist.find_all('li')
        for defs in word_defs:
            #If tag <div class="trg"> exist, then fetch the main definition which is located in <p> tag
            mean_word=defs.find('div',{'class':'trg'})
            if mean_word!=None:
                #Generate all <div class="trg"> children
                m_word=mean_word.findChildren()
                for mw in m_word:
                    #If the current section class is ind and the parent tag is p, then that's the main definiton 
                    if mw.get('class')==['ind'] and mw.parent.name=='p':
                        #Putting on the type and the main definition to the list
                        lst.append('({}){}'.format(types.get_text().strip(),mw.get_text().strip()))
                       
    #If the list contains all of the defintions, then print out all of them
    if lst:
        res='List of definitions of "{}" word/phrase:\n'.format(word)
        for num,define in enumerate(lst,1):
            res+='{}. {}\n'.format(num,define)
        return res
    #Otherwise, print error message
    else:
        return 'There\'s no "{}" word/phrase in the oxford dictionary database!'.format(word)

