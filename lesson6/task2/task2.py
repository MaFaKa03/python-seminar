def same_by(condition, nums):
    return "same" if len(set(map(condition, nums))) == 1 else "different"


values = [0, 2, 10, 6]
print(same_by(lambda x: x % 2, values))

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')