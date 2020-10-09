def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort()
    n = len(scores)
    i = 0
    result = []

    for alice_score in alice:
        while i < n and scores[i] <= alice_score:
            i += 1

        # scores [80, 90, 100]
        # alice 90

        result.append(n - i + 1)

    for i in result:
        print(i)


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    climbingLeaderboard(ranked, player)
