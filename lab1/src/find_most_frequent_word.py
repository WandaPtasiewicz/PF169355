from collections import Counter

w = "Ala ma kota Felka i kota Felka"

def find_most_frequent_word(text):
    if not text.strip():
        return None

    words = text.lower().split()
    word_counts = Counter(words)
    max_count = max(word_counts.values(), default=0)

    most_frequent_words = [word for word, count in word_counts.items() if count == max_count]

    return most_frequent_words if most_frequent_words else None


print(find_most_frequent_word(w))

