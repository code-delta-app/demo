#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include "parser.h"
#include "log.h"

/* Hand-rolled tokenizer for the buildproj expression language. */

static const char *tok_names[] = {
    "IDENT", "NUMBER", "STRING", "LPAREN", "RPAREN", "LBRACE",
    "RBRACE", "COMMA", "SEMI", "PLUS", "MINUS", "STAR",
    "SLASH", "ASSIGN", "EQ", "NEQ", "LT", "GT",
};

const char *tok_name(int t) {
    if (t < 0 || t >= (int)(sizeof tok_names / sizeof *tok_names))
        return "?";
    return tok_names[t];
}

static int is_ident_start(int c) { return isalpha(c) || c == '_'; }
static int is_ident_char(int c)  { return isalnum(c) || c == '_'; }

int lex_next(struct lexer *lx) {
    while (isspace(lx->src[lx->pos])) lx->pos++;
    int c = lx->src[lx->pos];
    if (c == 0) return TOK_EOF;
    if (is_ident_start(c)) {
        int start = lx->pos;
        while (is_ident_char(lx->src[lx->pos])) lx->pos++;
        lx->len = lx->pos - start;
        lx->text = lx->src + start;
        return TOK_IDENT;
    }
    if (isdigit(c)) {
        lx->value = strtol(lx->src + lx->pos, NULL, 10);
        while (isdigit(lx->src[lx->pos])) lx->pos++;
        return TOK_NUMBER;
    }
    if (c == '(') { lx->pos++; return TOK_LPAREN; }
    if (c == ')') { lx->pos++; return TOK_RPAREN; }
    if (c == '{') { lx->pos++; return TOK_LBRACE; }
    if (c == '}') { lx->pos++; return TOK_RBRACE; }
    if (c == ',') { lx->pos++; return TOK_COMMA; }
    if (c == ';') { lx->pos++; return TOK_SEMI; }
    if (c == '+') { lx->pos++; return TOK_PLUS; }
    if (c == '-') { lx->pos++; return TOK_MINUS; }
    if (c == '*') { lx->pos++; return TOK_STAR; }
    if (c == '/') { lx->pos++; return TOK_SLASH; }
    if (c == '<') { lx->pos++; return TOK_LT; }
    if (c == '>') { lx->pos++; return TOK_GT; }
    log_warn("lex: unexpected character 0x%02x", c);
    lx->pos++;
    return TOK_ERROR;
}

static int parse_primary(struct parser *p);

static int parse_term(struct parser *p) {
    int left = parse_primary(p);
    while (p->tok == TOK_STAR || p->tok == TOK_SLASH) {
        int op = p->tok;
        p->tok = lex_next(&p->lx);
        int right = parse_primary(p);
        if (op == TOK_SLASH && right == 0) {
            log_warn("parse: division by zero folded to 0");
            left = 0;
        } else {
            left = (op == TOK_STAR) ? left * right : left / right;
        }
    }
    return left;
}

int parse_expr(struct parser *p) {
    int left = parse_term(p);
    while (p->tok == TOK_PLUS || p->tok == TOK_MINUS) {
        int op = p->tok;
        p->tok = lex_next(&p->lx);
        int right = parse_term(p);
        left = (op == TOK_PLUS) ? left + right : left - right;
    }
    return left;
}

static int parse_primary(struct parser *p) {
    if (p->tok == TOK_NUMBER) {
        int v = (int)p->lx.value;
        p->tok = lex_next(&p->lx);
        return v;
    }
    if (p->tok == TOK_LPAREN) {
        p->tok = lex_next(&p->lx);
        int v = parse_expr(p);
        if (p->tok != TOK_RPAREN) log_warn("parse: missing )");
        else p->tok = lex_next(&p->lx);
        return v;
    }
    log_warn("parse: unexpected token %s", tok_name(p->tok));
    p->tok = lex_next(&p->lx);
    return 0;
}
