# Generated from SwitchGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwitchGrammarParser import SwitchGrammarParser
else:
    from SwitchGrammarParser import SwitchGrammarParser

# This class defines a complete listener for a parse tree produced by SwitchGrammarParser.
class SwitchGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by SwitchGrammarParser#program.
    def enterProgram(self, ctx:SwitchGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#program.
    def exitProgram(self, ctx:SwitchGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by SwitchGrammarParser#statement.
    def enterStatement(self, ctx:SwitchGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#statement.
    def exitStatement(self, ctx:SwitchGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by SwitchGrammarParser#assignment.
    def enterAssignment(self, ctx:SwitchGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#assignment.
    def exitAssignment(self, ctx:SwitchGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SwitchGrammarParser#switchStatement.
    def enterSwitchStatement(self, ctx:SwitchGrammarParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#switchStatement.
    def exitSwitchStatement(self, ctx:SwitchGrammarParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by SwitchGrammarParser#caseBlock.
    def enterCaseBlock(self, ctx:SwitchGrammarParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#caseBlock.
    def exitCaseBlock(self, ctx:SwitchGrammarParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by SwitchGrammarParser#defaultCase.
    def enterDefaultCase(self, ctx:SwitchGrammarParser.DefaultCaseContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#defaultCase.
    def exitDefaultCase(self, ctx:SwitchGrammarParser.DefaultCaseContext):
        pass


    # Enter a parse tree produced by SwitchGrammarParser#expr.
    def enterExpr(self, ctx:SwitchGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by SwitchGrammarParser#expr.
    def exitExpr(self, ctx:SwitchGrammarParser.ExprContext):
        pass



del SwitchGrammarParser