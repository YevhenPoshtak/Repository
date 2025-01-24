def sort_and_display_results(input_file, output_file):
    # Зчитування частот слів із файлу
    with open(input_file, 'r', encoding='utf-8') as file:
        word_counts = [line.strip().split(',') for line in file]
        word_counts = [(word, int(count)) for word, count in word_counts]

    # Сортування за частотою у спадному порядку
    sorted_counts = sorted(word_counts, key=lambda x: x[1], reverse=True)

    # Запис відсортованого результату у файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in sorted_counts:
            file.write(f'{word}: {count}\n')

# Виконання програми
if __name__ == "__main__":
    sort_and_display_results('word_counts.txt', 'sorted_results.txt')
