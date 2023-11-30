import os

def getScoreDifference(numSeq):
    player_scores = [0, 0]

    for round_num in range(len(numSeq) // 2):
        # First player picks two numbers
        player_scores[0] += numSeq[2 * round_num]
        # Second player picks one number
        player_scores[1] += numSeq[2 * round_num + 1]

    score_difference = player_scores[0] - player_scores[1]
    return score_difference

if __name__ == "__main__":
    # Open a file for writing instead of using the environment variable
    with open("output.txt", "w") as fptr:
        numSeq_count = int(input().strip())

        numSeq = []

        for _ in range(numSeq_count * 2):  # Read all the numbers in the sequence
            numSeq_item = int(input().strip())
            numSeq.append(numSeq_item)

        result = getScoreDifference(numSeq)

        fptr.write(str(result) + '\n')
