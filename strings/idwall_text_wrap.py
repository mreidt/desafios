import textwrap

from constants import DEFAULT_INPUT_TEXT, DEFAULT_MAXIMUM_LINE_WIDTH


class IdwallTextWrap:
    def _write_to_file(self, input_text: str, output_filename: str) -> None:
        """Write text to file.

        Args:
            input_text (str): The text to be write.
            output_filename (str): The file to be created.
        """
        with open(output_filename, "w") as out_file:
            out_file.write(input_text)

    def _show_configurations(
        self, input_text: str, line_width: int, output_filename: str
    ) -> None:
        """Print configurations in the screen.

        Args:
            input_text (str): The text to be wrapped.
            line_width (int): Maximum line width.
            output_filename (str): he filename in wich text will be saved.
        """
        print("*" * 50)
        print("CONFIGURATIONS")
        print(f"Input text: {input_text}")
        print(f"Input text size: {len(input_text)}")
        print(f"Maximum line width: {line_width}")
        print(f"Generated output file: {output_filename}")
        print("*" * 50)

    def _check_words_size(self, input_text: str, maximum_line_width: int) -> None:
        """Check words size, to ensure it will not be greater than maximum line size.

        Args:
            input_text (str): The input text to check the words.
            maximum_line_width (int): Maximum accepted line width.

        Raises:
            ValueError: If an word with size > maximum line size is found.
        """
        for word in input_text.split():
            if len(word) > maximum_line_width:
                raise ValueError(
                    f"Word {word} (size {len(word)}) is greater than maximum line width (size {maximum_line_width})."
                )

    def _wrap_text(self, input_text: str, maximum_line_width: int) -> str:
        """My wrapping solution.

        How it works:
        - Split the input text in spaces;
        - For each word, test if the length of the word + length of previous words <= maximum_line_width;
            - if length of the word + length of previous words <= maximum_line_width:
                - append the word in the line list and increment line_length, considering 1 whitespace;
            - else:
                - convert words in line list to a string and clears line list and line_length;
        - At the end, if there is still words in line list, append it to the output string;
        - Returns the text as string.

        Args:
            input_text (str): The text to be wrapped.
            maximum_line_width (int): Maximum line width.

        Returns:
            str: The wrapped text.
        """
        line = []
        line_length = 0
        output_text = []
        for word in input_text.split():
            if line_length + len(word) <= maximum_line_width:
                line.append(word)
                line_length += len(word) + 1
            else:
                output_text.append(" ".join(line))
                line.clear()
                line.append(word)
                line_length = len(word) + 1
        if len(line) > 0:
            output_text.append(" ".join(line))
        return "\n".join(output_text)

    def wrap_text(
        self,
        input_text: str,
        line_width: int,
        output_filename: str = "output-part1.txt",
        show_configuration: bool = False,
        use_python_wrap: bool = False,
    ) -> None:
        """Wraps text.

        Args:
            input_text (str, optional): The text to be wrapped.
            line_width (int, optional): Maximum line width.
            output_filename (str, optional): The filename in wich text will be saved. Defaults to "output-part1.txt".
            show_configuration (bool, optional): Print configuration in the screen. Defaults to False.
            use_python_wrap (bool, optional): Use Python built-in method to wrap. Defaults to False.
        """
        if show_configuration:
            self._show_configurations(input_text, line_width, output_filename)
        self._check_words_size(input_text, line_width)
        if use_python_wrap:
            output_text = textwrap.fill(text=input_text, width=line_width)
        else:
            if len(input_text) > line_width:
                output_text = self._wrap_text(input_text, line_width)
            else:
                output_text = input_text
        self._write_to_file(output_text, output_filename)

    def _python_justify_text(
        self,
        input_text: str = DEFAULT_INPUT_TEXT,
        line_width: int = DEFAULT_MAXIMUM_LINE_WIDTH,
        output_filename: str = "output-part2.txt",
    ):
        justified_text = textwrap.fill(text=input_text, width=line_width)
        for line in justified_text:
            print(line)
