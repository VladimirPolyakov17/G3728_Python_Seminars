import model
import view
import text_fields as txt


def start(): 
    while True: # Цикл для пользователя
        choice = view.main_menu()
        match choice:
            case 1: # Открытие файла
                model.open_file() 
                view.print_message(txt.successful_open)
            case 2: # Сохранение файла
                model.save_file() 
                view.print_message(txt.successful_save)
            case 3: # Показ всех контактов
                pb = model.get_phone_book()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
            case 4: # Добавление нового контакта
                new_contact = view.new_contact()
                model.add_contact(new_contact)
                view.print_message(txt.contact_saved(new_contact.get('name')))
            case 5: # Поиск контакта
                word = view.enter_keyword()
                result = model.find_contact(word)
                view.show_contacts(result, txt.not_found(word))
            case 6: # Изменение контакта
                pb = model.get_phone_book()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    model.edit_contact(edited_contact)
                    view.print_message(txt.successful_edited(edited_contact[1].get('name')))
            case 7: # Удаление контакта
                pb = model.get_phone_book()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirm(txt.confirm_delete(pb[index - 1].get('name'))):
                        view.print_message(txt.delete_contact(model.remove_contact(index)))
            case 8: # Выход
                if model.original_book != model.phone_book:
                    if view.confirm(txt.no_saved_book):
                        model.save_file()
                view.print_message(txt.goodbye)
                exit()