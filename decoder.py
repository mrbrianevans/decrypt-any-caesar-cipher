def shift_string(string: str, positions: int):
    shifted_string = ""
    for character in string:
        if character == " ":  # preserve spaces
            new_character: chr = " "
        else:
            new_character: chr = chr((ord(character) + positions) % 26 + ord('a'))
        shifted_string += str(new_character)
    return shifted_string


def count_real_words(string: str):
    real_words = open("words.txt").read().split()
    words = string.split()
    count = 0
    for word in words:
        if word in real_words:
            count += 1
    return count


def decipher_by_word_length(cipher_text):
    tracker = {}
    for i in range(26):
        count = count_real_words(shift_string(cipher_text, i))
        # if count > 0:
            # If real words were found by shifting the characters, it will print the size of shift
            # print(f"Shifting by {i} positions yielded {count} real words")
        tracker[i] = count
    tracker = {k: v for k, v in sorted(tracker.items(),
                                       key=lambda item: item[1],
                                       reverse=True)}
    highest_frequency_counter = -1
    highest_frequency_position_shift = ''
    # Printing tracker will show how many real words were yielded by different shifts
    # print(tracker)
    for positions_shifted, ocurrances in tracker.items():
        if ocurrances > highest_frequency_counter:
            highest_frequency_counter = ocurrances
            highest_frequency_position_shift = positions_shifted
    # Running count_characters will print the frequency for each character, original and translated
    # count_characters(cipher_text, highest_frequency_position_shift)

    if highest_frequency_position_shift == 0:
        return "Could not decrypt. Try a longer string"

    decoded_message = shift_string(cipher_text, highest_frequency_position_shift)

    # This prints details of the decryption to the console
    # print(f"Letters have been shifted {highest_frequency_position_shift} places in the alphabet")
    # print("\nThe decoded message is: \n")
    # print(decoded_message)

    return decoded_message


if __name__ == '__main__':
    encoded_clues = [
        "&D6 J@FC !JE9@? D<:==DP",
        "xE :D 72:C E@ 2DDF>6 E92E E96 4=62C E6IE :D HC:EE6? :? t?8=:D9]",
        "*@F 42? 2DDF>6 E92E E96 >6DD286 @?=J 4@?E2:?D =@H6C 42D6 492C24E6CD[ H9:E6\\",
        "~?=J 492C24E6CD 2C6 6?4CJAE65]",
        "r@F?E E96 7C6BF6?4J @7 E96 G2C:@FD 6>@E:4@?D[ :D E96C6 2?JE9:?8 DFDA:4:@FDn",
        "(:<:A65:2 92D ?:46 A286 @? =6EE6C 7C6BF6?4:6D]"
    ]
    decoded_clues = map(decipher_by_word_length, encoded_clues)

    for decoded_clue in decoded_clues:
        print(decoded_clue)
