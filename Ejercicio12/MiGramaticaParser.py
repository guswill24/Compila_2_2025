# Generated from MiGramatica.g4 by ANTLR 4.13.2
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
        4,1,19,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,33,8,2,5,2,35,8,2,10,2,12,2,38,9,2,1,2,1,
        2,1,2,1,2,1,2,3,2,45,8,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,3,2,53,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,70,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,
        5,0,1,10,6,0,2,4,6,8,10,0,3,1,0,12,15,1,0,10,11,1,0,8,9,87,0,15,
        1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,54,1,0,0,0,8,58,1,0,0,0,10,69,
        1,0,0,0,12,13,3,2,1,0,13,14,5,16,0,0,14,16,1,0,0,0,15,12,1,0,0,0,
        16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,
        0,0,1,20,1,1,0,0,0,21,24,3,4,2,0,22,24,3,8,4,0,23,21,1,0,0,0,23,
        22,1,0,0,0,24,3,1,0,0,0,25,26,5,1,0,0,26,27,5,3,0,0,27,28,3,6,3,
        0,28,29,5,4,0,0,29,36,5,5,0,0,30,32,3,2,1,0,31,33,5,16,0,0,32,31,
        1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,30,1,0,0,0,35,38,1,0,0,0,
        36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,52,5,
        6,0,0,40,41,5,2,0,0,41,48,5,5,0,0,42,44,3,2,1,0,43,45,5,16,0,0,44,
        43,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,42,1,0,0,0,47,50,1,0,0,
        0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,53,
        5,6,0,0,52,40,1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,0,54,55,5,17,0,0,
        55,56,7,0,0,0,56,57,5,18,0,0,57,7,1,0,0,0,58,59,5,17,0,0,59,60,5,
        7,0,0,60,61,3,10,5,0,61,9,1,0,0,0,62,63,6,5,-1,0,63,70,5,18,0,0,
        64,70,5,17,0,0,65,66,5,3,0,0,66,67,3,10,5,0,67,68,5,4,0,0,68,70,
        1,0,0,0,69,62,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,70,79,1,0,0,0,
        71,72,10,5,0,0,72,73,7,1,0,0,73,78,3,10,5,6,74,75,10,4,0,0,75,76,
        7,2,0,0,76,78,3,10,5,5,77,71,1,0,0,0,77,74,1,0,0,0,78,81,1,0,0,0,
        79,77,1,0,0,0,79,80,1,0,0,0,80,11,1,0,0,0,81,79,1,0,0,0,10,17,23,
        32,36,44,48,52,69,77,79
    ]

class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'('", "')'", "'{'", 
                     "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
                     "'=='", "'!='", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "NEQ", "SEMI", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_ifElseStmt = 2
    RULE_condicion = 3
    RULE_asignacion = 4
    RULE_expresion = 5

    ruleNames =  [ "programa", "sentencia", "ifElseStmt", "condicion", "asignacion", 
                   "expresion" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    ASSIGN=7
    PLUS=8
    MINUS=9
    MUL=10
    DIV=11
    GT=12
    LT=13
    EQ=14
    NEQ=15
    SEMI=16
    ID=17
    INT=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiGramaticaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiGramaticaParser.SEMI)
            else:
                return self.getToken(MiGramaticaParser.SEMI, i)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = MiGramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.sentencia()
                self.state = 13
                self.match(MiGramaticaParser.SEMI)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==17):
                    break

            self.state = 19
            self.match(MiGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElseStmt(self):
            return self.getTypedRuleContext(MiGramaticaParser.IfElseStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = MiGramaticaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.ifElseStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.asignacion()
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


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_ifElseStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseContext(IfElseStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.IfElseStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiGramaticaParser.IF, 0)
        def LPAREN(self):
            return self.getToken(MiGramaticaParser.LPAREN, 0)
        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)

        def RPAREN(self):
            return self.getToken(MiGramaticaParser.RPAREN, 0)
        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiGramaticaParser.LBRACE)
            else:
                return self.getToken(MiGramaticaParser.LBRACE, i)
        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiGramaticaParser.RBRACE)
            else:
                return self.getToken(MiGramaticaParser.RBRACE, i)
        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)

        def ELSE(self):
            return self.getToken(MiGramaticaParser.ELSE, 0)
        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiGramaticaParser.SEMI)
            else:
                return self.getToken(MiGramaticaParser.SEMI, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)



    def ifElseStmt(self):

        localctx = MiGramaticaParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifElseStmt)
        self._la = 0 # Token type
        try:
            localctx = MiGramaticaParser.IfElseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(MiGramaticaParser.IF)
            self.state = 26
            self.match(MiGramaticaParser.LPAREN)
            self.state = 27
            self.condicion()
            self.state = 28
            self.match(MiGramaticaParser.RPAREN)
            self.state = 29
            self.match(MiGramaticaParser.LBRACE)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==17:
                self.state = 30
                self.sentencia()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 31
                    self.match(MiGramaticaParser.SEMI)


                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(MiGramaticaParser.RBRACE)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 40
                self.match(MiGramaticaParser.ELSE)
                self.state = 41
                self.match(MiGramaticaParser.LBRACE)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1 or _la==17:
                    self.state = 42
                    self.sentencia()
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 43
                        self.match(MiGramaticaParser.SEMI)


                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.match(MiGramaticaParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionSimpleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)
        def GT(self):
            return self.getToken(MiGramaticaParser.GT, 0)
        def LT(self):
            return self.getToken(MiGramaticaParser.LT, 0)
        def EQ(self):
            return self.getToken(MiGramaticaParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiGramaticaParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionSimple" ):
                listener.enterCondicionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionSimple" ):
                listener.exitCondicionSimple(self)



    def condicion(self):

        localctx = MiGramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = MiGramaticaParser.CondicionSimpleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MiGramaticaParser.ID)
            self.state = 55
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.match(MiGramaticaParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(MiGramaticaParser.ASSIGN, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def asignacion(self):

        localctx = MiGramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            localctx = MiGramaticaParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiGramaticaParser.ID)
            self.state = 59
            self.match(MiGramaticaParser.ASSIGN)
            self.state = 60
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(MiGramaticaParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiGramaticaParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)

        def PLUS(self):
            return self.getToken(MiGramaticaParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MiGramaticaParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiGramaticaParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(MiGramaticaParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = MiGramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.match(MiGramaticaParser.INT)
                pass
            elif token in [17]:
                localctx = MiGramaticaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(MiGramaticaParser.ID)
                pass
            elif token in [3]:
                localctx = MiGramaticaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(MiGramaticaParser.LPAREN)
                self.state = 66
                self.expresion(0)
                self.state = 67
                self.match(MiGramaticaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiGramaticaParser.MulDivContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 71
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 72
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = MiGramaticaParser.AddSubContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        self.expresion(5)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




