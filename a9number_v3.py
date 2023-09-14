import cProfile
import re
from collections import Counter
from collections import OrderedDict


"""In order to run the tests simply run

python -m pytest a9number_v3.py

In order to see the profiling, you need to add the option -s
"""


def count_occurrences_in_text(word, text):
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """

    # TODO: your code goes here, but it's OK to add new functions or import modules if needed
    # Convert both word and text to lowercase for case-insensitive search
    od = OrderedDict(((word, 0) for word in word_list))

    # Convert the text and words to lowercase for case-insensitive search
    text = text.lower()
    word_list = [word.lower() for word in word_list]

    # Count occurrences of each word in the text
    for word in word_list:
        od[word] = text.count(word)

    # Print the count of each word
    for word, count in od.items():
        print(f"{word}: {count}")

    return od


def test_count_occurrences_in_text():
    text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""
    # test with a little text.
    assert 3 == count_occurrences_in_text("Georges", text)
    assert 3 == count_occurrences_in_text("GEORGES", text)
    assert 3 == count_occurrences_in_text("georges", text)
    assert 0 == count_occurrences_in_text("george", text)
    assert 3 == count_occurrences_in_text("python", text)
    assert 3 == count_occurrences_in_text("PYTHON", text)
    assert 2 == count_occurrences_in_text("I", text)
    assert 0 == count_occurrences_in_text("n", text)
    assert 1 == count_occurrences_in_text("true", text)
    # regard ' as text:
    assert 0 == count_occurrences_in_text("maley", "John O'maley is my friend")

    # Test it but with a BIG length file.
    text = (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )
    text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
    text += (
        """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog."""
        * 500
    )

    assert 3 == count_occurrences_in_text("Georges", text)
    assert 3 == count_occurrences_in_text("GEORGES", text)
    assert 3 == count_occurrences_in_text("georges", text)
    assert 0 == count_occurrences_in_text("george", text)
    assert 3 == count_occurrences_in_text("python", text)
    assert 3 == count_occurrences_in_text("PYTHON", text)
    assert 2 == count_occurrences_in_text("I", text)
    assert 0 == count_occurrences_in_text("n", text)
    assert 1 == count_occurrences_in_text("true", text)
    # assert 1 == count_occurrences_in_text(
    #     "'reflexion mirror'",
    #     "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida",
    # )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror", 'Reflexion Mirror" in Sopchoppy, Florida'
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida",
    )
    assert 1 == count_occurrences_in_text(
        "legitimate",
        "who is approved by OILS is completely legitimate: their employees are of legal working age",
    )
    assert 0 == count_occurrences_in_text(
        "legitimate their",
        "who is approved by OILS is completely legitimate: their employees are of legal working age",
    )
    assert 1 == count_occurrences_in_text(
        "get back to me",
        "I hope you will consider this proposal, and get back to me as soon as possible",
    )
    assert 1 == count_occurrences_in_text(
        "skin-care",
        "enable Delavigne and its subsidiaries to create a skin-care monopoly",
    )
    assert 1 == count_occurrences_in_text(
        "skin-care monopoly",
        "enable Delavigne and its subsidiaries to create a skin-care monopoly",
    )
    assert 0 == count_occurrences_in_text(
        "skin-care monopoly in the US",
        "enable Delavigne and its subsidiaries to create a skin-care monopoly",
    )
    assert 1 == count_occurrences_in_text(
        "get back to me", "When you know:get back to me"
    )
    assert 1 == count_occurrences_in_text(
        "don't be left",
        """emergency alarm warning.
Don't be left unprotected. Order your SSSS3000 today!""",
    )
    assert 1 == count_occurrences_in_text(
        "don",
        """emergency alarm warning.
Don't be left unprotected. Order your don SSSS3000 today!""",
    )
    assert 1 == count_occurrences_in_text(
        "take that as a 'yes'", "Do I have to take that as a 'yes'?"
    )
    assert 1 == count_occurrences_in_text(
        "don't take that as a 'yes'", "I don't take that as a 'yes'?"
    )
    assert 1 == count_occurrences_in_text(
        "take that as a 'yes'", "I don't take that as a 'yes'?"
    )
    assert 1 == count_occurrences_in_text("don't", "I don't take that as a 'yes'?")
    assert 1 == count_occurrences_in_text(
        "attaching my c.v. to this e-mail", "I am attaching my c.v. to this e-mail."
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist Specialist",
        "'''Linguist Specialist Found Dead on Laboratory Floor'''",
    )
    assert 1 == count_occurrences_in_text(
        "Laboratory Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "''Linguist Specialist Found Dead on Laboratory Floor''"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "__Linguist Specialist Found Dead on Laboratory Floor__"
    )
    assert 1 == count_occurrences_in_text(
        "Floor", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "''Linguist Specialist Found Dead on Laboratory Floor''"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "__Linguist Specialist Found Dead on Laboratory Floor__"
    )
    assert 1 == count_occurrences_in_text(
        "Linguist", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''"
    )


SAMPLE_TEXT_FOR_BENCH = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
Bob Carter
"""


def doit():
    """
    Run count_occurrences_in_text on a few examples
    """
    i = 0
    words = [
        "word",
        "sugar",
        "help",
        "heavily",
        "witfull",
        "dog",
        "almost",
        "insulin",
        "attaching",
        "asma",
        "neither",
        "won't",
        "green",
        "parabole",
        "t",  # Add "t" to the list
    ]
    for word in words:
        count = count_occurrences_in_text(word, SAMPLE_TEXT_FOR_BENCH)
        print(f"{word}: {count}")
        i += count
    return i


def test_profile():
    with cProfile.Profile() as pr:
        assert doit() == 9
        pr.print_stats()
