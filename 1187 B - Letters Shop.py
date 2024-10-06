# https://codeforces.com/contest/1187/problem/B -  Letters Shop
# Start:    Finish:     Duration:    Attempts:     Difficulty: 1300
n = int(input())
name = input()
mydict = {chr(i): [] for i in range(97, 123)}
for i in range(n):
    mydict[name[i]].append(i + 1)

k = int(input())
for i in range(k):
    z = list(input())
    mydict2 = dict()
    for i in z:
        mydict2[i] = mydict2.get(i, 0) + 1
    maxi = -1
    for i in mydict2:
        maxi = max(maxi, mydict[i][mydict2[i] - 1])
    print(maxi)

# def letters_shop(dict_word, no_of_letters, friend):
#
#     for i in range(no_of_letters):
#         dict_name = dict()
#         for i in friend:
#             dict_name[i] = dict_name.get(i, 0) + 1
#         maximum_i = -1
#         for i in dict_name:
#             maximum_i = max(maximum_i, dict_word[i][dict_name[i] - 1])
#     return maximum_i
#
# if __name__ == '__main__':
#     b = 'abcdefghijklmnopqrstuvwxyz'
#     length_of_word = int(input())
#     word = input()
#     word_dict = {i: [] for i in b}
#     for i in range(length_of_word):
#         word_dict[word[i]].append(i + 1)
#     no_of_friends = int(input())
#     for i in range(no_of_friends):
#         friend_name = input()
#         print(letters_shop(word_dict, length_of_word, friend_name))



