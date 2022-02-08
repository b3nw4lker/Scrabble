from importlib_metadata import distribution
from scrabbleproj.constants import DISTRIBUTION, POINTS
from scrabbleproj.tile import Tile


class TileBag:
    def __init__(self):
        self.tile_bag_values = DISTRIBUTION
        self.tile_bag_items = self._create_list_of_tile_bag()

    def _create_list_of_tile_bag(self):
        tile_bag = []

        for tile_name, distribution in self.tile_bag_values.items():
            qty = distribution

            for qty_of_tile in range(0, qty):
                tile_bag.append(Tile(tile_name))

        return tile_bag

    def get_tile_bag_count(self):
        return len(self.tile_bag_items)
