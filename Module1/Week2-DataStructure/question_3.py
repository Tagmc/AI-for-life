import gdown
url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
output = 'P1_data.txt'
gdown.download(url, output, quiet=False)


def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    return counter


if __name__ == "__main__":
    file_path = 'P1_data.txt'
    result = count_word(file_path)
    print(result['man'])
