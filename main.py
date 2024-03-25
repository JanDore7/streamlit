import streamlit as sl
import pandas as pd
import time as ts
from datetime import time

# sl.markdown("""
# <style>
# .st-emotion-cache-1avcm0n.ezrtsby2
# {
#     display: none !important;
# }
# </style>
# """, unsafe_allow_html=True)



sl.markdown('<h1>Регистрация</h1>', unsafe_allow_html=True)
# sl.subheader('Я подзаголовок')
# sl.header('Заголовок')
# sl.text('Обычный текст')
# sl.markdown('**Привет** *мир*') 
# sl.markdown('[Google](https://google.com)')
# sl.caption('Подпись')
# sl.latex(r"\begin{pmatrix}a&b\\c&b\end{pmatrix}")
# json = {'a': '1, 2, 3', 'b': '4, 5 , 6'}
# sl.json(json)
# code = '''
# print('Привет')
# def funck():
#     return 0;
# '''
# sl.code(code, language='python')
# sl.write('## H2')
# sl.write(json)

# sl.metric(label='Скорость ветра', value='120ms⁻¹', delta='1.4ms⁻¹')
# sl.metric(label='Скорость ветра', value='120ms⁻¹', delta='-1.4ms⁻¹')

# table = pd.DataFrame({'column 1': [1,2,3,4,5,6,7], 'column 2': [11,12,13,14,15,16,17]})
# sl.table(table)

# sl.dataframe(table)

# sl.image('2024-01-10_13-29.png',caption='Снимок' , width=150, clamp=False, channels='RGB')

# sl.audio('sample-6s.mp3')

# sl.video('MOT - Kogda muzhchina vlyublen - 1080HD - [ VKlipe.org ].mp4')

# state = sl.checkbox(label='Чекбокс', value=True)
# if state:
#     sl.write('Привет')

# def foo():
#     print(f'Состояние {sl.session_state.чекер}')

# state = sl.checkbox(label='Бокс', on_change=foo, key='чекер')

# radio_btn = sl.radio('В какой стране ты живешь?', options=('US', 'RU', 'UA'))
# print(radio_btn)

# def btn():
#     print('КЛИК-КЛАК')

# btn = sl.button('Нажми меня', help='кликни', on_click=btn)



# select = sl.selectbox('Выбери автомобиль', help='Кликни на нужный', options=('Audi', 'BMW', 'Changan', 'VAZ'))
# print(select)


# m_select = sl.multiselect('Твой любимый бренд?', options=('Microsoft', 'Apple', 'Accer'))
# sl.write(m_select)
# print(m_select)


sl.markdown('---')
# images = sl.file_uploader('Загрузи изображение', type=['jpeg','png'], accept_multiple_files=True)
# if images is not None:
#     for image in images:
#         sl.image(image)


# sl.markdown('---')
# video = sl.file_uploader('Загрузи изображение', type='mp4')
# if video is not None:
#     sl.video(video)


# val = sl.slider('Это слайдер', min_value=50, max_value=250, value=110 )
# print(val)


# vak1 = sl.select_slider('Новый ползунок', options=('1', '3', '5'))

# val = sl.text_input('Введите название курса', value=' Мой курс: ', max_chars=15)
# sl.write(val)


# val = sl.text_area('Опиши ситуацию.', height=100 )
# print(val)


# val = sl.date_input('Веди дату')
# print(val)




# def converter(value):
#     m,s,mm = value.split(':')
#     t_s = int(m)*60+int(s)+int(mm)/1000
#     return t_s

# val = sl.time_input('Выбери время', value=time(0,0,0))
# if str(val) == '00:00:00':
#     sl.write('Установи таймер')
# else:
#     sec = converter(str(val))
#     bar = sl.progress(0)
#     per = sec/100
#     progress_status = sl.empty()
#     for i in range(100):
#         bar.progress(i+1)
#         progress_status.write(str(i) + '%')
#         ts.sleep(per)
#     progress_status.write('Выполнено')
        

# form = sl.form('Форма №1')
# form.text_input('Имя')
# form.form_submit_button('Отправить')

with sl.form('Форма №2'):
    col1, col2 = sl.columns(2)
    col1.text_input('Логин')
    col2.text_input('Пароль')
    sl.text_input('Электронная почта')
    sl.text_input('Подтверди пароль')
    sl.form_submit_button('Отправить')