def character_count(word):
    character_count = {}
    for char in word:
        if (char in character_count):
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


if __name__ == "__main__":
    print(character_count('smiles'))
