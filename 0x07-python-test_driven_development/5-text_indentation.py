#!/usr/bin/python3
'''
Module 5-text_indentation
Has a function that   function that prints a text with 2 new lines,
after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''function that prints a text with
    2 new lines after each of these characters: .?:
    '''
    if isinstance(text, str):
        for sub in '.?:':
            # replace: reemplaza caracteres de un texto
            text = text.replace(sub, sub + '\n\n')
            # strip: para eliminar espacios
        l_sent = [sentence.strip(' ') for sentence in text.split('\n')]
        con_list = '\n'.join(l_sent)
        print(con_list, end='')
    else:
        raise TypeError('text must be a string')
