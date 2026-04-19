def number_theory(k):
    import heapq

    remainders = [float('inf')] * k
    heap = ([(i, i) for i in range(1, min(10, k))])
    heapq.heapify(heap)

    while heap:
        digit_sum, remainder = heapq.heappop(heap)
        for d in range(10):
            new_remainder = (remainder * 10 + d) % k
            new_sum = digit_sum + d
            if remainders[new_remainder] > new_sum:
                remainders[new_remainder] = new_sum
                heapq.heappush(heap, (new_sum, new_remainder))

    return remainders[0]


k = int(input())
print(number_theory(k))
