import speech_recognition


def greeting():
    """greeting functon"""


    return 'привет хозяин!'


def crate_task():
    """crate a todo task"""

    print('Что добавим в список дел?')

    with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    with open('todo.list.txt', 'a') as file:
        file.write(f' ! {query}\n')
        
        return f'задача {query} добавлена в todo-list'

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

if query == 'привет друг':
        print(greeting())
elif query == 'добавить задачу':
    print(crate_task())
else:
    print('хозяйн я вас не понял повторите пажалуйста! >:|')