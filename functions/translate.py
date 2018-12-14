'''This function returns the translation of the word to another language using google translate API. The language is specified based on user input.'''
import goslate
def translate(txt):
    #Splitting the input into two 
    txt = txt.split(maxsplit=1)
    gs=goslate.Goslate()
    #This function will do the translation,if the input length is 2
    if(len(txt)==2):
        return gs.translate(txt[1],txt[0])
    #Otherwise, return the warning
    else:
        return 'Invalid input!'

