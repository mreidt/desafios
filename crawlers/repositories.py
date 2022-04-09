from datetime import datetime
from time import sleep
from typing import List

import requests

from constants import MAXIMUM_TRIES, REDDIT_BASE_ADDRESS, START_WAITING_TIME


class UtilsRepository:
    def split_string(self, string_to_separate: str, separator: str = ";") -> List[str]:
        """Split string according to a separator.

        Args:
            string_to_separate (str): The string to be splitted.
            separator (str, optional): The separator. Defaults to ";".

        Returns:
            List[str]: List with splitted strings.
        """
        return string_to_separate.split(separator)

    def _print_thread_cli(self, reddit_thread: dict) -> None:
        """Print the crawler results to terminal.

        Args:
            reddit_thread (dict): The reddit thread informations.
        """
        print(f"{reddit_thread.get('rank')} - {reddit_thread.get('title')}")
        print(f"{'-':>5} Score.........: {reddit_thread.get('score')}")
        print(f"{'-':>5} Subreddit.....: {reddit_thread.get('subreddit')}")
        print(f"{'-':>5} Comments link.: {reddit_thread.get('comments_link')}")
        print(f"{'-':>5} Thread link...: {reddit_thread.get('thread_link')}")

    def _save_thread_to_file(self, reddit_thread: dict, filename: str):
        """Write the crawler results to a file.

        Args:
            reddit_thread (dict): The reddit thread information.
            filename (str): The filename to save the informations.
        """
        with open(filename, "a") as file:
            file.write(f"{'-'*70}\n")
            file.write(f"{reddit_thread.get('rank')} - {reddit_thread.get('title')}\n")
            file.write(f"{'-':>5} Score.........: {reddit_thread.get('score')}\n")
            file.write(f"{'-':>5} Subreddit.....: {reddit_thread.get('subreddit')}\n")
            file.write(f"{'-':>5} Comments link.: {reddit_thread.get('comments_link')}\n")
            file.write(f"{'-':>5} Thread link...: {reddit_thread.get('thread_link')}\n")

    def cli_show_results(
        self,
        buzz_thread_list: List[dict],
        filename: str = None,
    ) -> None:
        """Show the results of the crawler.

        Args:
            buzz_thread_list (List[dict]): The list with the reddit threads.
            filename (str, optional): The filename to save the informations.. Defaults to None.
        """
        for buzz_thread in buzz_thread_list:
            self._print_thread_cli(buzz_thread)
            if filename:
                self._save_thread_to_file(buzz_thread, filename)

    def create_subreddit_url(self, subreddit: str) -> str:
        """Create the subreddit URL.

        Args:
            subreddit (str): The subreddit address.

        Returns:
            str: The subreddit complete URL.
        """
        return f"{REDDIT_BASE_ADDRESS}/r/{subreddit}"


class RequestsRepository:
    def __init__(self) -> None:
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/100.0.4896.79 Safari/537.36"
        }

    def _handle_status_code_429(self, requests_tried: int) -> None:
        """Handle TOO MANY REQUESTS error in requests.

        Args:
            requests_tried (int): Number of previous tried requests.
        """
        print(f"Error in reddit response. Details: status_code ({429}).")
        wait_time = START_WAITING_TIME * requests_tried
        print(f"{datetime.now()} - Waiting {wait_time} seconds until next request.")
        sleep(wait_time)

    def make_get_request(self, url: str, maximum_tries: int = MAXIMUM_TRIES) -> str:
        """Make a get request and handle the results.

        Args:
            url (str): The URL to do the GET request.
            maximum_tries (int, optional): Maximum number of request tries. Defaults to MAXIMUM_TRIES.

        Returns:
            str: The request response text.
        """
        requests_tried = 1
        status_code = None
        while requests_tried < maximum_tries and status_code != 200:
            print(f"Trying to make GET request to {url}.")
            response = requests.get(url, headers=self.headers)
            status_code = response.status_code
            if status_code == 429:
                self._handle_status_code_429(requests_tried)
            elif status_code != 200:
                print(
                    f"Error {response.status_code} during GET request to {url}. Exiting."
                )
                exit(2)
            requests_tried += 1
        if status_code != 200:
            print(
                "It was not possible to make GET request to {reddit_address}. Exiting."
            )
            exit(3)
        return response.text


utils_repository = UtilsRepository()
requests_repository = RequestsRepository()
