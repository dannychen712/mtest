class BasketballReference:
    """
    Page object representing the basketballreference.com all star page.
    """

    def __init__(self, browser):
        """
        Pass in browser fixture from conftest.py
        """
        self.browser = browser

    def player_names(self):
        """
        All player names have the custom attribute

        Returns Array of player names
        """
        names_objects = self.browser.find_elements_by_css_selector(
            "[data-stat=player]")

        # using list comprehension extract all text from the elements
        # also remove "player" text from table

        names = [name.text for name in names_objects if not name.text == "Player"]
        cleaned_names = list(filter(None, names))
        return cleaned_names

