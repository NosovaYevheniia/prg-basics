import module


if __name__ == "__main__":
    sentence = "You never get a second chance to make a first impression"
    letter = "e"
    print(sentence)
    count = module.f(sentence, letter)
    print(f"The number of letter {letter} : {count}")