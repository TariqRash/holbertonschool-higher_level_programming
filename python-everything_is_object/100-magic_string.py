#!/usr/bin/python3
def magic_string():
    magic_string.strings = getattr(magic_string, 'strings', [])
    magic_string.strings.append("BestSchool")
    return ", ".join(magic_string.strings)
