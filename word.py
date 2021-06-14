with open('word.inp', 'r') as inFile:
    list_word = list(inFile.readline().split())

# 정렬 기준 : 길이(짧은것부터) > 문자(대문자 우선, 백과사전순) > 숫자(작은수부터)


def sorting():
    for count in range(1, len(list_word) + 1):
        for i in range(len(list_word) - count):
            list_word[i], list_word[i+1] = compare(list_word[i], list_word[i+1])


def compare(a, b):
    if len(a) > len(b):
        a, b = b, a
    elif len(a) < len(b):
        pass
    else:
        for idx in range(len(a)):
            if a[idx] == b[idx]:
                continue

            if a[idx].isdigit() and not b[idx].isdigit():
                a, b = b, a
            elif not a[idx].isdigit() and b[idx].isdigit():
                pass
            else:
                if a[idx].isdigit() and b[idx].isdigit():
                    if int(a[idx]) > int(b[idx]):
                        a, b = b, a
                elif a[idx].isupper() and b[idx].isupper():
                    if a[idx] > b[idx]:
                        a, b = b, a
                elif a[idx].islower() and b[idx].isupper():
                    a, b = b, a
                elif a[idx].isupper() and b[idx].islower():
                    pass
                else:
                    if a[idx] > b[idx]:
                        a, b = b, a
            break
    return a, b


sorting()

result = ""
for item in list_word:
    result += "{} ".format(item)

with open('word.out', 'w') as outFile:
    outFile.write(result.rstrip())
