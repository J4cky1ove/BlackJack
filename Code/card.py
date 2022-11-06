class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert rank in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        assert suit in ["hearts", "spades", "clubs", "diamonds"]
        assert isinstance(visible, bool)
        self.rank = rank
        self.suit = suit
        self.visible = visible

    def __lt__(self, other_card):
        temp = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        shape = ["clubs", "diamonds", "hearts", "spades"]
        for i in range(len(temp)):
            if temp[i] == self.rank:
                temp1 = i 
            if temp[i] == other_card.rank:
                temp2 = i 
        if temp1 < temp2:
            return True 
        elif temp2 < temp1:
            return False
        else:
            for j in range(len(shape)):
                if shape[j] == self.suit:
                    shape1 = j
                if shape[j] == other_card.suit:
                    shape2 = j
            return shape1 < shape2
                
        

    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|
        """
        if self.suit == "hearts":
            shape = "♥"
        elif self.suit ==  "spades":
            shape = "♠"
        elif self.suit == "clubs":
            shape = "♣"
        else:
            shape = "♦"
        if self.visible:
            rank = str(self.rank)
        else:
            rank = "?"
            shape = "?"
        result = "____" + '\n' + '|' + rank + "  |" + '\n' + '|' + " " + shape + " |" + '\n' +\
    '|__' + rank + '|'
        return result

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.
        """
        if self.visible:
            rank = str(self.rank)
            suit = self.suit
        else:
            rank = "?"
            suit = "?"
        return "(" + rank + ", " + suit + ")"

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
