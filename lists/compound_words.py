english_words = ['water', 'big', 'apple', 'watch',
                'banana', 'york', 'amsterdam', 'orange',
                'macintosh', 'bottle', 'book']
mixed_words = ['paris', 'applewatch', 'ipod',
               'amsterdam', 'bigbook', 'orange',
               'waterbottle']


def get_compound_words():
    """
    Get compound words from given list of mixed words
    :return: list of compound words
    """
    compound_words = [mixed_words[i] for i in range(len(mixed_words)) if mixed_words[i] not in english_words]
    print(compound_words)


if __name__ == "__main__":
    get_compound_words()
