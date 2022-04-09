from textwrap import wrap

from constants import DEFAULT_INPUT_TEXT, DEFAULT_MAXIMUM_LINE_WIDTH
from repository import idwall_strings_repository


class IdwallTextWrap:
    def _wrap_text(
        self, input_text, maximum_line_width, output_filename, use_python_wrap
    ):
        idwall_strings_repository._check_words_size(input_text, maximum_line_width)
        if use_python_wrap:
            wrapped_text = wrap(input_text, maximum_line_width)
        else:
            wrapped_text = idwall_strings_repository._manually_wrap_text(
                input_text, maximum_line_width
            )
        return wrapped_text

    def left_allign_text(
        self,
        input_text: str,
        maximum_line_width: int,
        output_filename: str = "output-part1.txt",
        use_python_wrap: bool = False,
    ) -> None:
        """Left allign a text.

        Args:
            input_text (str, optional): The text to be wrapped.
            maximum_line_width (int, optional): Maximum line width.
            output_filename (str, optional): The filename in wich text will be saved. Defaults to "output-part1.txt".
            use_python_wrap (bool, optional): Use Python built-in method to wrap. Defaults to False.
        """
        output_text = self._wrap_text(
            input_text, maximum_line_width, output_filename, use_python_wrap
        )
        idwall_strings_repository._write_to_file(output_text, output_filename)

    def justify_text(
        self,
        input_text: str = DEFAULT_INPUT_TEXT,
        maximum_line_width: int = DEFAULT_MAXIMUM_LINE_WIDTH,
        output_filename: str = "output-part2.txt",
        use_python_wrap: bool = False,
    ):
        """Justify a text.

        Args:
            input_text (str, optional): The input text to be justified.. Defaults to DEFAULT_INPUT_TEXT.
            maximum_line_width (int, optional): The desired line width. Defaults to DEFAULT_MAXIMUM_LINE_WIDTH.
            output_filename (str, optional): The output filename to save the results. Defaults to "output-part2.txt".
            use_python_wrap (bool, optional): Use Python built-in method to wrap. Defaults to False.
        """
        wrapped_text = self._wrap_text(
            input_text, maximum_line_width, output_filename, use_python_wrap
        )
        splitted_lines = [line.split() for line in wrapped_text]
        output_text = idwall_strings_repository._justify_text_in_list_of_lines(
            maximum_line_width, splitted_lines
        )
        idwall_strings_repository._write_to_file(output_text, output_filename)
