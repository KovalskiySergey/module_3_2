def send_email(m, r, *, s = 'university.help@mail.ru'):
    vailed = (".com", ".ru", ".net" )
    if r == s:
        print("Нельзя отправить письмо самому себе!")
    elif (('@' not in s or not any(s.endswith(d) for d in vailed))
          or ('@' not in r or not any(r.endswith(d) for d in vailed))):
        print(f'"Невозможно отправить письмо с адреса {s} на адрес {r}"')
    elif s != 'university.help@mail.ru':
        print(f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {s} на адрес {r}"')
    elif s == 'university.help@mail.ru':
        print(f'"Письмо успешно отправлено с адреса {s} на адрес {r}"')
    else:
        print(f'"Письмо успешно отправлено с адреса {s} на адрес {r}"')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', s='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', s='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', s='urban.teacher@mail.ru')