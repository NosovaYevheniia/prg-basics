def number_of_words(text:str):
    text_list = text.split()
    return len(text_list)

def ordered(text:str):
    text_list = text.split()
    sorted_list = sorted(text_list, key=len, reverse=True)
    return sorted_list
        

def alphabetic(text:str):
    text_list = text.split()
    text_list.sort()
    return text_list

x = ordered("An apple a day keeps the doctor away")
print(x)