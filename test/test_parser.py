import nose
from mf2py.parser import Parser

def test_empty():
   p = Parser() 
   assert type(p) is not None
   assert type(p.to_dict()) is dict

def test_open_file():
   p = Parser(open("test/examples/empty.html"))
   assert p.__doc__ is not None
   assert type(p) is not None
   assert type(p.to_dict()) is dict

def test_user_agent():
    assert Parser.useragent == 'mf2py - microformats2 parser for python'
    Parser.useragent = 'something else'
    assert Parser.useragent == 'something else'
    # set back to default. damn stateful classes
    Parser.useragent = 'mf2py - microformats2 parser for python'
 
def test_base():
    p = Parser(open("test/examples/base.html"))
    assert p.__url__ == u"http://tantek.com/"

def test_simple_parse():
    p = Parser(open("test/examples/simple_person_reference.html"))
    result = p.to_dict()
    assert result["items"][0]["properties"] == {u'name': [u'Frances Berriman']}

def test_simple_person_reference_implied():
    p = Parser(open("test/examples/simple_person_reference_implied.html"))
    result = p.to_dict()
    assert result["items"][0]["properties"] == {u'name': [u'Frances Berriman']}

def test_simple_person_reference_same_element():
    p = Parser(open("test/examples/simple_person_reference_same_element.html"))
    result = p.to_dict()
    assert result["items"][0]["properties"] == {u'name': [u'Frances Berriman']}

def test_person_with_url():
    p = Parser(open("test/examples/person_with_url.html"))
    result = p.to_dict()
    assert result["items"][0]["properties"]["name"] == [u'Tom Morris']
    assert result["items"][0]["properties"]["url"] == [u'http://tommorris.org/']

