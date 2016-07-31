# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.5, Sun Jul 31 14:41:33 2016

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <1> = 'Refresh View' ;
        <27> = 'Refresh' ;
        <view_mode> = ('Extra Large' | 'Large' | 'Medium' | 'List' | 'Details' ) ;
        <2> = 'View Mode' <view_mode> ;
        <3> = 'Search' ;
        <4> = ('Copy' | 'Paste' | 'Go' ) 'Address' ;
        <5> = 'Go' ('Back' | 'Forward' ) ;
        <6> = 'Go' ('Back' | 'Forward' ) ('one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine' | 10) ;
        <7> = ('Copy' | 'Paste' | 'Go' ) ('Address' | 'URL' ) ;
        <8> = 'New Folder' ;
        <9> = 'Folders' ;
        <10> = 'Open Folder' ;
        <11> = 'Expand That' ;
        <12> = 'Collapse That' ;
        <13> = 'Share That' ;
        <14> = 'Copy Filename' ;
        <15> = 'Copy Folder Name' ;
        <16> = 'Copy Leaf Name' ;
        <17> = 'new text Document' ;
        <18> = 'Duplicate That' ;
        <19> = 'Rename That' ;
        <20> = 'Paste Here' ;
        <21> = ('Show' | 'Edit' ) 'Properties' ;
        <22> = 'Toggle Read Only' ;
        <28> = 'Read Only' ;
        <23> = 'open with' ;
        <24> = ('open' | 'edit' ) 'with vim' ;
        <25> = 'file edit' ;
        <26> = 'file options' ;
        <any> = <1>|<27>|<2>|<3>|<4>|<5>|<6>|<7>|<8>|<9>|<10>|<11>|<12>|<13>|<14>|<15>|<16>|<17>|<18>|<19>|<20>|<21>|<22>|<28>|<23>|<24>|<25>|<26>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'explorer','')
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

    # 'Refresh View'
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+v}r'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_1(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 6, '\'Refresh View\'', e)
            self.firstWord = -1

    # 'Refresh'
    def gotResults_27(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+v}r'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_27(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 6, '\'Refresh\'', e)
            self.firstWord = -1

    def get_view_mode(self, list_buffer, functional, word):
        if word == 'Extra Large':
            list_buffer += 'x'
        elif word == 'Large':
            list_buffer += 'r'
        elif word == 'Medium':
            list_buffer += 'm'
        elif word == 'List':
            list_buffer += 'l'
        elif word == 'Details':
            list_buffer += 'd'
        return list_buffer

    # 'View Mode' <view_mode>
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+v}'
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_view_mode(top_buffer, False, word)
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('explorer.vcl', 9, '\'View Mode\' <view_mode>', e)
            self.firstWord = -1

    # 'Search'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+e}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 10, '\'Search\'', e)
            self.firstWord = -1

    # ('Copy' | 'Paste' | 'Go') 'Address'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+d}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            word = fullResults[0 + self.firstWord][0]
            if word == 'Copy':
                top_buffer += '{Ctrl+c}'
            elif word == 'Paste':
                top_buffer += '{Ctrl+v}'
            elif word == 'Go':
                top_buffer += ''
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_4(words[2:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 11, '(\'Copy\' | \'Paste\' | \'Go\') \'Address\'', e)
            self.firstWord = -1

    # 'Go' ('Back' | 'Forward')
    def gotResults_5(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '{Alt+'
            word = fullResults[1 + self.firstWord][0]
            if word == 'Back':
                dragon_arg1 += 'Left'
            elif word == 'Forward':
                dragon_arg1 += 'Right'
            dragon_arg1 += '}'
            saved_firstWord = self.firstWord
            call_Dragon('SendSystemKeys', 'si', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_5(words[2:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 14, '\'Go\' (\'Back\' | \'Forward\')', e)
            self.firstWord = -1

    # 'Go' ('Back' | 'Forward') 1..10
    def gotResults_6(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '{Alt+'
            word = fullResults[1 + self.firstWord][0]
            if word == 'Back':
                dragon_arg1 += 'Left'
            elif word == 'Forward':
                dragon_arg1 += 'Right'
            dragon_arg1 += '_'
            word = fullResults[2 + self.firstWord][0]
            dragon_arg1 += self.convert_number_word(word)
            dragon_arg1 += '}'
            saved_firstWord = self.firstWord
            call_Dragon('SendSystemKeys', 'si', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 3
            if len(words) > 3: self.gotResults_6(words[3:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 15, '\'Go\' (\'Back\' | \'Forward\') 1..10', e)
            self.firstWord = -1

    # ('Copy' | 'Paste' | 'Go') ('Address' | 'URL')
    def gotResults_7(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+d}'
            word = fullResults[0 + self.firstWord][0]
            if word == 'Copy':
                top_buffer += '{Ctrl+c}'
            elif word == 'Paste':
                top_buffer += '{Ctrl+v}'
            elif word == 'Go':
                top_buffer += ''
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_7(words[2:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 16, '(\'Copy\' | \'Paste\' | \'Go\') (\'Address\' | \'URL\')', e)
            self.firstWord = -1

    # 'New Folder'
    def gotResults_8(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}wf'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_8(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 24, '\'New Folder\'', e)
            self.firstWord = -1

    # 'Folders'
    def gotResults_9(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+v}eo'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_9(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 25, '\'Folders\'', e)
            self.firstWord = -1

    # 'Open Folder'
    def gotResults_10(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}{Enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_10(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 26, '\'Open Folder\'', e)
            self.firstWord = -1

    # 'Expand That'
    def gotResults_11(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '{Alt+NumKey+}'
            saved_firstWord = self.firstWord
            call_Dragon('SendSystemKeys', 'si', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_11(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 27, '\'Expand That\'', e)
            self.firstWord = -1

    # 'Collapse That'
    def gotResults_12(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '{Alt+NumKey-}'
            saved_firstWord = self.firstWord
            call_Dragon('SendSystemKeys', 'si', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_12(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 28, '\'Collapse That\'', e)
            self.firstWord = -1

    # 'Share That'
    def gotResults_13(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}r'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '1000'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{Tab_5}{Right_2}{Alt+s}{Enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_13(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 29, '\'Share That\'', e)
            self.firstWord = -1

    # 'Copy Filename'
    def gotResults_14(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}m{Ctrl+c}{Alt+d}{Right}\\{Ctrl+v}'
            top_buffer += '{Home}{Shift+End}{Ctrl+c}{Esc}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_14(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 34, '\'Copy Filename\'', e)
            self.firstWord = -1

    # 'Copy Folder Name'
    def gotResults_15(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+d}{Ctrl+c}{Esc}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_15(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 35, '\'Copy Folder Name\'', e)
            self.firstWord = -1

    # 'Copy Leaf Name'
    def gotResults_16(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}m{Ctrl+c}{Esc}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_16(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 36, '\'Copy Leaf Name\'', e)
            self.firstWord = -1

    # 'new text Document'
    def gotResults_17(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}wt'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_17(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 38, '\'new text Document\'', e)
            self.firstWord = -1

    # 'Duplicate That'
    def gotResults_18(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+c}{Left}{Ctrl+v}c'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_18(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 39, '\'Duplicate That\'', e)
            self.firstWord = -1

    # 'Rename That'
    def gotResults_19(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{F2}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_19(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 40, '\'Rename That\'', e)
            self.firstWord = -1

    # 'Paste Here'
    def gotResults_20(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '1'
            dragon_arg2 = ''
            dragon_arg2 += '1'
            saved_firstWord = self.firstWord
            call_Dragon('ButtonClick', 'ii', [dragon_arg1, dragon_arg2])
            self.firstWord = saved_firstWord
            top_buffer += '{Ctrl+v}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_20(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 41, '\'Paste Here\'', e)
            self.firstWord = -1

    # ('Show' | 'Edit') 'Properties'
    def gotResults_21(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}r'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_21(words[2:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 43, '(\'Show\' | \'Edit\') \'Properties\'', e)
            self.firstWord = -1

    # 'Toggle Read Only'
    def gotResults_22(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}r'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '2000'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{Alt+r}{Enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_22(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 44, '\'Toggle Read Only\'', e)
            self.firstWord = -1

    # 'Read Only'
    def gotResults_28(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}r'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '2000'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{Alt+r}{Enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_28(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 44, '\'Read Only\'', e)
            self.firstWord = -1

    # 'open with'
    def gotResults_23(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{shift+f10}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += 'h'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_23(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 48, '\'open with\'', e)
            self.firstWord = -1

    # ('open' | 'edit') 'with vim'
    def gotResults_24(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{shift+f10}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += 'v'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_24(words[2:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 49, '(\'open\' | \'edit\') \'with vim\'', e)
            self.firstWord = -1

    # 'file edit'
    def gotResults_25(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}e'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_25(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 50, '\'file edit\'', e)
            self.firstWord = -1

    # 'file options'
    def gotResults_26(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+f}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_26(words[1:], fullResults)
        except Exception, e:
            handle_error('explorer.vcl', 51, '\'file options\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
