def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{len(words)} words found in the document')
        counts = char_count(file_contents)
        counts.sort(reverse=True, key=sort_on)
        for c in counts:
            print(f'The \'{c['name']}\' character was found {c['num']} times')


def char_count(text):
    low = text.lower()
    results = {}
    for chara in low:
        if(chara in results):
            results[chara]+=1
        else:
            results[chara]=1

    resname = []
    for res in results:
        if res.isalpha():
            resname.append({'name': res, 'num': results[res]})
    return resname

def sort_on(dict):
    return dict["num"]


main()
