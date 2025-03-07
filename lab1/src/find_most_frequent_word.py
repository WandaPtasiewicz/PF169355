w = ["apple", "banana", "apple", "orange", "banana", "apple"]

def find_most_frequent_word(string):
    f = {}
    for word in w:
     f[word] = f.get(word, 0) + 1

    m = max(f, key=f.get)
    print(m)
find_most_frequent_word(w)