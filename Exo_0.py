input = "Hello World"


def len_of_last_world(sentences: str):
    words_list = sentences.split()
    return len(words_list[-1])


print(len_of_last_world(input))
