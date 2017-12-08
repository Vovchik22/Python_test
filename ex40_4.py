class poem (object):
    """docstring for poem ."""
    def __init__(self, words):
        self.words = words

    def poet (self):
        for line in self.words:
            print(line)

poem_1 = poem(['aaaa', 'bbbbbb', 'ccccccc'])
poem_2 = poem(['11111', '222222', '333333'])
poem_3 = poem(['ababbababa', 'bcbcbcbbcb', 'cdcdcdcdccd'])

poem_1.poet()
poem_2.poet()
poem_3.poet()
