# Generated from IfElseLang.g4 by ANTLR 4.13.2
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
        4,1,20,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,3,3,39,8,3,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,52,8,5,10,5,12,5,55,9,5,
        1,5,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,5,3,5,67,8,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,
        0,1,2,1,0,17,18,1,0,11,16,74,0,19,1,0,0,0,2,25,1,0,0,0,4,33,1,0,
        0,0,6,38,1,0,0,0,8,40,1,0,0,0,10,45,1,0,0,0,12,68,1,0,0,0,14,72,
        1,0,0,0,16,74,1,0,0,0,18,20,3,6,3,0,19,18,1,0,0,0,20,21,1,0,0,0,
        21,19,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,
        0,0,25,26,3,4,2,0,26,29,5,17,0,0,27,28,5,10,0,0,28,30,3,14,7,0,29,
        27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,9,0,0,32,3,1,0,0,
        0,33,34,7,0,0,0,34,5,1,0,0,0,35,39,3,8,4,0,36,39,3,10,5,0,37,39,
        3,2,1,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,7,1,0,0,0,40,
        41,5,17,0,0,41,42,5,10,0,0,42,43,3,14,7,0,43,44,5,9,0,0,44,9,1,0,
        0,0,45,46,5,3,0,0,46,47,5,5,0,0,47,48,3,12,6,0,48,49,5,6,0,0,49,
        53,5,7,0,0,50,52,3,6,3,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,
        0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,66,5,8,0,0,57,58,
        5,4,0,0,58,62,5,7,0,0,59,61,3,6,3,0,60,59,1,0,0,0,61,64,1,0,0,0,
        62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,67,5,
        8,0,0,66,57,1,0,0,0,66,67,1,0,0,0,67,11,1,0,0,0,68,69,3,14,7,0,69,
        70,3,16,8,0,70,71,3,14,7,0,71,13,1,0,0,0,72,73,7,1,0,0,73,15,1,0,
        0,0,74,75,7,2,0,0,75,17,1,0,0,0,6,21,29,38,53,62,66
    ]

class IfElseLangParser ( Parser ):

    grammarFileName = "IfElseLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'string'", "'if'", "'else'", 
                     "'('", "')'", "'{'", "'}'", "';'", "'='", "'<'", "'>'", 
                     "'>='", "'<='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
                      "LT", "GT", "GE", "LE", "EQ", "NE", "ID", "NUMBER", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_type = 2
    RULE_statement = 3
    RULE_assignment = 4
    RULE_ifStatement = 5
    RULE_condition = 6
    RULE_expr = 7
    RULE_operator = 8

    ruleNames =  [ "program", "declaration", "type", "statement", "assignment", 
                   "ifStatement", "condition", "expr", "operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    ELSE=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    SEMI=9
    ASSIGN=10
    LT=11
    GT=12
    GE=13
    LE=14
    EQ=15
    NE=16
    ID=17
    NUMBER=18
    COMMENT=19
    WS=20

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
            return self.getToken(IfElseLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = IfElseLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 131086) != 0)):
                    break

            self.state = 23
            self.match(IfElseLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IfElseLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(IfElseLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = IfElseLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.type_()
            self.state = 26
            self.match(IfElseLangParser.ID)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 27
                self.match(IfElseLangParser.ASSIGN)
                self.state = 28
                self.expr()


            self.state = 31
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IfElseLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = IfElseLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(IfElseLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.IfStatementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(IfElseLangParser.DeclarationContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = IfElseLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.ifStatement()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.declaration()
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
            return self.getToken(IfElseLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(IfElseLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = IfElseLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(IfElseLangParser.ID)
            self.state = 41
            self.match(IfElseLangParser.ASSIGN)
            self.state = 42
            self.expr()
            self.state = 43
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(IfElseLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(IfElseLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.LBRACE)
            else:
                return self.getToken(IfElseLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.RBRACE)
            else:
                return self.getToken(IfElseLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(IfElseLangParser.ELSE, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = IfElseLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(IfElseLangParser.IF)
            self.state = 46
            self.match(IfElseLangParser.LPAREN)
            self.state = 47
            self.condition()
            self.state = 48
            self.match(IfElseLangParser.RPAREN)
            self.state = 49
            self.match(IfElseLangParser.LBRACE)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131086) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(IfElseLangParser.RBRACE)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 57
                self.match(IfElseLangParser.ELSE)
                self.state = 58
                self.match(IfElseLangParser.LBRACE)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131086) != 0):
                    self.state = 59
                    self.statement()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(IfElseLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(IfElseLangParser.OperatorContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = IfElseLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.expr()
            self.state = 69
            self.operator()
            self.state = 70
            self.expr()
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
            return self.getToken(IfElseLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(IfElseLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = IfElseLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
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


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(IfElseLangParser.LT, 0)

        def GT(self):
            return self.getToken(IfElseLangParser.GT, 0)

        def GE(self):
            return self.getToken(IfElseLangParser.GE, 0)

        def LE(self):
            return self.getToken(IfElseLangParser.LE, 0)

        def EQ(self):
            return self.getToken(IfElseLangParser.EQ, 0)

        def NE(self):
            return self.getToken(IfElseLangParser.NE, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = IfElseLangParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
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





