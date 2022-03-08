from assets.allwords import worddict
from scrabbleproj.constants import POINTS
from scrabbleproj.tileboosters import TileBoost


class Words:

    def __init__(self):
        self.word_to_calc = ''
        self.points_per_letter = POINTS
        self.tileboost = TileBoost()

    def check_if_word(self, board, last_tile_placed):
        print("In word check")
        print(board)
        print(last_tile_placed)
        start_location = board.board[last_tile_placed[0]][last_tile_placed[1]]

    def calc_score_and_add(self):  # this should work
        final_word_points = 0
        for letter in self.word_to_calc:
            points_achieved_for_letter = self.points_per_letter.get(str(letter))
            final_word_points += points_achieved_for_letter

        if self.tileboost.double_letter:
            pass

        if self.tileboost.double_word:
            final_word_points *= 2

        if self.tileboost.triple_letter:
            pass

        if self.tileboost.triple_word:
            final_word_points *= 3

        self.game_man.current_player.score += final_word_points


    def word_lookup(self):
        pass
    # store the location the player has placed their first tile (if player picks up tile and moves it we need to reset to new locations
    # on turn end from location the first tile was placed during turn, iterate left on board, right on board to create a word (break when there no tile)
    # iterate vertical on board from each horizontal tile
    #
    # word is SIALN
    #
    # A is placed first
    #
    # word = ["A"]
    #
    # horizontal
    # go left on board:
    #     check_if_vertical()
    #     prepend(I)
    #     if check_if_vertical == true set a flag with cel location
    #     word = ["I","A"]
    #     prepend(S)
    #     word = ["S","I","A"]
    #     break (no more tiles)
    #
    # go right on board:
    #     check_if_vertical()
    #     append(L)
    #     word = ["S","I","A", "L"]
    #     append(N)
    #     word = ["S","I","A", "L", "N"]
    #     break (no more tiles)
    #
    #
    # vertical
    # if vertical cell location:
    #     go up and go down as per above to form word



