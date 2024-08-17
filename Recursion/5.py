def prepare(text,index = 0,result = None):
    if result is None:
        result = []
    
    first = text.find("'", index)
    second = text.find("'",first + 1)

    if first == -1 or second == -1:
        return result
    str = text[first + 1:second]
    result.append(str)

    return prepare(text,second + 1,result)

def segment(text,wordlist):
    if not text:
        return True

    if not wordlist:
        return False
    
    word = wordlist[0]
    if word and word in text:
        remain_text = text.replace(word, '',1)
        if segment(remain_text,wordlist) or segment(text,wordlist[1:]):
            return True
    
    return segment(text,wordlist[1:])

inp = prepare(input("Enter list[str]: "))
texts,l = inp[0],inp[1:]
print(f"text: str = '{texts}'")
print(f'lang: list[str] = {l}')
print(f'segment(text, lang) -> {segment(texts,l)}')