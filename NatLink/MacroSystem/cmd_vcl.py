# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.5, Fri Sep 30 08:41:50 2016

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <subcmds> = ('log' | 'fetch' | 'pull' | 'clone' | 'config' | 'help' | 'checkout' | 'checkout move' | 'checkout new' | 'checkout reset' | 'branch' | 'branch remove' | 'branch show' | 'status' | 'status show' | 'add' | 'add updated' | 'add patch' | 'add interactive' | 'diff' | 'diff cashed' | 'rebase' | 'rebase continue' | 'rebase master' | 'rebase develop' | 'rebase managed' | 'checkout master' | 'checkout branch' | 'commit' | 'commit amend' | 'commit modified' | 'commit message' | 'commit patch' | 'commit interactive' | 'commit previous message' | 'ref log' | 'cherry' | 'reset' | 'reset soft' | 'reset hard' | 'reset head' | 'reset hard head' | 'stash' | 'stash list' | 'stash show' | 'stash pop' | 'submodule init' | 'submodule update' ) ;
        <1> = 'versioning' <subcmds> ;
        <2> = 'minimise' ;
        <3> = 'close' ;
        <4> = 'list' ;
        <any> = <1>|<2>|<3>|<4>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'cmd','')
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

    def get_subcmds(self, list_buffer, functional, word):
        if word == 'log':
            list_buffer += 'log'
        elif word == 'fetch':
            list_buffer += 'fetch'
        elif word == 'pull':
            list_buffer += 'pull'
        elif word == 'clone':
            list_buffer += 'clone'
        elif word == 'config':
            list_buffer += 'config'
        elif word == 'help':
            list_buffer += 'help'
        elif word == 'checkout':
            list_buffer += 'checkout '
        elif word == 'checkout move':
            list_buffer += 'checkout -B '
        elif word == 'checkout new':
            list_buffer += 'checkout -b '
        elif word == 'checkout reset':
            list_buffer += 'checkout -- '
        elif word == 'branch':
            list_buffer += 'branch '
        elif word == 'branch remove':
            list_buffer += 'branch -D '
        elif word == 'branch show':
            list_buffer += 'branch{enter}'
        elif word == 'status':
            list_buffer += 'status'
        elif word == 'status show':
            list_buffer += 'status -uno{enter}'
        elif word == 'add':
            list_buffer += 'add'
        elif word == 'add updated':
            list_buffer += 'add -u '
        elif word == 'add patch':
            list_buffer += 'add --patch{enter}'
        elif word == 'add interactive':
            list_buffer += 'add --interactive{enter}'
        elif word == 'diff':
            list_buffer += 'diff'
        elif word == 'diff cashed':
            list_buffer += 'diff --cached '
        elif word == 'rebase':
            list_buffer += 'rebase -i '
        elif word == 'rebase continue':
            list_buffer += 'rebase --continue'
        elif word == 'rebase master':
            list_buffer += 'rebase -i master'
        elif word == 'rebase develop':
            list_buffer += 'rebase -i develop'
        elif word == 'rebase managed':
            list_buffer += 'rebase -i managed-zfs'
        elif word == 'checkout master':
            list_buffer += 'checkout master'
        elif word == 'checkout branch':
            list_buffer += 'checkout -b '
        elif word == 'commit':
            list_buffer += 'commit -s'
        elif word == 'commit amend':
            list_buffer += 'commit --amend -s'
        elif word == 'commit modified':
            list_buffer += 'commit -a '
        elif word == 'commit message':
            list_buffer += 'commit -m '
        elif word == 'commit patch':
            list_buffer += 'commit --patch{enter}'
        elif word == 'commit interactive':
            list_buffer += 'commit --interactive{enter}'
        elif word == 'commit previous message':
            list_buffer += 'commit -C '
        elif word == 'ref log':
            list_buffer += 'reflog'
        elif word == 'cherry':
            list_buffer += 'cherry-pick '
        elif word == 'reset':
            list_buffer += 'reset'
        elif word == 'reset soft':
            list_buffer += 'reset --soft'
        elif word == 'reset hard':
            list_buffer += 'reset --hard '
        elif word == 'reset head':
            list_buffer += 'reset HEAD'
        elif word == 'reset hard head':
            list_buffer += 'reset --hard HEAD'
        elif word == 'stash':
            list_buffer += 'stash'
        elif word == 'stash list':
            list_buffer += 'stash list'
        elif word == 'stash show':
            list_buffer += 'stash show'
        elif word == 'stash pop':
            list_buffer += 'stash pop'
        elif word == 'submodule init':
            list_buffer += 'submodule init'
        elif word == 'submodule update':
            list_buffer += 'submodule update{enter}'
        return list_buffer

    # 'versioning' <subcmds>
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'git '
            word = fullResults[1 + self.firstWord][0]
            top_buffer = self.get_subcmds(top_buffer, False, word)
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('git.vch', 28, '\'versioning\' <subcmds>', e)
            self.firstWord = -1

    # 'minimise'
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+'
            top_buffer += ' '
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += 'n'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_2(words[1:], fullResults)
        except Exception, e:
            handle_error('cmd.vcl', 6, '\'minimise\'', e)
            self.firstWord = -1

    # 'close'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+'
            top_buffer += ' '
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += 'c'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('cmd.vcl', 7, '\'close\'', e)
            self.firstWord = -1

    # 'list'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'dir '
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_4(words[1:], fullResults)
        except Exception, e:
            handle_error('cmd.vcl', 8, '\'list\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
