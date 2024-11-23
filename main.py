from enum import Enum

class TextColor(Enum):
    # Standard colors
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    GRAY = 90  # Added gray color for verbose output
    RESET = 0

    # Bright colors
    BRIGHT_BLACK = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97

    # Background colors
    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_MAGENTA = 45
    BG_CYAN = 46
    BG_WHITE = 47
    BG_GRAY = 100  # Added gray background
    BG_BRIGHT_BLACK = 100
    BG_BRIGHT_RED = 101
    BG_BRIGHT_GREEN = 102
    BG_BRIGHT_YELLOW = 103
    BG_BRIGHT_BLUE = 104
    BG_BRIGHT_MAGENTA = 105
    BG_BRIGHT_CYAN = 106
    BG_BRIGHT_WHITE = 107

def colored_print(text: str, color: TextColor):
    """Print text in the specified color using ANSI escape codes."""
    print(f"\033[{color.value}m{text}\033[0m")


class BoxPrinter:
    def __init__(self, indent_char: str = "    "):
        """
        Initializes the BoxPrinter with no active box and an empty data queue.
        
        :param indent_char: Character(s) to use for indentation. Defaults to four spaces.
        """
        self.current_title = None
        self.contents = []
        self.indent_char = indent_char

    def start_box(self, title: str):
        """
        Starts a new box with the given title. Clears any previous box data.
        
        :param title: Title of the new box
        """
        self.current_title = title
        self.contents = []

    def queue_print(self, content: str, indent: int = 0):
        """
        Adds content to the current box with optional indentation.
        
        :param content: The content to queue for printing
        :param indent: The level of indentation (number of indent_char repetitions)
        """
        if self.current_title is None:
            raise ValueError("No active box. Use start_box() to begin a new box.")
        indented_content = f"{self.indent_char * indent}{content}"
        self.contents.append(indented_content)

    def print_box(self):
        """
        Prints the contents of the current box with the title and formatting.
        """
        if self.current_title is None:
            raise ValueError("No active box. Use start_box() to begin a new box.")
        
        # Print box title
        print()
        print("=" * 10 + f" {self.current_title} " + "=" * 10)
        
        # Print box contents
        for line in self.contents:
            print("|| " + line)
        
        # Print box footer
        print("=" * (20 + len(self.current_title)))
        print()
