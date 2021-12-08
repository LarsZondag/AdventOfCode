# %%
from typing import List
with open('input.txt') as f:
    lines = [l.strip().split(" | ") for l in f.readlines()]
inputs = [l[0].split() for l in lines]
outputs = [l[1].split() for l in lines]


# %%
# First determine the sets that comprise certain digits
true_mapping = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg')
}

# Determine which options are still open for a set of given length
lengthOptions = set([len(ss) for ss in true_mapping.values()])
optionsBasedOnLength = {length: [] for length in lengthOptions}
for option, ss in true_mapping.items():
    optionsBasedOnLength[len(ss)].append(option)

# Take a known set X and an unknown set Y. Take the difference of Y wrt X.
# Determine which options remain based on the length of this difference
# For example, set('abcefg') - set('cf') = set('abeg')
# Thus this difference has length 4. The only option for len(set(X) - set(Y)) == 4
# is for the digit 0. Therefore we know the unknown set must represent 0
# If more options are present, take the intersection between the options from this mapping
# and the options that were still under investigation.
remainder_options = {x: {} for x in true_mapping.keys()}
for known_digit, known_set in true_mapping.items():
    for unknown_digit, unknown_set in true_mapping.items():
        if known_digit == unknown_digit:
            continue

        length_of_remaining = len(known_set - unknown_set)
        try:
            remainder_options[known_digit][length_of_remaining].append(
                unknown_digit)
        except:
            remainder_options[known_digit][length_of_remaining] = [
                unknown_digit]
# %%


def find_output(ii: List[str], oo: List[str]):
    dictionary = {}
    unidentified = []
    # Build the dictionary from digits with a unique length
    # If the string does not have a unique length, determine how many
    # options are available based on its length.
    # E.g. a set with length 5 can be either a 2, 3, or 5.
    for s in (ii + oo):
        ss = set(s)
        ss_length = len(ss)
        if ss_length == 2:
            dictionary[1] = ss
        elif ss_length == 4:
            dictionary[4] = ss
        elif ss_length == 3:
            dictionary[7] = ss
        elif ss_length == 7:
            dictionary[8] = ss
        else:
            if all([a['set'] != ss for a in unidentified]):
                unidentified.append(
                    {'set': ss, 'options': set(optionsBasedOnLength[len(ss)])})

    # Now we start to narrow down the options by determining the difference
    # wrt digits we already know. Take the union of options under investigation
    # and possible options based on the difference. See mapping above.
    while len(unidentified) > 0:
        for known_digit, known_set in dictionary.items():
            for u in unidentified:
                currentSet = u['set']
                currentOptions = u['options']
                left_remainder_length = len(known_set - currentSet)
                left_remainder_options = remainder_options[known_digit][left_remainder_length]
                options_left = currentOptions.intersection(
                    left_remainder_options)
                u['options'] = options_left

        newlyIdentified = [u for u in unidentified if len(u['options']) == 1]
        for u in newlyIdentified:
            dictionary[u["options"].pop()] = u["set"]
        unidentified = [u for u in unidentified if len(u['options']) > 1]

    reverseDictionary = {
        "".join(sorted(ss)): i for i, ss in dictionary.items()}
    oo_digits = [reverseDictionary["".join(sorted(o))] for o in oo]
    oo_strings = [str(o) for o in oo_digits]
    oo_string = "".join(oo_strings)
    oo_value = int(oo_string)
    return oo_value


output_solutions = [find_output(ii, oo) for ii, oo in zip(inputs, outputs)]

print(sum(output_solutions))
# %%
