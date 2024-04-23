from typing import List

import numpy as np


class GlobalFilters(object):
    def __init__(self) -> None:
        self.pose_filter = [11, 12, 13, 14, 15, 16]
        self.face_filter = [
            0,
            4,
            8,
            10,
            13,
            14,
            17,
            33,
            37,
            46,
            52,
            54,
            55,
            61,
            127,
            133,
            145,
            150,
            152,
            159,
            263,
            267,
            276,
            282,
            284,
            285,
            291,
            356,
            362,
            374,
            379,
            386,
        ]
        self.face_filter_big = [
            0,
            4,
            7,
            8,
            10,
            13,
            14,
            17,
            21,
            33,
            37,
            39,
            40,
            46,
            52,
            53,
            54,
            55,
            58,
            61,
            63,
            65,
            66,
            67,
            70,
            78,
            80,
            81,
            82,
            84,
            87,
            88,
            91,
            93,
            95,
            103,
            105,
            107,
            109,
            127,
            132,
            133,
            136,
            144,
            145,
            146,
            148,
            149,
            150,
            152,
            153,
            154,
            155,
            157,
            158,
            159,
            160,
            161,
            162,
            163,
            172,
            173,
            176,
            178,
            181,
            185,
            191,
            234,
            246,
            249,
            251,
            263,
            267,
            269,
            270,
            276,
            282,
            283,
            284,
            285,
            288,
            291,
            293,
            295,
            296,
            297,
            300,
            308,
            310,
            311,
            312,
            314,
            317,
            318,
            321,
            323,
            324,
            332,
            334,
            336,
            338,
            356,
            361,
            362,
            365,
            373,
            374,
            375,
            377,
            378,
            379,
            380,
            381,
            382,
            384,
            385,
            386,
            387,
            388,
            389,
            390,
            397,
            398,
            400,
            402,
            405,
            409,
            415,
            454,
            466,
        ]

    @staticmethod
    def filter(features: np.ndarray, filter_list: List[int]) -> np.ndarray:
        return features[filter_list]


class FilteredLabels(object):
    @staticmethod
    def get_labels():
        return [
            "give",
            "turn",
            "way",
            "improve",
            "hill",
            "take",
            "my",
            "middle",
            "rest",
            "suggest",
            "go",
            "no",
            "excuse",
            "first",
            "send",
            "end",
            "miss",
            "there",
            "buy",
            "suppose",
            "yes",
            "develop",
            "chance",
            "prepare",
            "answer",
            "avoid",
            "grateful",
            "none",
            "offer",
            "thing",
            "wow",
            "break",
            "hour",
            "invest",
            "or",
            "start",
            "organize",
            "bad",
            "motivate",
            "ride",
            "weekend",
            "welcome",
            "bother",
            "east",
            "should",
            "visualize",
            "skip",
            "long",
            "again",
            "we",
            "you",
            "stretch",
            "time",
            "make",
            "bribe",
            "email",
            "inspire",
            "what",
            "learn",
            "catch",
            "to",
            "street",
            "identify",
            "earn",
            "minute",
            "guide",
            "freeway",
            "appreciate",
            "only",
            "empty",
            "kiss",
            "around",
            "inform",
            "mad",
            "through",
            "dirt",
            "in",
            "stupid",
            "arrive",
            "forgive",
            "determine",
            "borrow",
            "zero",
            "shame",
            "while",
            "say",
            "establish",
            "once",
            "postpone",
            "disgusted",
            "discuss",
            "on",
            "near",
            "save",
            "ask",
            "but",
            "rush",
            "sell",
            "nothing",
            "aim",
            "after",
            "lend",
            "clueless",
            "gamble",
            "order",
            "all",
            "manage",
            "intersection",
            "reason",
            "wander",
            "place",
            "south",
            "waste",
            "feel",
            "within",
            "dumb",
            "then",
            "cost",
            "get",
            "not",
            "address",
            "and",
            "decide",
            "guess",
            "pocket",
            "explain",
            "provide",
            "why",
            "up",
            "road",
            "highway",
            "push",
            "beside",
            "sit",
            "bridge",
            "attract",
            "dollar",
            "pray",
            "solve",
            "ahead",
            "think",
            "wish",
            "wait",
            "any",
            "bus",
            "aid",
            "when",
            "few",
            "next",
            "kill",
            "silly",
            "teach",
            "bicycle",
            "beginning",
            "wrong",
            "one",
            "pay",
            "understand",
            "quit",
            "admit",
            "can",
            "car",
            "mean",
            "north",
            "walk",
            "shout",
            "bring",
            "benefit",
            "right",
            "last",
            "willing",
            "night",
            "terrible",
            "assist",
            "fix",
            "will",
            "see",
            "enough",
            "before",
            "sad",
            "half",
            "support",
            "know",
            "ready",
            "since",
            "hello",
            "this",
            "awful",
            "lose",
            "ignore",
            "another",
            "pull",
            "now",
            "find",
            "because",
            "if",
            "behind",
            "bye",
            "doubt",
            "recover",
            "bless",
            "over",
            "finance",
            "geography",
            "invite",
            "wonder",
            "either",
            "out",
            "refuse",
            "until",
            "later",
            "upset",
            "wallet",
            "warn",
            "from",
            "work",
            "please",
            "try",
            "build",
            "t",
            "forget",
            "pity",
            "each",
            "name",
            "penny",
            "without",
            "educate",
            "maybe",
            "somewhere",
            "encourage",
            "prevent",
            "introduce",
            "pause",
            "angry",
            "help",
            "hurry",
            "scold",
            "money",
            "able",
            "keep",
            "misunderstand",
            "really",
            "here",
            "stand",
            "front",
            "worry",
            "away",
            "sure",
            "down",
            "correct",
            "agree",
            "during",
            "hope",
            "accomplish",
            "busy",
            "question",
            "put",
            "week",
            "opposite",
            "rude",
            "period",
            "disagree",
            "profit",
            "inside",
            "motorcycle",
            "need",
            "promote",
            "stuck",
            "expensive",
            "late",
            "traffic",
            "dime",
            "connect",
            "west",
            "me",
            "vacation",
            "gather",
            "happy",
            "for",
            "thankful",
            "afraid",
            "path",
            "year",
            "necessary",
            "tell",
            "left",
            "value",
            "past",
            "month",
            "come",
            "city",
            "tired",
            "goodbye",
            "off",
            "price",
            "tomorrow",
            "bottom",
            "corner",
            "outside",
            "reduce",
            "straight",
            "journey",
            "travel",
            "stop",
            "whatever",
            "river",
            "thank you",
            "confused",
            "hug",
            "sorry",
            "much",
            "sick",
            "leave",
            "trip",
            "resist",
            "assume",
            "want",
            "scared",
            "discover",
            "day",
            "allow",
            "world",
            "create",
            "recognize",
            "let",
            "interrupt",
            "that",
            "back",
            "same",
            "effort",
            "house",
            "every",
            "continue",
            "gone",
            "a",
            "contribute",
            "protect",
            "convince",
            "ok",
            "side",
            "across",
            "bike",
            "town",
            "better",
            "anyway",
            "second",
            "truck",
            "subway",
            "move",
            "cheap",
            "believe",
        ]
