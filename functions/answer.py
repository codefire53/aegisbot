'''This function is based on kerang ajaib bot'''
import random
def kerang(question):
    ans=['Ya','Tidak']
    if question.lower().startswith('apakah'):
        return random.choice(ans)
        
        
