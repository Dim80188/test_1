import wikipediaapi

wiki_w = wikipediaapi.Wikipedia('ru')


def print_categorymembers(categorymembers, level=0, max_level=1):
    all_c = []
    for c in categorymembers.values():
        all_c.append(c.title)
    return all_c



cat = wiki_w.page("Категория:Животные по алфавиту")

list_a = print_categorymembers(cat.categorymembers)

dict_a = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ы': 0, 'э': 0, 'ю': 0, 'я': 0,
          'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for word in list_a:
    for key, value in dict_a.items():
        if word[0].lower() == key:
            dict_a[key] += 1

for k, v in dict_a.items():
    print(k.upper(), ':', v)