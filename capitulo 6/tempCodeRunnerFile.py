
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("Los siguientes lenguajes fueron mencionados: \t ")
for language in favorite_languages.values():
    print(f"\t {language.title()}")