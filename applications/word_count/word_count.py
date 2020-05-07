def word_count(s):

    word_dic = {}
    word_list = s.lower().split()
    word_count = []
    new_word_list = []

    for word in word_list:
        new_word_list.append(word.replace(':','')
        .replace(';','').replace(',','').replace('.','')
        .replace('-','').replace('+','').replace('=','')
        .replace('/','').replace('|','').replace('\\','')
        .replace('[','').replace(']','').replace('{','')
        .replace('}','').replace('(','').replace(')','')
        .replace('*','').replace('^','').replace('&','')
        .replace('"',''))

    if new_word_list == ['']:
        return word_dic

    for w in new_word_list:
        word_dic[w] = new_word_list.count(w)

    return word_dic

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))