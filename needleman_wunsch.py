# match_score: The score given for a match between two characters in the sequences.
# A positive number encourages alignments of identical characters.

# mismatch_penalty: The penalty (a negative number) for a mismatch between two characters.
# This discourages alignments of different characters.

# gap_penalty: The penalty (a negative number) for introducing a gap into one of the sequences.
# This is used to handle insertions and deletions.
def needleman_wunsch(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    # Determine the lengths of the two sequences
    m, n = len(seq1), len(seq2)

    # Initialize a matrix to hold the scores for alignments
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix with gap penalties
    for i in range(m + 1):
        score_matrix[i][0] = gap_penalty * i
    for j in range(n + 1):
        score_matrix[0][j] = gap_penalty * j

    # Fill in the score matrix with scores for each possible alignment
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate scores for a match/mismatch or introducing a gap
            match = score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty

            # Choose the best score and update the matrix
            score_matrix[i][j] = max(match, delete, insert)

    # Backtrack to find the optimal alignment
    align1, align2 = '', ''
    i, j = m, n

    # Trace back from bottom right to top left
    while i > 0 and j > 0:
        score_current = score_matrix[i][j]
        score_diagonal = score_matrix[i - 1][j - 1]
        score_up = score_matrix[i][j - 1]
        score_left = score_matrix[i - 1][j]

        # Check if the current cell is from a match/mismatch
        if score_current == score_diagonal + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        # Check if the current cell is from a deletion (gap in seq2)
        elif score_current == score_left + gap_penalty:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1
        # Check if the current cell is from an insertion (gap in seq1)
        elif score_current == score_up + gap_penalty:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1

    # Complete the alignment for remaining sequence after traceback
    while i > 0:
        align1 += seq1[i - 1]
        align2 += '-'
        i -= 1
    while j > 0:
        align1 += '-'
        align2 += seq2[j - 1]
        j -= 1

    # Return the alignments in the proper order (reversed)
    return align1[::-1], align2[::-1]

# Example sequence
seq1 = "ATTACC"
seq2 = "GCATGCU"

# Running the algorithm with the example sequences
align1, align2 = needleman_wunsch(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2)

# Print the aligned sequences
print("Aligned Sequence 1:", align1)
print("Aligned Sequence 2:", align2)

seq1 = "ATTCCC"
seq2 = "GCATGCU"

# Running the algorithm with the example sequences
align1, align2 = needleman_wunsch(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2)

# Print the aligned sequences
print("Aligned Sequence 1:", align1)
print("Aligned Sequence 2:", align2)

seq1 = "ATTACATGC"
seq2 = "GCATGCU"

# Running the algorithm with the example sequences
align1, align2 = needleman_wunsch(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2)

# Print the aligned sequences
print("Aligned Sequence 1:", align1)
print("Aligned Sequence 2:", align2)