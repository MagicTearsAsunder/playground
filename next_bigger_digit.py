def next_bigger(n):
    if n < 10:
        return -1

    digit = [int(i) for i in str(n)]
    digit.reverse()
    temp = None

    final_digit = []
    for i in range(1, len(digit)):
        if digit[i] < digit[i-1]:
            rest_slice = digit[i:]
            temp = digit[i]
            first_slice = digit[:i]
            minimal = [first_slice[-1], -1]

            for j, jitem in enumerate(first_slice):
                if jitem > temp and jitem <= minimal[0]:
                    minimal = [jitem, j]

            temporal = temp
            rest_slice[0] = minimal[0]
            first_slice[minimal[1]] = temporal
            first_slice.sort(reverse=True)

            final_digit = first_slice + rest_slice
            final_digit.reverse()
            break

    if not final_digit:
        return -1

    return int("".join([str(i) for i in final_digit]))


if __name__ == "__main__":
    result = next_bigger(int(input("Enter the digit: \n")))
    print(result)
