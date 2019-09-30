from test_framework import generic_test


def look_and_say(n):
    # TODO - you fill in here.
    if n < 1:
        return ""
    prev_str = "1"
    new_str = ""
    look_say_table = {}
    look_say_index = 1
    while look_say_index < n:
        i = 0
        j = 0
        while j < len(prev_str):
            while j < len(prev_str) and prev_str[j] == prev_str[i]:
                j += 1
            look = prev_str[i:j]
            if look in look_say_table:
                new_str += look_say_table[look]
            else:
                say = str(len(look)) + prev_str[i]
                look_say_table[look] = say
                new_str += say
            i = j
        prev_str = new_str
        new_str = ""
        look_say_index += 1
    return prev_str


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
