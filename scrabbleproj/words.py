from assets.allwords import worddict
from scrabbleproj.constants import POINTS
from scrabbleproj.tileboosters import TileBoost


class Words:

    def __init__(self):
        self.word_to_calc = ''
        self.points_per_letter = POINTS
        self.tileboost = TileBoost()

    def check_if_word(self, board, last_tile_placed):
        horizontal_word = []
        vertical_word = []
        print(f"Last Tile Placed {board.board[last_tile_placed[0]][last_tile_placed[1]].letter}")

        # FIXME: If we place the horizontal tile last we need to use _create_row_representation to generate row

        row_representation = self._create_row_representation(board, last_tile_placed)

        # Check if words are right
        for index, tile in enumerate(row_representation, start=last_tile_placed[0]):
            if row_representation[index].letter:
                horizontal_word.append(row_representation[index])
                vertical_word = self._vertical_word_check(board, index, last_tile_placed, vertical_word)
                continue
            break

        # Check if words are left
        negative_count = 1
        for index, tile in enumerate(row_representation, start=last_tile_placed[0]):
            adjusted_index = index - negative_count

            if row_representation[adjusted_index].letter:
                horizontal_word.insert(0, row_representation[adjusted_index])
                negative_count += 2
                vertical_word = self._vertical_word_check(board, index, last_tile_placed, vertical_word)
                continue
            break

        if len(horizontal_word) == 1 and len(vertical_word) > 1:
            horizontal_word.clear()
        elif len(vertical_word) == 1 and len(horizontal_word) > 1:
            vertical_word.clear()

        print(f"Horizontal Words: {[word.letter for word in horizontal_word]}")
        print(f"Vertical Words: {[word.letter for word in vertical_word]}")

        word_exists = self.does_word_exist('word')

        if word_exists:
            self.score_word()
        else:
            pass

    @staticmethod
    def _vertical_word_check(board, index, last_tile_placed, vertical_word):
        cell_above = board.board[index][last_tile_placed[1] - 1]
        cell_below = board.board[index][last_tile_placed[1] + 1]

        if cell_above.letter:
            for cell in board.board[index]:
                if cell.letter:
                    vertical_word.append(cell)

        if cell_below.letter:
            for cell in board.board[index]:
                if cell.letter:
                    vertical_word.append(cell)

        return vertical_word

    @staticmethod
    def _create_row_representation(board, last_tile_placed):
        board_representation = []
        for row in board.board:
            new_row = []
            for letter in row:
                new_row.append(letter.letter)

            board_representation.append(new_row)
        # Create row based on start location (the list is all flipped)

        row_representation = []
        for cell in range(15):
            row_representation.append(board.board[cell][last_tile_placed[1]])

        return row_representation

    #     return message showing which words are fake.

    # To return tiles to deck - we store all tiles placed in turn in a list, if turn can't be scored we run function to
    # move all tiles form list back to deck

    def score_word(self, word):
        pass

    def does_word_exist(self, word):
        # If word does not exist return word / words that are fake
        pass

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



