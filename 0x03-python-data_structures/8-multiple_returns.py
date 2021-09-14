#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng > 0:
        return(leng, sentence[0])
    else:
        return (leng, 'None')
