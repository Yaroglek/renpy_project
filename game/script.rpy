init:
    image snoop = "snop.png"
    image bg radik = "radik.png"

# Определение персонажей игры.
define eileen = Character('Эйлин', color = "#c8ffc8")
define snoop = Character('Снуп Дог', color = "#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy
    eileen "Вы создали новую игру Ren'Py."

    eileen "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    show eileen at left

    eileen "Хехе"

    hide eileen

    eileen "где я"
    scene bg radik

    show snoop

    snoop "Поступайте в радик учиться, пацаны)"

    return
