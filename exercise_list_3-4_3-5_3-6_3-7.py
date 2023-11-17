# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

dinner_invite = ['daniele', 'alice', 'marlon']
print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.

# Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is still in
# your list.

dinner_invite = ['daniele', 'alice', 'marlon']
print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Infelizmente {dinner_invite[-1].title()} não irá comparecer ao jantar.')

dinner_invite.remove('marlon')
dinner_invite.insert(2, 'joãozinho')

print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.

# Use insert() to add one new guest to the beginning of your list.

# Use insert() to add one new guest to the middle of your list.

# Use append() to add one new guest to the end of your list.

# print a new set of invitation messages, one for each person in your list.

dinner_invite = ['daniele', 'alice', 'marlon']
print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Infelizmente {dinner_invite[-1].title()} não irá comparecer ao jantar.')

dinner_invite.remove('marlon')
dinner_invite.insert(2, 'joãozinho')

print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Gostaria de informar a vocês, {dinner_invite[0].title()}, {dinner_invite[1].title()} e {dinner_invite[2].title()} que encontrei uma mesa maior.')

dinner_invite.insert(0, 'mariazinha')
dinner_invite.insert(2, 'alicezinha')
dinner_invite.append('ratinho')

print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[3].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[4].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[5].title()}, para o jantar no restaurante.')

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

dinner_invite = ['daniele', 'alice', 'marlon']
print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Infelizmente {dinner_invite[-1].title()} não irá comparecer ao jantar.')

dinner_invite.remove('marlon')
dinner_invite.insert(2, 'joãozinho')

print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Gostaria de informar a vocês, {dinner_invite[0].title()}, {dinner_invite[1].title()} e {dinner_invite[2].title()} que encontrei uma mesa maior.')

dinner_invite.insert(0, 'mariazinha')
dinner_invite.insert(2, 'alicezinha')
dinner_invite.append('ratinho')

print(f'Gostaria de convidar você, {dinner_invite[0].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[1].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[2].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[3].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[4].title()}, para o jantar no restaurante.')
print(f'Gostaria de convidar você, {dinner_invite[5].title()}, para o jantar no restaurante.')

print('Vou poder convidar apenas duas pessoas para o jantar!')

dinner_unvited = dinner_invite.pop(0)
print(f'Sinto muito, mas {dinner_unvited.title()} não está mais convidado(a).')

dinner_unvited = dinner_invite.pop(1)
print(f'Sinto muito, mas {dinner_unvited.title()} não está mais convidado(a).')

dinner_unvited = dinner_invite.pop(3)
print(f'Sinto muito, mas {dinner_unvited.title()} não está mais convidado(a).')

dinner_unvited = dinner_invite.pop(2)
print(f'Sinto muito, mas {dinner_unvited.title()} não está mais convidado(a).')

print(f'{dinner_invite[0].title()}, você ainda está convidada!')
print(f'{dinner_invite[1].title()}, você ainda está convidada!')

print(dinner_invite)

del dinner_invite[0]
print(dinner_invite)
del dinner_invite[0]
print(dinner_invite)
