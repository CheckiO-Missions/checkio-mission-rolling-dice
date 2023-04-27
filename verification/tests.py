"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["SN"],
            "answer": 1,
        },
        {
            "input": [""],
            "answer": 1,
        },
        {
            "input": ["EESWN"],
            "answer": 6,
        },
        {
            "input": ["NWSNWEESNW"],
            "answer": 3,
        },
        {
            "input": ["NNNSESNESWNENSWNNWSWNSSNWWSWNW"],
            "answer": 5,
        },
    ],
    "Extra": [
        {
            "input": ["SSSS"],
            "answer": 1,
        },
        {
            "input": ["SSS"],
            "answer": 2,
        },
        {
            "input": ["WENWNNSSSE"],
            "answer": 2,
        },
        {
            "input": ["SSENNWWEES"],
            "answer": 5,
        },
        {
            "input": ["NNNSESNESWNENSWNNWSWNSSNWWSWNW"],
            "answer": 5,
        },
        {
            "input": ["WSWNENSNSEWESEESNWEW"],
            "answer": 2,
        },
        {
            "input": ["ESWWNNNNSEENWSENNWNW"],
            "answer": 2,
        },
        {
            "input": ["SENWNSENSESSSEWNENWSNSENWNNWNNNWWESESESNWE"],
            "answer": 2,
        },
        {
            "input": ["SNNNWSSSESWNWSWSENNWNNSNWNENWEWSESNENWNNW"],
            "answer": 6,
        },
        {
            "input": ["ESWNNNWWSNSNNESWSWEWENNNSESENNWNENWSWNSENNWSW"],
            "answer": 2,
        },
    ]
}
