def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago...'
result = index_words_iter(address)
print(result)
print(list(result))         # 리스트를 통해서 generator 수행
