import pafy

print('Хотите скачать видео с Ютуба? Просто введите URL ниже....')
url = input('Введите URL:')

try:
    v = pafy.new(url)
    print('Выберите желаемое качество видео набрав нужную цифру...')
    available_streams = {}
    count = 1
    video = v.streams
    for item in video:
        available_streams[count] = item
        print(f'{count}:{item}')
        count += 1
    item_count = int(input('Введите номер нужного качества:'))
    d = video[item_count - 1].download()
    print('Скачивание прошло успешно добро пожаловать в пираты!')
except:
    print('Возможно ссылка не верна...')
