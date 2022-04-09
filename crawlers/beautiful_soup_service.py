from typing import List

from bs4 import BeautifulSoup, element

from constants import BUZZ_THREAD_THRESHOLD


class BeautifulSoupService:
    def __init__(self, page: str) -> None:
        """Initializes the Beautifulsoup service.

        Args:
            page (str): The html page.
        """
        self.soup = BeautifulSoup(page, "html.parser")

    def _get_reddit_threads(self) -> List[element.Tag]:
        """Get the list of threads in reddit page.

        Returns:
            List[element.Tag]: The list of threads in a reddit page.
        """
        site_table = self.soup.find(class_="sitetable linklisting")
        return site_table.findAll("div", {"class": "thing"})

    def _get_reddit_thread_title(self, reddit_thread: element.Tag) -> str:
        """Get the title of a reddit thread.

        Args:
            reddit_thread (element.Tag): The reddit thread Tag.

        Returns:
            str: The title of the thread.
        """
        title = reddit_thread.find_all("a", {"class": "title"})
        return title[0].contents[0]

    def _get_reddit_thread_score(self, reddit_thread: element.Tag) -> int:
        """Get the score of a reddit thread.

        Args:
            reddit_thread (element.Tag): The reddit thread Tag.

        Returns:
            int: The score of the thread or None if not score found.
        """
        score = reddit_thread.find_all("div", {"class": "score unvoted"})
        if "•" in score[0]:
            return 0
        try:
            return int(score[0].get("title"))
        except (ValueError, TypeError):
            import pdb

            pdb.set_trace()
            print(
                f"Impossible to find score for thread {self._get_reddit_thread_title(reddit_thread)}"
            )
            return None

    def _get_reddit_thread_link(self, reddit_thread: element.Tag) -> str:
        """Get the link (permalink) of a reddit thread.

        Args:
            reddit_thread (element.Tag): The reddit thread Tag.

        Returns:
            str: The link (permalink) of the thread.
        """
        return reddit_thread.get("data-permalink")

    def _get_reddit_thread_rank(self, reddit_thread: element.Tag) -> str:
        """Get the rank of a reddit thread

        Args:
            reddit_thread (element.Tag): The reddit thread Tag.

        Returns:
            str: The rank of the thread.
        """
        rank = reddit_thread.find_all("span", {"class": "rank"})
        return rank[0].contents[0]

    def _get_reddit_thread_subreddit(self, reddit_thread: element.Tag) -> str:
        """Get the subreddit of a reddit thread.

        Args:
            reddit_thread (element.Tag): The reddit thread Tag.

        Returns:
            str: The subreddit of the thread.
        """
        return reddit_thread.get("data-subreddit")

    def get_reddit_buzz_threads(self) -> List[dict]:
        """Get the list of buzz threads (score greater than threshold - default is 5000).

        Returns:
            List[dict]: A list with all threads that satisfies the requirement of a buzz thread.
        """
        reddit_buzz_threads_list = []
        reddit_threads = self._get_reddit_threads()
        for reddit_thread in reddit_threads:
            reddit_thread_score = self._get_reddit_thread_score(reddit_thread)
            if reddit_thread_score and reddit_thread_score >= BUZZ_THREAD_THRESHOLD:
                reddit_thread_title = self._get_reddit_thread_title(reddit_thread)
                reddit_link_to_thread = (
                    reddit_link_to_comments
                ) = self._get_reddit_thread_link(reddit_thread)
                reddit_thread_subreddit = self._get_reddit_thread_subreddit(
                    reddit_thread
                )
                reddit_thread_rank = self._get_reddit_thread_rank(reddit_thread)
                reddit_buzz_thread = {
                    "rank": reddit_thread_rank,
                    "score": reddit_thread_score,
                    "subreddit": reddit_thread_subreddit,
                    "title": reddit_thread_title,
                    "comments_link": reddit_link_to_comments,
                    "thread_link": reddit_link_to_thread,
                }
                reddit_buzz_threads_list.append(reddit_buzz_thread)
        return reddit_buzz_threads_list
