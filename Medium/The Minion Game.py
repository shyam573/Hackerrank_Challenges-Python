def minion_game(s):
    # your code goes here

    vowels = "AEIOU"

    score_a = 0
    score_b = 0
    for i in range(len(s)):
        if s[i] in vowels:
            score_a += (len(s)-i)
        else:
            score_b += (len(s)-i)

    if score_a > score_b:
        print("Kevin", score_a)
    elif score_a < score_b:
        print("Stuart", score_b)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)