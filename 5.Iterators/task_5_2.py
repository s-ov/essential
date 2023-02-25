# Взяв за основу код примера example_5.py, расширьте функциональность класса MyList, добавив методы для очистки списка,
# добавления элемента в произвольное место списка, удаления элемента из конца и произвольного места списка.
class MyList(object):
    """Класс списка"""
    class _ListNode(object):
        """Внутренний класс элемента списка"""
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next_=None):
            self.value = value
            self.prev = prev
            self.next = next_

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)
#######

    def delete_element(self, element, index):
        if index not in range(len(self)):
            raise TypeError('Invalid index.')
        object.__delattr__(self, element, index)

    def empty_list(self):
        object.clear()

    def insert_(self, element, index):
        if index == self._length:
            self.append(element)
        node = self._head
        if index == 0:
            self._head.prev = node
            node.next = self._head
        elif 1 <= index < self._length:
            tmp = self._head
            for _ in range(index):
                tmp = tmp.next

            tmp_prev = tmp.prev
            tmp_prev.next = node
            node.prev = tmp_prev
            node.next = tmp
            tmp.prev = node
            self._length += 1
        else:
            raise IndexError('List index out of range')



    def pop(self):
        del self._tail


def main():
    my_list = MyList([1, 2, 5])
    print(len(my_list))
    print(my_list)
    print()
    for element in my_list:
        print(element)
    print()


if __name__ == '__main__':
    main()
    my_list = MyList([1, 2, 5, 12])
    # my_list.delete_element([1])
    # my_list.empty_list()
    # print(dir(my_list))
    my_list.insert_(0, 0)
    print(my_list)
