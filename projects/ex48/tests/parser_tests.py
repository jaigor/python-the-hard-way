from nose.tools import *
from ex48 import parser
from ex48.parser import ParserError, Sentence

def test_subject():
    result = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(result.subject, 'player')
    result2 = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(result2.subject, 'bear')
    assert_raises(ParserError, parser.parse_sentence, [('stop', 'the'), ('stop', 'and'), ('stop', 'at')])

def test_verb():
    result = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(result.verb, 'run')
    result2 = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(result2.verb, 'eat')
    assert_raises(ParserError, parser.parse_sentence, [('noun', 'bear'), ('stop', 'and'), ('noun', 'honey')])
   

def test_object():
    result = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(result.object, 'north')
    result2 = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(result2.object, 'honey')
    assert_raises(ParserError, parser.parse_sentence, [('noun', 'bear'), ('stop', 'and'), ('noun', 'honey')])