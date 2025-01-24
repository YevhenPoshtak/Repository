from collections import Counter

def count_word_frequency(input_file, output_file):
    # Зчитування списку слів із файлу
    with open(input_file, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()

    # Підрахунок кількості кожного слова
    word_counts = Counter(words)

    # Запис результату у файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in word_counts.items():
            file.write(f'{word},{count}\n')

# Виконання програми
if __name__ == "__main__":
    count_word_frequency('words.txt', 'word_counts.txt')
