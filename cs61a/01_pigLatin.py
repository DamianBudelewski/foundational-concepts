def pig_latin(sentence):
    """Performs pig latin translation on given sentence.

    Transfer initial consonant or consonant cluster of each word to the end
    of the word and adding a vocalic syllable (usually /eɪ/)

    Test using docstring:
    >>> pig_latin("pig latin")
    'igpay atinlay'

    How to test:
    a) Using Python interpreter
        .>>> from doctest import run_docstring_examples
        .>>> run_docstring_examples(pig_latin, globals(), True)
        Finding tests in NoName
        Trying:
            pig_latin("pig latin")
        Expecting:
            'igpay atinlay'
        ok
    b) Using CLI
        python3 -m doctest 01_pigLatin.py
    """
    try:
        transformed_sentence = str()
        for word in sentence.split(" "):
            transformed_word = word[1 : len(word)] + word[0] + "ay"
            transformed_sentence += f"{transformed_word} "
        return transformed_sentence[0:-1]
    except IndexError:
        print("Can't process empty strings ... try again with a valid sentence!")


def pig_latin_test():
    """Test pig latin translation on given sentence using assertion."""
    assert (
        pig_latin("pig latin") == "igpay atinlay"
    ), "Wrong translation for 'pig latin' sentence"
