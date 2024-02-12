def perform_set_operations(set1, set2):
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    difference_result = set1.difference(set2)
    symmetric_difference_result = set1.symmetric_difference(set2)

    print("Union of {} and {} is {}".format(set1, set2, union_result))
    print("Intersection of {} and {} is {}".format(set1, set2, intersection_result))
    print("Difference of {} and {} is {}".format(set1, set2, difference_result))
    print("Symmetric difference of {} and {} is {}".format(set1, set2, symmetric_difference_result))

set_E = {0, 1, 2, 3, 4, 5}
set_N = {2, 4, 6, 8}

perform_set_operations(set_E, set_N)
