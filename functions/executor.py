'''Importing all the bot modules'''
from translate import translate
from calc import calculate
from wiki import summarize
from wolf import wolfram
from answer import kerang
from helper import docum
from profile import info
from command import lst
from kbbi import search
from oxford import define
'''This function will returning the another function result'''
def result(us_input):
    #Return the translate function result on text format
    if(us_input[0:us_input.index(' ')]=='#translate'):
        return ['text',translate(us_input[len('#translate')+1:])]
    #Return the wiki function result on text format
    elif(us_input[0:us_input.index(' ')]=='#wiki'):
        word=us_input[len('#wiki')+1:]
        try:
            word=word.split(maxsplit=1)
            language=word[0]
            keyword=word[1]
            return ['text',summarize(language,keyword)]
        except IndexError:
             return ['text',summarize('en',word)]
    #Return the wolfram function result on image format
    elif(us_input[0:us_input.index(' ')]=='#wolfram'):
        return ['image',wolfram(us_input[len('#wolfram')+1:])]
    #Return the calc function result on text format
    elif(us_input[0:us_input.index(' ')]=='#calc'):
        return ['text',calculate(us_input[len('#calc')+1:])]
    #Retun the kerang function result on text format
    elif(us_input[0:us_input.index(' ')]=='#kerang'):
        return ['text',kerang(us_input[len('#kerang')+1:])]
    #Return the help function result on text format
    elif(us_input[0:us_input.index(' ')]=='#help'):
        return ['text',docum(us_input[len('#help')+1:])]
    #Return the profile function result on text format
    elif(us_input=='#profile'):
        return ['text',info()]
    #Return the command function result on text format
    elif(us_input=='#command'):
        return ['text',lst()]
    #Return the arti function result on text format
    elif(us_input[0:us_input.index(' ')]=='#arti'):
        return ['text',search(us_input[len('#arti')+1:])]
    #Return the define function result on text format
    elif(us_input[0:us_input.index(' ')]=='#define'):
        return ['text',define(us_input[len('#define')+1:])]
    #Otherwise, return warning
    else:
        return 'No {} command found!'.format(us_input)


