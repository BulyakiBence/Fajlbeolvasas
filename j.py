import shutil

RED = "\033[91m"
RESET = "\033[0m"

width = shutil.get_terminal_size().columns

art = [
    "     JJJJJJJJJ",
    "          J",
    "          J",
    "          J",
    "    J     J",
    "     JJJJJ",

    "",
    "   **     **",
    " ****** ******",
    " ************",
    "  **********",
    "    ******",
    "      **"
]

for line in art:
    print(RED + line.center(width) + RESET)
