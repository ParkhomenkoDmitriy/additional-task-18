def letters(text):
    clean_text = text.replace(" ", "").lower()

    # Множество для отслеживания всех букв
    all_letters = set(clean_text)

    # Множество для отслеживания повторяющихся букв
    repeated_letters = set()

    # Проходим по буквам в тексте
    for i in range(len(clean_text) - 1):
        for j in range(i + 1, len(clean_text)):
            if clean_text[i] == clean_text[j]:
                repeated_letters.add(clean_text[i])
                break  # Если нашли повтор, переход на следующую букву

    unique_letters = all_letters - repeated_letters

    return repeated_letters, unique_letters


input_text = input("Введите строку: ")
repeated_letters, unique_letters = letters(input_text)

if repeated_letters:
    print(f"Повторяющиеся буквы: {', '.join(sorted(repeated_letters))}")
if unique_letters:
    print(f"Уникальные буквы: {', '.join(sorted(unique_letters))}")
else:
    print("Нет уникальных букв.")
