# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.5, Fri Sep 30 08:41:51 2016

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <1> = ('contacts' | 'recent' ) ;
        <2> = ('messages' | 'add person' | 'call person' ) ;
        <3> = 'text' ;
        <4> = 'login reset' ;
        <any> = <1>|<2>|<3>|<4>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'skype','')
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

    # ('contacts' | 'recent')
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{alt+'
            word = fullResults[0 + self.firstWord][0]
            if word == 'contacts':
                top_buffer += '1'
            elif word == 'recent':
                top_buffer += '2'
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_1(words[1:], fullResults)
        except Exception, e:
            handle_error('skype.vcl', 2, '(\'contacts\' | \'recent\')', e)
            self.firstWord = -1

    # ('messages' | 'add person' | 'call person')
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            word = fullResults[0 + self.firstWord][0]
            if word == 'messages':
                limit += '3'
            elif word == 'add person':
                limit += '4'
            elif word == 'call person':
                limit += '5'
            for i in range(to_long(limit)):
                top_buffer += '{shift+tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_2(words[1:], fullResults)
        except Exception, e:
            handle_error('skype.vcl', 3, '(\'messages\' | \'add person\' | \'call person\')', e)
            self.firstWord = -1

    # 'text'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            limit += '3'
            for i in range(to_long(limit)):
                top_buffer += '{tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('skype.vcl', 4, '\'text\'', e)
            self.firstWord = -1

    # 'login reset'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{alt+s}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '200'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += 's'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '500'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{tab}'
            top_buffer += 'cideric306'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '200'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_4(words[1:], fullResults)
        except Exception, e:
            handle_error('skype.vcl', 5, '\'login reset\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
