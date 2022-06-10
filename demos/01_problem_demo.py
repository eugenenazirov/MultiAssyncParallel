def read_numbers(path):
    lst = []
    with open(path, 'r') as file:
        while line := file.readline():
            lst.append(int(line))
    return lst


def count_triplets_sum(ints):
    print("started counting triplets sum")

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f"Triple found: {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

    print(f"ended count triplet sum. Triplet counter = {counter}")


if __name__ == '__main__':
    print("started main")

    ints = read_numbers(r'..\data\1Kints.txt')
    count_triplets_sum(ints)

    print("What are we waiting for?")
    print("ended main")
