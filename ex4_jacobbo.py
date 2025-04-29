"""
Name: Jacob Bondar
UserName: jacobbo
ID: 322336488

The program provides two distinct exercises for the user to choose from.

In the first exercise, the program prompts the user to input a series of numbers
 until an empty input is given. It then calculates and displays
 the sum, minimum, maximum, and average of the input values.
The results are clearly printed, and the function that performs these
 calculations is documented with a help() call.

The second exercise allows the user to enter sentences repeatedly.
For each sentence, the program uses both list comprehensions and
 lambda with map/filter techniques to perform several tasks:
 - Count and display the length of each word (if alphabetic).
 - Count each letter’s occurrences in the sentence.
 - Generate tuples for each word showing the number of vowels and consonants.
 - List all words with 4 or more letters.

After processing the sentence with both approaches, the program compares their
 results and displays whether they matched (they will always match).
It also prints a side-by-side view
  of all the results from both methods for easy comparison.

The user can repeatedly choose between "ex1" and "ex2", or press Enter to exit
 the program.
"""

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def ex1():
    list_nums = get_input()

    sum, min, max, avg = receive_values(*list_nums)

    show_values(list_nums, sum, min, max, avg)

#-------------------------------------------------------------------------------

def get_input():
    list_ret = []
    index = 1

    print("\nEnter numeric values.\nTo stop, press Enter.")
    while num_user := input(f"Enter value number #{index}: "):
        try:
            int(num_user)
        except ValueError:
            continue

        list_ret.append(int(num_user))
        index += 1

    return list_ret

#-------------------------------------------------------------------------------

def receive_values(*args):
    """
        The function receives numbers from the user and returns:
        - The sum of the numbers.
        - The smallest number.
        - The largest number.
        - The average of the numbers.
    """
    if not args: return 0, 0, 0, 0

    total_sum = sum(args)
    min_value = min(args)
    max_value = max(args)
    avg = total_sum / len(args)

    return total_sum, min_value, max_value, avg

#-------------------------------------------------------------------------------

def show_values(list_nums, sum_val, min_val, max_val, avg_val):
    print(f"The input was: {list_nums}\n")
    print(f"The sum is: {sum_val}\nThe min is: {min_val}\n"
          f"The max is: {max_val}\nThe avg_val is: {avg_val:.3f}\n")
    help(receive_values)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def ex2():
    while sentence := input("\nPlease enter a sentence: "):
        len_comp, counter_comp, pairs_comp, four_comp = do_list_comp(sentence)
        len_lam, counter_lam, pairs_lam, four_lam = do_lam(sentence)

        compare_results(len_comp, counter_comp, pairs_comp, four_comp,
                        len_lam, counter_lam, pairs_lam, four_lam)

        show_results(sentence, len_comp, counter_comp, pairs_comp, four_comp,
                               len_lam, counter_lam, pairs_lam, four_lam)
    print("\nReturning to main!")

#-------------------------------------------------------------------------------

def do_list_comp(sentence):
    arr_lengths = calc_lengths_comp(sentence.split())

    dict_counter = calc_counter_comp(sentence)

    list_vow_con = get_pairs_comp(sentence.split())

    list_four = get_above_four_comp(sentence.split())

    return arr_lengths, dict_counter, list_vow_con, list_four

#-------------------------------------------------------------------------------

def calc_lengths_comp(sentence_words):
    return [len(x) for x in sentence_words if x.isalpha()]

#-------------------------------------------------------------------------------

def calc_counter_comp(sentence):
    list_letters = [ch for ch in sentence if ch.isalpha()]
    list_letters = set(list_letters)

    return {char: sum(1 for c in sentence if c == char) for char in list_letters}

#-------------------------------------------------------------------------------

def get_pairs_comp(sentence_words):
    vowels = "aeiouAEIOU"

    return [(sum(1 for char in word if char in vowels),
                 sum(1 for char in word if char not in vowels))
                for word in sentence_words if word.isalpha()]

#-------------------------------------------------------------------------------

def get_above_four_comp(sentence_words):
    return [word for word in sentence_words if len(word) >= 4 and word.isalpha()]

#-------------------------------------------------------------------------------

def do_lam(sentence):
    arr_lengths = calc_lengths_lam(sentence.split())

    dict_counter = calc_counter_lam(sentence)

    list_vow_con = get_pairs_lam(sentence.split())

    list_four = get_above_four_lam(sentence.split())

    return arr_lengths, dict_counter, list_vow_con, list_four

#-------------------------------------------------------------------------------

def calc_lengths_lam(sentence_words):
    return list(map(lambda b: len(b), filter(lambda a: a.isalpha(), sentence_words)))

#-------------------------------------------------------------------------------

def calc_counter_lam(sentence):
    return dict(map(lambda c: (c, sum(1 for char in sentence if char == c)),
                    filter(lambda s: s.isalpha(), set(sentence))))

#-------------------------------------------------------------------------------

def get_pairs_lam(sentence_words):
    vowels = "aeiouAEIOU"

    return list((map(lambda w:
                     ((sum(map(lambda c: 1 if c in vowels else 0, w))),
                      sum(map(lambda c: 1 if c not in vowels else 0, w))),
                     filter(lambda word: word.isalpha(), sentence_words))))

#-------------------------------------------------------------------------------

def get_above_four_lam(sentence_words):
    return list(map(lambda w: w , filter(lambda word: len(word) >= 4 and word.isalpha() ,sentence_words)))

#-------------------------------------------------------------------------------

def compare_results(len_comp, counter_comp, pairs_comp, four_comp,
                    len_lam, counter_lam, pairs_lam, four_lam):
    if (len_comp == len_lam and
            counter_comp == counter_lam and
            pairs_comp == pairs_lam and
            four_comp == four_lam):
        print("\nThe two methods gave the same results!")
    else: print("\nThe two methods didn't gave the same results!")

#-------------------------------------------------------------------------------

def show_results(sentence, len_comp, counter_comp, pairs_comp, four_comp,
                           len_lam, counter_lam, pairs_lam, four_lam):
    print(f"The sentence input is: {sentence}\n")

    print(f"The length words from list comprehension is:\n{len_comp}\n"
          f"The length words from lambda + map / filter is:\n{len_lam}\n")
    print(f"The counter letters from list comprehension is:\n{counter_comp}\n"
          f"The counter letters from lambda + map / filter is:\n{counter_lam}\n")
    print(f"The tuple vowels from list comprehension is:\n{pairs_comp}\n"
          f"The tuple vowels from lambda + map / filter is:\n{pairs_lam}\n")
    print(f"The words above 4 len from list comprehension is:\n{four_comp}\n"
          f"The words above 4 len from lambda + map / filter is:\n{four_lam}\n")

#-------------------------------------------------------------------------------

#main
while input_user := input("\nPlease enter:\n"
                       "'ex1' for the first exercise.\n"
                       "'ex2' for the second exercise.\n"
                       "Press Enter to end the run: "):
    if input_user == "ex1":
        ex1()
    elif input_user == "ex2":
        ex2()
    else:
        print("\nNo matching requests, try again.")