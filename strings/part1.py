import argparse
from sys import exit

from constants import DEFAULT_INPUT_TEXT, DEFAULT_MAXIMUM_LINE_WIDTH
from idwall_text_wrap import IdwallTextWrap


def main(
    input_text: str,
    line_width: int,
    output_filename: str,
    show_configuration: bool,
    use_python_wrap: bool,
):
    idwall_text_wrap = IdwallTextWrap()
    try:
        idwall_text_wrap.wrap_text(
            input_text, line_width, output_filename, show_configuration, use_python_wrap
        )
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Idwall challenge - Part 1")
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
        "-c",
        "--show_config",
        nargs="?",
        default=None,
        const=True,
        help="Print configuration during execution.",
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

    # Those errors should never occur, but tested, just in case.
    if args.input_text and not isinstance(args.input_text, str):
        print(f"Input text should be a string! Received {args.input_text}.")
        exit(1)
    if args.output_filename and not isinstance(args.output_filename, str):
        print(f"Output filename should be a string! Received {args.output_filename}.")
        exit(1)

    if args.line_width:
        try:
            args.line_width = int(args.line_width)
        except ValueError:
            print(f"Line width should be an integer! Received {args.line_width}.")
            exit(1)

    main(
        args.input_text,
        args.line_width,
        args.output_filename,
        args.show_config,
        args.use_python_wrap,
    )
