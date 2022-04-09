from typing import List


class IdwallStringsRepository:
    def _write_to_file(self, input_text: List[str], output_filename: str) -> None:
        """Write text to file.

        Args:
            input_text (List[str]): The text to be write.
            output_filename (str): The file to be created.
        """
        with open(output_filename, "w") as out_file:
            out_file.write("\n".join(input_text))

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

    def _manually_wrap_text(
        self, input_text: str, maximum_line_width: int
    ) -> List[str]:
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
            List[str]: The list with wrapped text.
        """
        if len(input_text) <= maximum_line_width:
            return input_text.split()
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
        return output_text

    def _append_whitespaces_in_list(
        self,
        list_of_strings: List[str],
        needed_whitespaces: int,
        range_to_append_whitespaces: int = None,
    ) -> List[str]:
        """Append the whitespaces in a list of strings.

        Transform a list of strings, adding a number of whitespaces in each string.
        Example:
        - input list : ['idwall', 'is', 'a', 'great', 'place', 'to', 'work.']
        - output list: ['idwall ', 'is ', 'a ', 'great ', 'place ', 'to ', ' work.']

        Args:
            list_of_strings (List[str]): The list of strings.
            needed_whitespaces (int): Total number of required whitespaces.
            range_to_append_whitespaces (int, optional): Number of strings in the list that should receive an
            whitespace. Defaults to None.

        Returns:
            List[str]: The list with the strings with the required number of whitespaces.
        """
        if not range_to_append_whitespaces:
            range_to_append_whitespaces = len(list_of_strings)
        for word_index in range(range_to_append_whitespaces):
            word = list_of_strings[word_index]
            if word_index == len(list_of_strings) - 1:
                word = word.rjust(len(word) + needed_whitespaces)
            else:
                word = word.ljust(len(word) + needed_whitespaces)
            list_of_strings[word_index] = word
        return list_of_strings

    def _justify_list_of_strings(
        self, list_of_strings: List[str], needed_whitespaces: int
    ) -> List[str]:
        """Justify the text in a list of strings.

        Args:
            list_of_strings (List[str]): The list of strings to be justified.
            needed_whitespaces (int): Total number of whitespaces to be added in each string.

        Returns:
            List[str]: The justified list of strings.
        """
        number_of_strings_in_list = len(list_of_strings)
        if needed_whitespaces > number_of_strings_in_list - 1:
            needed_whitespaces = int(
                needed_whitespaces / (number_of_strings_in_list - 1)
            )
            justified_line = self._append_whitespaces_in_list(
                list_of_strings, needed_whitespaces
            )
        elif needed_whitespaces > 0:
            justified_line = self._append_whitespaces_in_list(
                list_of_strings, 1, needed_whitespaces
            )
        else:
            justified_line = list_of_strings
        return justified_line

    def _calculate_needed_whitespaces_to_justify_text(
        self, maximum_text_length: int, list_of_strings: List[str]
    ) -> int:
        """Calculate the number of whitespaces required to justify a text in a list of strings.

        Args:
            maximum_text_length (int): The maximum length of the text.
            list_of_strings (List[str]): The list with the strings to be justified.

        Returns:
            int: The total whitespaces needed to justify the text in the list of strings.
        """
        whitespaces_in_text = len(list_of_strings) - 1
        text_size = sum([len(word) for word in list_of_strings]) + whitespaces_in_text
        needed_whitespaces = maximum_text_length - text_size
        return needed_whitespaces

    def _justify_text_in_list_of_lines(
        self, maximum_line_width: int, lines: List[str]
    ) -> List[str]:
        """Justify a text in a list of lines.

        Args:
            maximum_line_width (int): The maximum line width.
            lines (List[str]): Lines of the text.

        Returns:
            List[str]: The justified list of lines.
        """
        output_text = []
        for line in lines:
            needed_whitespaces = self._calculate_needed_whitespaces_to_justify_text(
                maximum_line_width, line
            )
            justified_line = self._justify_list_of_strings(line, needed_whitespaces)
            output_text.append(" ".join(justified_line))
        return output_text


idwall_strings_repository = IdwallStringsRepository()
