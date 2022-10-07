#!/usr/bin/env python

from re import findall
from sys import stdin
from os import path, environ

import sys
stopwords = ['a',
             'about',
             'above',
             'across',
             'after',
             'afterwards',
             'again',
             'against',
             'all',
             'almost',
             'alone',
             'along',
             'already',
             'also',
             'although',
             'always',
             'am',
             'among',
             'amongst',
             'amoungst',
             'amount',
             'an',
             'and',
             'another',
             'any',
             'anyhow',
             'anyone',
             'anything',
             'anyway',
             'anywhere',
             'are',
             'around',
             'as',
             'at',
             'back',
             'be',
             'became',
             'because',
             'become',
             'becomes',
             'becoming',
             'been',
             'before',
             'beforehand',
             'behind',
             'being',
             'below',
             'beside',
             'besides',
             'between',
             'beyond',
             'bill',
             'both',
             'bottom',
             'by',
             'can',
             'cannot',
             'cant',
             'con',
             'could',
             'couldnt',
             'de',
             'describe',
             'detail',
             'do',
             'done',
             'down',
             'due',
             'during',
             'each',
             'eg',
             'eight',
             'either',
             'eleven',
             'else',
             'elsewhere',
             'empty',
             'enough',
             'etc',
             'even',
             'ever',
             'every',
             'everyone',
             'everything',
             'everywhere',
             'except',
             'few',
             'fifteen',
             'fify',
             'fill',
             'fire',
             'first',
             'five',
             'for',
             'former',
             'formerly',
             'forty',
             'four',
             'from',
             'front',
             'full',
             'further',
             'get',
             'give',
             'go',
             'had',
             'has',
             'hasnt',
             'have',
             'he',
             'hence',
             'her',
             'here',
             'hereafter',
             'hereby',
             'herein',
             'hereupon',
             'hers',
             'herself',
             'him',
             'himself',
             'his',
             'how',
             'however',
             'hundred',
             'ie',
             'if',
             'in',
             'inc',
             'indeed',
             'interest',
             'into',
             'is',
             'it',
             'its',
             'itself',
             'keep',
             'last',
             'latter',
             'latterly',
             'least',
             'less',
             'ltd',
             'made',
             'many',
             'may',
             'me',
             'meanwhile',
             'might',
             'mill',
             'mine',
             'more',
             'moreover',
             'most',
             'mostly',
             'move',
             'much',
             'must',
             'my',
             'myself',
             'name',
             'namely',
             'neither',
             'never',
             'nevertheless',
             'next',
             'nine',
             'no',
             'nobody',
             'none',
             'noone',
             'nor',
             'not',
             'nothing',
             'now',
             'nowhere',
             'of',
             'off',
             'often',
             'on',
             'once',
             'one',
             'only',
             'onto',
             'or',
             'other',
             'others',
             'otherwise',
             'our',
             'ours',
             'ourselves',
             'out',
             'over',
             'own',
             'part',
             'per',
             'perhaps',
             'please',
             'put',
             'rather',
             're',
             'same',
             'see',
             'seem',
             'seemed',
             'seeming',
             'seems',
             'serious',
             'several',
             'she',
             'should',
             'show',
             'side',
             'since',
             'sincere',
             'six',
             'sixty',
             'so',
             'some',
             'somehow',
             'someone',
             'something',
             'sometime',
             'sometimes',
             'somewhere',
             'still',
             'such',
             'system',
             'take',
             'ten',
             'than',
             'that',
             'the',
             'their',
             'them',
             'themselves',
             'then',
             'thence',
             'there',
             'thereafter',
             'thereby',
             'therefore',
             'therein',
             'thereupon',
             'these',
             'they',
             'thickv',
             'thin',
             'third',
             'this',
             'those',
             'though',
             'three',
             'through',
             'throughout',
             'thru',
             'thus',
             'to',
             'together',
             'too',
             'top',
             'toward',
             'towards',
             'twelve',
             'twenty',
             'two',
             'un',
             'under',
             'until',
             'up',
             'upon',
             'us',
             'very',
             'via',
             'was',
             'we',
             'well',
             'were',
             'what',
             'whatever',
             'when',
             'whence',
             'whenever',
             'where',
             'whereafter',
             'whereas',
             'whereby',
             'wherein',
             'whereupon',
             'wherever',
             'whether',
             'which',
             'while',
             'whither',
             'who',
             'whoever',
             'whole',
             'whom',
             'whose',
             'why',
             'will',
             'with',
             'within',
             'without',
             'would',
             'yet',
             'you',
             'your',
             'yours',
             'does',
             'did',
             'doing',
             'theirs',
             'yourself',
             'yourselves',
             'just',
             'the']


for line in stdin:

    doc_id = environ["map_input_file"]

    doc_id = path.split(doc_id)[-1]

    words = line.rstrip('\n').split()

    words = [word.lower() for word in words]

    words = [word for word in words if word not in stopwords]

    for word in words:
        print(f"{word}\t{doc_id}:1")