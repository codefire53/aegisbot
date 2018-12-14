'''Importing necessary modules'''
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
#Creating word not found error
class WordNotFound(Exception):
    pass
def search(word):
    #Define kbbi website query url
    url='https://kbbi.kemdikbud.go.id/entri/'+quote(word)
    raw_parsed=requests.get(url).text
    #if there\'s no keyword definitions on kbbi, return errir message 
    try:
        if 'Entri tidak ditemukan. ' in raw_parsed:
            raise WordNotFound()
    except WordNotFound:
        return '{} tidak ditemukan!'.format(word)
    #Gathering all the definitions of the keyword
    else:
        definitions=[]
        parsed=raw_parsed[raw_parsed.find('<h2>'):raw_parsed.find('<h4>')]
        soup=BeautifulSoup(parsed,'html.parser')
        entries=soup.find_all('ul')+soup.find_all('ol')
        for entry in entries:
            for row in entry.find_all('li'):
                tipe=''
                #Getting the definition class
                tipe=row.find(color="red").get_text().strip()
                meaning=row.get_text().strip()[len(tipe):]
                #Excluding the examples
                if ':' in meaning:
                    meaning=meaning[:meaning.find(':')]
                #Append the definition to list if there's no class obtained
                if tipe=='':
                    definitions.append(meaning)
                #Otherwise, append the class and the definition to the list
                else:
                    definitions.append('({}){}'.format(tipe,meaning))
        #Outputting the definitions list aas string
        res='Daftar definisi kata/frasa "{}":\n'.format(word)
        for num,word in enumerate(definitions,1):
            res+='{}. {}\n'.format(num,word)
        return res
print(search('deru'))
        
                

        
    
