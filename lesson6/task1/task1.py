def find_farthest_orbit(nums_list):
    return max([(a[0]*a[1],a) for a in nums_list if a[0]!=a[1]])[1]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))