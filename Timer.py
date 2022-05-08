import time
import rich
from rich import print

try:
    start_time = time.time()
    while True:
        time.sleep(1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_duration = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print(f"[cyan]{formatted_duration}[/cyan]", end="\r"*8)
except KeyboardInterrupt:
    print("[red]INTERNAL SERVER ERROR[/red]")
    print(f"[cyan]{formatted_duration}[/cyan]")
