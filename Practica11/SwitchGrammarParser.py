# Generated from SwitchGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,
        1,3,3,3,43,8,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,51,8,4,10,4,12,4,54,9,
        4,1,5,1,5,1,5,5,5,59,8,5,10,5,12,5,62,9,5,1,6,1,6,1,6,0,0,7,0,2,
        4,6,8,10,12,0,1,1,0,11,12,64,0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,
        0,0,6,30,1,0,0,0,8,46,1,0,0,0,10,55,1,0,0,0,12,63,1,0,0,0,14,16,
        3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,24,3,4,2,0,22,24,3,6,
        3,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,11,0,0,26,27,
        5,10,0,0,27,28,3,12,6,0,28,29,5,9,0,0,29,5,1,0,0,0,30,31,5,1,0,0,
        31,32,5,4,0,0,32,33,3,12,6,0,33,34,5,5,0,0,34,38,5,6,0,0,35,37,3,
        8,4,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,
        42,1,0,0,0,40,38,1,0,0,0,41,43,3,10,5,0,42,41,1,0,0,0,42,43,1,0,
        0,0,43,44,1,0,0,0,44,45,5,7,0,0,45,7,1,0,0,0,46,47,5,2,0,0,47,48,
        3,12,6,0,48,52,5,8,0,0,49,51,3,2,1,0,50,49,1,0,0,0,51,54,1,0,0,0,
        52,50,1,0,0,0,52,53,1,0,0,0,53,9,1,0,0,0,54,52,1,0,0,0,55,56,5,3,
        0,0,56,60,5,8,0,0,57,59,3,2,1,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,
        1,0,0,0,60,61,1,0,0,0,61,11,1,0,0,0,62,60,1,0,0,0,63,64,7,0,0,0,
        64,13,1,0,0,0,6,17,23,38,42,52,60
    ]

class SwitchGrammarParser ( Parser ):

    grammarFileName = "SwitchGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "'default'", "'('", 
                     "')'", "'{'", "'}'", "':'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "SWITCH", "CASE", "DEFAULT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI", "ASSIGN", 
                      "ID", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_switchStatement = 3
    RULE_caseBlock = 4
    RULE_defaultCase = 5
    RULE_expr = 6

    ruleNames =  [ "program", "statement", "assignment", "switchStatement", 
                   "caseBlock", "defaultCase", "expr" ]

    EOF = Token.EOF
    SWITCH=1
    CASE=2
    DEFAULT=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    COLON=8
    SEMI=9
    ASSIGN=10
    ID=11
    NUMBER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SwitchGrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(SwitchGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SwitchGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==11):
                    break

            self.state = 19
            self.match(SwitchGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(SwitchGrammarParser.AssignmentContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(SwitchGrammarParser.SwitchStatementContext,0)


        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SwitchGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.switchStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SwitchGrammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(SwitchGrammarParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchGrammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(SwitchGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SwitchGrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(SwitchGrammarParser.ID)
            self.state = 26
            self.match(SwitchGrammarParser.ASSIGN)
            self.state = 27
            self.expr()
            self.state = 28
            self.match(SwitchGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(SwitchGrammarParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(SwitchGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SwitchGrammarParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(SwitchGrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SwitchGrammarParser.RBRACE, 0)

        def caseBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchGrammarParser.CaseBlockContext)
            else:
                return self.getTypedRuleContext(SwitchGrammarParser.CaseBlockContext,i)


        def defaultCase(self):
            return self.getTypedRuleContext(SwitchGrammarParser.DefaultCaseContext,0)


        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = SwitchGrammarParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(SwitchGrammarParser.SWITCH)
            self.state = 31
            self.match(SwitchGrammarParser.LPAREN)
            self.state = 32
            self.expr()
            self.state = 33
            self.match(SwitchGrammarParser.RPAREN)
            self.state = 34
            self.match(SwitchGrammarParser.LBRACE)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 35
                self.caseBlock()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 41
                self.defaultCase()


            self.state = 44
            self.match(SwitchGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(SwitchGrammarParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchGrammarParser.ExprContext,0)


        def COLON(self):
            return self.getToken(SwitchGrammarParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(SwitchGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseBlock" ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseBlock" ):
                listener.exitCaseBlock(self)




    def caseBlock(self):

        localctx = SwitchGrammarParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(SwitchGrammarParser.CASE)
            self.state = 47
            self.expr()
            self.state = 48
            self.match(SwitchGrammarParser.COLON)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==11:
                self.state = 49
                self.statement()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(SwitchGrammarParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(SwitchGrammarParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(SwitchGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_defaultCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultCase" ):
                listener.enterDefaultCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultCase" ):
                listener.exitDefaultCase(self)




    def defaultCase(self):

        localctx = SwitchGrammarParser.DefaultCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_defaultCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SwitchGrammarParser.DEFAULT)
            self.state = 56
            self.match(SwitchGrammarParser.COLON)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==11:
                self.state = 57
                self.statement()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SwitchGrammarParser.ID, 0)

        def NUMBER(self):
            return self.getToken(SwitchGrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return SwitchGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = SwitchGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





