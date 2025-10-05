def main():
    text = input("Text: ").lower()
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_words = sorted(word_counts.keys())
    max_length = max(len(word) for word in sorted_words)
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")

main()