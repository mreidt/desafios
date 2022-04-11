import argparse
from sys import exit

from constants import DEFAULT_INPUT_TEXT, DEFAULT_MAXIMUM_LINE_WIDTH
from idwall_text_wrap import IdwallTextWrap


def main(
    operation: str,
    input_text: str,
    line_width: int,
    output_filename: str,
    use_python_wrap: bool,
):
    """Executes the strings operations.

    Args:
        operation (str): Type of operation (left_allign or justify).
        input_text (str): The input text.
        line_width (int): Maximum line width.
        output_filename (str): The output filename.
        use_python_wrap (bool): Determines the use of built-in python wrap operation.

    Raises:
        ValueError: Unknown operation found.
    """
    idwall_text_wrap = IdwallTextWrap()
    try:
        operation = operation.lower()
        if operation == "left_allign":
            if not output_filename:
                output_filename = "output-part1.txt"
            idwall_text_wrap.left_allign_text(
                input_text, line_width, output_filename, use_python_wrap
            )
        elif operation == "justify":
            if not output_filename:
                output_filename = "output-part2.txt"
            idwall_text_wrap.justify_text(
                input_text, line_width, output_filename, use_python_wrap
            )
        else:
            raise ValueError(
                f"You tried to execute an unknown operation ({operation}). "
                "Available operations are 'left_allign' or 'justify'."
            )
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Idwall challenge")
    parser.add_argument(
        "operation", type=str, help="The operation to be done: left_allign or justify"
    )
    parser.add_argument(
        "-t",
        "--input_text",
        nargs="?",
        default=DEFAULT_INPUT_TEXT,
        help="The text to be wrapped.",
    )
    parser.add_argument(
        "-w",
        "--line_width",
        nargs="?",
        default=DEFAULT_MAXIMUM_LINE_WIDTH,
        help="Maximum line width.",
    )
    parser.add_argument(
        "-f",
        "--output_filename",
        nargs="?",
        default=None,
        help="The output filename to save wrapped text.",
    )
    parser.add_argument(
        "-p",
        "--use_python_wrap",
        nargs="?",
        default=None,
        const=True,
        help="Use python built-in wrap function.",
    )
    args = parser.parse_args()

    if args.operation.lower() not in ["left_allign", "justify"]:
        print(
            f"The operation must be: left_allign or justify! Received {args.operation.lower()}"
        )
        exit(1)
    # Those errors should never occur, but tested, just in case.
    if args.input_text and not isinstance(args.input_text, str):
        print(f"Input text should be a string! Received {args.input_text}.")
        exit(2)
    if args.output_filename and not isinstance(args.output_filename, str):
        print(f"Output filename should be a string! Received {args.output_filename}.")
        exit(3)

    if args.line_width:
        try:
            args.line_width = int(args.line_width)
        except ValueError:
            print(f"Line width should be an integer! Received {args.line_width}.")
            exit(4)

    main(
        args.operation.lower(),
        args.input_text,
        args.line_width,
        args.output_filename,
        args.use_python_wrap,
    )
