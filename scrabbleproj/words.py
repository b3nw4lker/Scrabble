from assets.allwords import worddict
from scrabbleproj.constants import POINTS
from scrabbleproj.tileboosters import TileBoost


class Words:

    def __init__(self):
        self.word_to_calc = ''
        self.points_per_letter = POINTS
        self.tileboost = TileBoost()

    def check_if_word(self, word):
        x = str(word)
        lowercaseword = x.lower()
        if lowercaseword in worddict:
            print('thats a word')
            self.word_to_calc = x
        else:
            print('thats not a word')

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
