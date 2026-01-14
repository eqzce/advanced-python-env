import string

def analyze_text(input_file, output_file):
    with open(input_file, encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = 0
    word_freq = {}

    for line in lines:
        line = line.translate(str.maketrans("", "", string.punctuation)).lower()
        words = line.split()
        word_count += len(words)

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Total lines: {line_count}\n")
        file.write(f"Total words: {word_count}\n")
        file.write("Word frequencies:\n")

        for word, count in word_freq.items():
            file.write(f"{word}: {count}\n")



if __name__ == "__main__":
    analyze_text("task1/text.txt", "task1/analysis.txt")
