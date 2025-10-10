from time import time
def ft_tqdm(lst: range) -> None:
    """
    Makes a progress bar
    takes a range objectas an argument
    """
# 100%|[===============================================================>]| 333/333 333/333 [00:01<00:00, 191.61it/s]
# percentage
# | progress bar |
# = progress completed
# empty = half done
# > current position
# current iteration count / total iterations.
# [
# 00:01 Elapsed time
# <00:00 estimated remaining time
# , 191.61it/s iterations/s
# ]
