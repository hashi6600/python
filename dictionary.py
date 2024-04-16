def word_counter(word):
    """
    Counts the frequency of each character in a word.
    Args:
    word: A string.
    Returns:
    A dictionary mapping each character in the word to its frequency.
    """
    # Create a dictionary to store the character counts.
    counts = {}

    # Iterate over the word and count the occurrences of each character.
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

print(word_counter("Mississippi"))