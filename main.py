import streamlit as sl


sl.title('Привет я приложение')
sl.subheader('Я подзаголовок')
sl.header('Заголовок')
sl.text('Обычный текст')
sl.markdown('**Привет** *мир*') 
sl.markdown('[Google](https://google.com)')
sl.caption('Подпись')
sl.latex(r"\begin{pmatrix}a&b\\c&b\end{pmatrix}")
json = {'a': '1, 2, 3', 'b': '4, 5 , 6'}
sl.json(json)
code = '''
print('Привет')
def funck():
    return 0;
'''
sl.code(code, language='python')