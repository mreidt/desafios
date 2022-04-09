import argparse
from typing import List

from beautiful_soup_service import BeautifulSoupService
from repositories import requests_repository, utils_repository


def crawler_reddit(subreddits: str) -> List[dict]:
    """Go and search the reddit threads.

    Args:
        subreddits (str): The subreddits to search.

    Returns:
        List[dict]: A list with the buzzer_threads.
    """
    list_of_subreddits = utils_repository.split_string(subreddits)
    buzz_threads_list = []
    for subbredit in list_of_subreddits:
        request_address = utils_repository.create_subreddit_url(subbredit)
        response = requests_repository.make_get_request(request_address)
        beautiful_soup_service = BeautifulSoupService(response)
        buzz_threads_list.extend(beautiful_soup_service.get_reddit_buzz_threads())
    return buzz_threads_list


def main(subreddits: str, filename: str = None) -> None:
    """Executes the scrapper operations.

    Args:
        subreddits (str): List of subreddits to search, separeted by ';'.
        filename (str, optional): The filename to save the results. Defaults to None.
    """
    buzz_threads_list = crawler_reddit(subreddits)
    if len(buzz_threads_list) > 0:
        utils_repository.cli_show_results(buzz_threads_list, filename)
    else:
        print("No buzzer threads found for those subreddits!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Idwall challenge")
    parser.add_argument(
        "subreddits",
        type=str,
        help="A list with subreddits to crawler, separeted by ';' (eg. 'askreddit;worldnews;cats').",
    )
    parser.add_argument(
        "-f",
        "--output_filename",
        nargs="?",
        default=None,
        help="The output filename to save threads results.",
    )
    args = parser.parse_args()

    main(args.subreddits, args.output_filename)
