class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    """    
        
    def modified_overhand(cards, num):
        if num == 0:
            return cards
        else:
            if len(cards)%2 != 0 and num%2 == 0:
                middle = len(cards)//2
                cishu = (num - 2)/2
                def odd_even(cards, num):
                    if num == 0:
                        return []
                    else:
                        first = cards[int(middle - cishu - 1)]
                        cards.remove(first)
                        return [first] + odd_even(cards, num - 1)
                cards = odd_even(cards, num) + cards
            elif len(cards)%2 == 0 and num%2 != 0:
                middle = len(cards)/2 - 1 
                cishu = (num - 1)/2  
                def even_odd(cards, num):
                    if num == 0:
                        return []
                    else:
                        first = cards[int(middle - cishu)]
                        cards.remove(first)
                        return [first] + even_odd(cards, num - 1)
                cards = even_odd(cards, num) + cards
            elif len(cards)%2 == 0 and num%2 == 0:
                middle = len(cards)/2 
                cishu = (num - 2)/2
                def even_even(cards, num):
                    if num == 0:
                        return []
                    else:
                        first = cards[int(middle - cishu - 1)]
                        cards.remove(first)
                        return [first] + even_even(cards, num - 1)
                cards = even_even(cards, num) + cards
            else:
                middle = len(cards)//2 
                cishu = (num - 1)/2
                def odd_odd(cards, num):
                    if num == 0:
                        return []
                    else:
                        first = cards[int(middle - cishu)]
                        cards.remove(first)
                        return [first] + odd_odd(cards, num - 1)
                cards = odd_odd(cards, num) + cards
            cards = Shuffle.modified_overhand(cards, num - 1)     
            return cards
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        if len(cards) == 0:
            return []
        elif len(cards) % 2 == 0:
            result = Shuffle.mongean(cards[:-1])
            result.insert(0,cards[-1])
            return result
        else:
            result = Shuffle.mongean(cards[:-1])
            result.append(cards[-1])
        return result
    
