'''This function contains documentation of each bot command'''
def docum(cmd):
    if cmd=='translate':
        return 'This keyword will return translation of the sentence/phrase/word.\n\nCommand: #translate <translate to language (id)> <sentence/phrase/word>\n\nFor example: #translate en canggih'
    elif cmd=='wiki':
        return 'This keyword will return the summary of the word/phrase in wikipedia.\n\nCommand: #wiki <wiki language> <word/phrase>\n\nFor example: #wiki en panama paper'
    elif cmd=='kerang':
        return 'This keyword is based on kerang bot.\n\nCommand: #kerang <question sentence>\n\nFor example: #kerang Apakah rey wibu?'
    elif cmd=='wolfram':
        return 'This keyword will return the search query answer on wolfram alpha.\n\nCommand: #wolfram <user input>.\n\nFor example: #wolfram integral as x approaches 0 of x^2'
    elif cmd=='arti':
        return 'This keyword will return indonesian word/phrase definitions based on kbbi website.\n\nCommand: #arti <indonesian word or phrase>.\n\nFor example: #arti deru'
    elif cmd=='define':
        return 'This keyword will return english word/phrase definitions based on oxford dictionary website.\n\nCommand: #define <english word or phrase>.\n\nFor example: #define tremendous'
    elif cmd=='command':
        return 'This keyword will return the keywords of the bot\n\nCommand: #command'
    elif cmd=='profile':
        return 'This keyword will return profile of the bot\n\nCommand: #profile'
