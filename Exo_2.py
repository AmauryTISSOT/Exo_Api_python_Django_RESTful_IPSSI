def score_of_string(s: str):
    print(f"Input: {s}\n")
    score = 0
    for i in range(len(s) - 1):
        current_char = s[i]
        next_char = s[i + 1]
        difference = abs(ord(current_char) - ord(next_char))
        score += difference
        print(
            f"Comparaison {i + 1}: '{current_char}' (ASCII {ord(current_char)}) "
            f"vs '{next_char}' (ASCII {ord(next_char)}) -> Différence = {difference}"
        )
        print(f"Score intermédiaire : {score}\n")
    return score


print(score_of_string("hello"))
