import streamlit as sl
import pandas as pd



sl.markdown("""
<style>
.st-emotion-cache-1avcm0n.ezrtsby2
{
    display: none !important;
}
</style>
""", unsafe_allow_html=True)



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
sl.write('## H2')
sl.write(json)

sl.metric(label='Скорость ветра', value='120ms⁻¹', delta='1.4ms⁻¹')
sl.metric(label='Скорость ветра', value='120ms⁻¹', delta='-1.4ms⁻¹')

table = pd.DataFrame({'column 1': [1,2,3,4,5,6,7], 'column 2': [11,12,13,14,15,16,17]})
sl.table(table)

sl.dataframe(table)

sl.image('2024-01-10_13-29.png',caption='Снимок' , width=150, clamp=False, channels='RGB')

sl.audio('sample-6s.mp3')

sl.video('MOT - Kogda muzhchina vlyublen - 1080HD - [ VKlipe.org ].mp4')


