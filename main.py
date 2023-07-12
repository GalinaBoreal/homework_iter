import types


class FlatIterator:

    def __init__(self, list_of_lists):
        self.list = list_of_lists
        self.counter = -1
        self.list_len = len(self.list)

    def __iter__(self):
        self.counter += 1
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor == len(self.list[self.counter]):
            iter(self)
        if self.counter == self.list_len:
            raise StopIteration
        self.cursor += 1
        return self.list[self.counter][self.cursor - 1]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):
    for first_level in list_of_lists:
        for second_level in first_level:
            yield second_level


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)



if __name__ == '__main__':
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # print(FlatIterator(list_of_lists))
    # i_list = [item for item in FlatIterator(list_of_lists)]
    # print(i_list)

    test_1()

    # print(flat_generator(list_of_lists))
    # g_list = [item for item in flat_generator(list_of_lists)]
    # print(g_list)

    test_2()
