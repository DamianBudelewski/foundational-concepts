def pig_latin(sentence):
    """Performs pig latin translation on given sentence.

    Transfer initial consonant or consonant cluster of each word to the end
    of the word and adding a vocalic syllable (usually /eɪ/)

    example: "pig latin" would be "igpay atinlay"
    """

    try:
        transformed_sentence = str()
        for word in sentence.split(" "):
            transformed_word = word[1 : len(word)] + word[0] + "ay"
            transformed_sentence += f"{transformed_word} "
        return transformed_sentence[0:-1]
    except IndexError:
        print("Can't process empty strings ... try again with a valid sentence!")
