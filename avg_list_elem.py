# Only error handles empty list
def avg_elements(lst):

    # Handle empty lst
    if len(lst) == 0:
        return 0
    else:
        return sum(lst) / len(lst)
