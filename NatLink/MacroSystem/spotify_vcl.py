# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.5, Mon Oct 17 08:06:59 2016

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <dgndictation> imported;
        <1> = 'Search bar' ;
        <2> = 'Search for' <dgndictation> ;
        <next_back> = ('next' | 'back' ) ;
        <3> = <next_back> 'track' ;
        <4> = <next_back> 'browser' ;
        <5> = ('play' | 'pause' ) ;
        <6> = 'volume' ('Up' | 'Down' | 'Mute' ) ;
        <7> = 'large artwork toggle' ;
        <8> = 'close window' ;
        <any> = <1>|<2>|<3>|<4>|<5>|<6>|<7>|<8>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'spotify','')
        if not window: return None
        self.firstWord = 0
        # Return if same window and title as before
        if moduleInfo == self.currentModule: return None
        self.currentModule = moduleInfo

        self.deactivateAll()
        title = string.lower(moduleInfo[1])
        if string.find(title,'') >= 0:
            for rule in self.ruleSet1:
                try:
                    self.activate(rule,window)
                except natlink.BadWindow:
                    pass

    def convert_number_word(self, word):
        if   word == 'zero':
            return '0'
        elif word == 'one':
            return '1'
        elif word == 'two':
            return '2'
        elif word == 'three':
            return '3'
        elif word == 'four':
            return '4'
        elif word == 'five':
            return '5'
        elif word == 'six':
            return '6'
        elif word == 'seven':
            return '7'
        elif word == 'eight':
            return '8'
        elif word == 'nine':
            return '9'
        else:
            return word

    # 'Search bar'
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+l}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_1(words[1:], fullResults)
        except Exception, e:
            handle_error('spotify.vcl', 5, '\'Search bar\'', e)
            self.firstWord = -1

    # 'Search for' <_anything>
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        fullResults = combineDictationWords(fullResults)
        opt = 1 + self.firstWord
        if opt >= len(fullResults) or fullResults[opt][1] != 'converted dgndictation':
            fullResults.insert(opt, ['', 'converted dgndictation'])
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+l}'
            word = fullResults[1 + self.firstWord][0]
            top_buffer += word
            top_buffer += '{Enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('spotify.vcl', 6, '\'Search for\' <_anything>', e)
            self.firstWord = -1

    def get_next_back(self, list_buffer, functional, word):
        if word == 'next':
            list_buffer += 'Right'
        elif word == 'back':
            list_buffer += 'Left'
        return list_buffer

    # <next_back> 'track'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Esc}{Ctrl+'
            word = fullResults[0 + self.firstWord][0]
            top_buffer = self.get_next_back(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('spotify.vcl', 10, '<next_back> \'track\'', e)
            self.firstWord = -1

    # <next_back> 'browser'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Esc}{Alt+'
            word = fullResults[0 + self.firstWord][0]
            top_buffer = self.get_next_back(top_buffer, False, word)
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('spotify.vcl', 11, '<next_back> \'browser\'', e)
            self.firstWord = -1

    # ('play' | 'pause')
    def gotResults_5(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += ' '
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_5(words[1:], fullResults)
        except Exception, e:
            handle_error('spotify.vcl', 13, '(\'play\' | \'pause\')', e)
            self.firstWord = -1

    # 'volume' ('Up' | 'Down' | 'Mute')
    def gotResults_6(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+'
            word = fullResults[1 + self.firstWord][0]
            if word == 'Up':
                top_buffer += 'Up'
            elif word == 'Down':
                top_buffer += 'Down'
            elif word == 'Mute':
                top_buffer += 'shift+Down'
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_6(words[2:], fullResults)
        except Exception, e:
            handle_error('spotify.vcl', 14, '\'volume\' (\'Up\' | \'Down\' | \'Mute\')', e)
            self.firstWord = -1

    # 'large artwork toggle'
    def gotResults_7(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{alt+v}l'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_7(words[1:], fullResults)
        except Exception, e:
            handle_error('spotify.vcl', 15, '\'large artwork toggle\'', e)
            self.firstWord = -1

    # 'close window'
    def gotResults_8(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{alt+f4}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_8(words[1:], fullResults)
        except Exception, e:
            handle_error('spotify.vcl', 16, '\'close window\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
