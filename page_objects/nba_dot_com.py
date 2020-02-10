

class NBADotCom:
    """
    Page object representing the nba.com all star page.
    """

    def __init__(self, browser):
        """
        Pass in browser fixture from conftest.py
        """
        self.browser = browser

    def player_names(self):
        """
        All player name p tags have "nba-player-index__name" as the class. This
        may change on the 30th when the reserves are announced.

        Returns Array of player names
        """
        names_objects = self.browser.find_elements_by_class_name(
            "nba-player-index__name")

        # have to replace newline with space, uses list comprehension
        list_of_names = [name.text.replace("\n", " ") for name in names_objects]

        return list_of_names[2:len(list_of_names) - 2]