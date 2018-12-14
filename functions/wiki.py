'''This function will return the wikipedia summary version of the keyword which is obtained from user input(default lang=en)'''
import wikipedia
def summarize(lang,keyword):
    #Setting up the wikipedia language
    wikipedia.set_lang(lang)
    #Return summary of the information about the keyword in wikipedia
    try:
        result=wikipedia.summary(keyword)
    #Return several search results option if there's ambiguity
    except wikipedia.exceptions.DisambiguationError:
        related_words=wikipedia.search(keyword)
        result='{} is ambiguous. Here are several suggestions:\n'.format(keyword)
        for word in related_words:
            result+='{}\n'.format(word)
        return result
    #Otherwise, print error
    except wikipedia.exceptions.PageError:
        return '{} keyword not found!'.format(keyword)
    #Limitizing the summary to 2000 characters(character limitation size of line messenger)
    else:
        if len(result) > 2000:
            result=result[:2000]
            if not result.endswith('.'):
                result=result[:result.rfind('.')+1]
        return result
