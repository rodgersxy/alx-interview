# def _primes(n):
#     """
#     Returns  a list of primes <= n
#     """
#     prime_list = [True] * (n + 1)
#     for i in range(3, int((n + 1)**0.5) + 1, 2):
#         if prime_list[i]:
#             prime_list[i * i::2 * i] = [False] * (((n + 1) - i * i - 1) //
#                                              (2 * i) + 1)
#     return [2] + [i for i in range(3, n + 1, 2) if prime_list[i]]
# print(_primes(1000))
