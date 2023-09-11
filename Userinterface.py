from Creation import Creation
from Saving import Saving
from Reading import read_all_notes
from Editing import editing_note
from Delete import del_note
from Download import download_notes
from Sorting import sort_note

def user_interface():
    info = "Данная программа позволяет создавать, редактировать и просматривать заметки.\n" \
           "Команды используемые для работы с программой: \n" \
           "help - справка по работе программы;\n" \
           "create  - создание заметки;\n" \
           "read - просмотр заметок;\n" \
           "edit - изменение заметок;\n" \
           "end - выход из программы;\n" \
           "delete - удалить заметку;\n" \
           "download - выгрузить в файл JSON\n" \
           "sort_ascend - сортировка по дате создания заметки по возрастанию\n" \
           "sort_descend - сортировка по дате создания заметки по убыванию\n"
    while True:
        print("Введите команду: ")
        user_input = input().lower()
        if user_input == "create":
            title = input("Введите название заметки: ")
            text = input("Введите содержание заметки: ")
            note = Creation(title, text)
            save = Saving(note.note())
            save.saving_note()
        elif user_input == "edit":
            editing_note("note.json")
        elif user_input == "read":
            read_all_notes("note.json")
        elif user_input == "help":
            print(info)
        elif user_input == "delete":
            save = Saving(del_note("note.json"))
            save.saving_note()
        elif user_input == "end":
            break
        elif user_input == "download":
            download_notes("note.json")
        elif user_input == "sort_ascend":
            sort_note("note.json", order=True)
            print("Заметки отсортированы по возрастанию")
        elif user_input == "sort_descend":
            sort_note("note.json", order=False)
            print("Заметки отсортированы по убыванию")
        else:
            print("Команда не найдена. help - справка о работе программы")