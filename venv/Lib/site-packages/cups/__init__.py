import random
import string
from typing import List


class CupsGenerator:

    def generate(self) -> string:
        ree_id = self._generate_ree_id()
        dist_id = self._generate_dist_id()
        print(ree_id)
        print(dist_id)
        control = int(ree_id + dist_id) % 529
        division = control / 23
        mod = control % 23
        control_letter = self._get_control_numbers_by(int(division))
        control_2_letter = self._get_control_numbers_by(mod)

        return f"ES{ree_id}{dist_id}{control_letter}{control_2_letter}"

    def _generate_ree_id(self) -> string:
        id = random.randint(0, 9999)
        return f'{id:04}'

    def _generate_dist_id(self) -> string:
        id = random.randint(0, 999999999999)
        return f'{id:12}'

    def _get_control_numbers_by(self, number) -> string:
        return self._get_control_numbers()[number]

    def _get_control_numbers(self) -> List:
        return [
            'T',
            'R',
            'W',
            'A',
            'G',
            'M',
            'Y',
            'F',
            'P',
            'D',
            'X',
            'B',
            'N',
            'J',
            'Z',
            'S',
            'Q',
            'V',
            'H',
            'L',
            'C',
            'K',
            'E',
        ]

