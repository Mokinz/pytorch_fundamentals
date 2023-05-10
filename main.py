def solution(S):
    # Implement your solution here

    import random

    S = list(S)
    length = len(S)

    for letter in range(length // 2):
        if S[letter] == S[-(letter + 1)] and S[letter] != "?":
            continue
        elif S[letter] == "?" and S[-(letter + 1)] != "?":
            S[letter] = S[-(letter + 1)]
        elif S[letter] != "?" and S[-(letter + 1)] == "?":
            S[-(letter + 1)] = S[letter]
        elif S[letter] == "?" and S[-(letter + 1)] == "?":
            S[letter] = chr(random.randint(97, 122))
            S[-(letter + 1)] = S[letter]
        elif S[letter] != S[-(letter + 1)]:
            return "NO"

    return "".join(S)


print(solution("allal??"))
