#ifndef PARSER_H
#define PARSER_H
#include <stddef.h>

enum {
    TOK_EOF, TOK_ERROR, TOK_IDENT, TOK_NUMBER, TOK_STRING,
    TOK_LPAREN, TOK_RPAREN, TOK_LBRACE, TOK_RBRACE, TOK_COMMA, TOK_SEMI,
    TOK_PLUS, TOK_MINUS, TOK_STAR, TOK_SLASH, TOK_ASSIGN,
    TOK_EQ, TOK_NEQ, TOK_LT, TOK_GT, TOK_LE, TOK_GE, TOK_AND, TOK_OR
};

struct lexer { const char *src; int pos; int len; const char *text; long value; };
struct parser { struct lexer lx; int tok; };

int lex_next(struct lexer *lx);
int parse_expr(struct parser *p);
const char *tok_name(int t);
#endif
