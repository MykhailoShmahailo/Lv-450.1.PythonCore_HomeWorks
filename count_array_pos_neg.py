def count_positives_sum_negatives(arr):
    count_positive = len(list(n for n in arr if n > 0))
    negative_sum = sum(n for n in arr if n < 0)
    return [count_positive, negative_sum] if len(arr) > 0 else []