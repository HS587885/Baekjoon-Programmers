def solution(n, words):
    used_words = set()
    used_words.add(words[0])

    for i in range(1, len(words)):
        if words[i] in used_words or words[i-1][-1] != words[i][0]:
            player = (i % n) + 1
            turn = (i // n) + 1
            return [player, turn]
        used_words.add(words[i])

    return [0, 0]



