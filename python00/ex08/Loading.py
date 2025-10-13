from time import time
from shutil import get_terminal_size


def format_time(seconds):
    """
    Takes the seconds and turns them into the format MM:SS

    Args:
        seconds (float): Time in seconds

    Returns:
        str: Time in the format MM:SS
    """
    time_str = f"{int(seconds // 60):02d}:{(seconds % 60):02.0f}"
    return time_str


def ft_tqdm(lst: range) -> None:
    """
    Makes a progress bar

    Args:
        lst: (range): The range to iterate through

    Yields:

    """
    # Yield is the keyword used to return a value without stopping execution

    try:
        range_len = len(lst)
    except TypeError:
        lst = list(lst)
        range_len = len(lst)
    if range_len == 0:
        print("0it [00:00, ?it/s]")
        return

    start_time = time()

    terminal_width = \
        get_terminal_size().columns - (5 + (4 + len(str(len(lst))) * 2) + 19)
    progress_bar_width = max(1, terminal_width)

    # 5                             => "100%|"
    # 4 + len(str(len(lst))) * 2)   => "| 333/333 "
    # 14                            => "[00:00<00:00, it/s]"
    last_print_time = start_time
    for i, item in enumerate(lst, start=1):
        progress = i
        percent = int(progress / range_len * 100)
        elapsed_time = time() - start_time
        speed = i / (elapsed_time if elapsed_time > 1e-8 else 1e-8)
        fspeed = f"{speed:.2f}"
        time_left = (range_len - i) / (speed if speed > 1e-8 else 1e-8)
        time_info = \
            f"[{format_time(elapsed_time)}<{format_time(time_left)}, \
{fspeed}it/s]"
        time_info_len = 19 + len(str(fspeed))
        progress_bar_width = max(1, terminal_width - len(str(fspeed)))
        progress_bar_len = int(progress / range_len * (progress_bar_width))
        progress_bar = f"{'█' * progress_bar_len:<{progress_bar_width}}"
        bar_text = \
            f"{percent:>3}%|{progress_bar}| {progress}/{range_len} \
{time_info:>{time_info_len}}"
        now = time()
        # Print if enough time has passed or it's the last item
        if now - last_print_time > 0.05 or i == range_len:
            print(bar_text[:get_terminal_size().columns], end="\r", flush=True)
            last_print_time = now
        yield item
    print(bar_text[:get_terminal_size().columns], flush=True)


# 100%|[==============>]| 333/333 [00:01<00:00, 191.61it/s]
# percentage ✅
# | progress bar |
# "█""          => progress completed ✅
# " "           => no progress
# ">"           => current position
# current iteration count / total iterations. ✅
# [00:01        =>Elapsed time ✅
# <00:00        =>estimated remaining time✅
# , 191.61it/s] => speed in iterations/s ✅

def main():
    ft_tqdm(range(0, 333))


if __name__ == "__main__":
    main()
