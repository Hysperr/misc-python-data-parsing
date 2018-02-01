"""
Mask the emails (E:) and phone numbers (P:)
with asteriks. 5 *'s between email name's
first and last letter, preserving the @domain.
Mask phone number with *'s except last 4 digits
and format properly.
"""

import re

# Test cases (emails and phone numbers are fictional)
test_case_1 = 'E:jackAndJill@volcanicpenguin.comE:maybelle@dairycow.comP:(333)456-7890P:+1333456-8888'
test_case_2 = 'E:jackAndJill@volcanicpenguin.comP:+13334567890'
test_case_3 = 'E:customexample@example.edu P: +122 760 555 9191'
test_case_4 = 'E:camo7@example.edu P: +43-(760)-050-3418'
test_case_5 = 'E:camo7@example.edu E:another@anno.eduP: +43-(760)-050-3418'

data = test_case_1

# split data where delimiter='E:' or 'P:', remove '', make list => ['E:camo7@example.edu', 'P:+43-(760)-050-3418']
entry = list(filter(None, re.split('E:|P:', data)))
for i, x in enumerate(entry):
    x = x.replace(' ', '')
    if '@' in x:
        # Dealing with email
        # Reverse split on '@' => roar@volcanicpenguin.com => dsplit[0] = roar & dsplit[1] = volcanicpenguin.com
        domain_split = x.rsplit('@', 1)
        # Insert middle of fragment with 5 '*'s, retain first and last letter of domain_split[0]
        x = 'E:' + x[0] + '*****' + domain_split[0][-1] + '@' + domain_split[1]
        entry[i] = x
    else:
        # Dealing with phone number
        x = re.sub('[()\-\s]+', '', x)
        # Replace appropriate indices with '*'
        for idx, tmp in enumerate(x):
            if tmp.isdigit() and 0 <= idx < len(x)-4:
                x = x.replace(tmp, '*', 1)
        # Insert dashes into number
        position, offset = -4, 0
        while abs(position-offset) < len(x):
            x = x[:position-offset] + '-' + x[position-offset:]
            offset += 4
        # Piece the fragment together
        x = 'P:' + x[1:] if x[0] == '-' else 'P:' + x
        entry[i] = x

entry = ''.join(entry)
print(entry)
