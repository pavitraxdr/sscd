def yacc():
    s="""
    %{
    #include<math.h>
    #include<stdio.h>
    #include<ctype.h>
    #define YYSTYPE double
%}

%%

input:|input line ;

line: '\n' | expr'\n' {printf("Result is %g", $1);} ;

expr: expr '+' term {$$ = $1 + $3;}
    | expr '-' term {$$ = $1 - $3;}
    | term {$$ = $1;} ;

term: term '*' factor {$$ = $1*$3;}
    | term '/' factor {$$ = $1/$3;}
    | factor {$$ = $1;} ;

factor: NUM {$$ = $1;} ;

NUM: digit {$$ = $1;} ;

digit: '0' {$$ = 0;}
    |'1' {$$ = 1;} 
    |'2' {$$ = 2;} 
    |'3' {$$ = 3;} 
    |'4' {$$ = 4;} 
    |'5' {$$ = 5;} 
    |'6' {$$ = 6;} 
    |'7' {$$ = 7;} 
    |'8' {$$ = 8;} 
    |'9' {$$ = 9;} ;

%%

int yylex(){
    return getchar();}

int main(){
    return yyparse();}

void yyerror(char*s){
    printf("%s",s); }
    """
    print(s)

def sic():
    s="""
    program = open("input.txt", "r").read()
program=program.split('\n')
op=open("opcode.txt", "r").read().split('\n')
sym=open("symtab.txt", "r").read().split('\n')
opcode={}
symtab={}
for i in op:
    temp=i.split(' ')
    opcode[temp[0]]=[temp[1]]
for i in sym:
    temp=i.split(' ')
    symtab[temp[0]]=[temp[1]]
line1=program[0].split(' ')
start=0
program_name=line1[0]
objcode=[]
for i in range(len(line1)):
    if line1[i]=='START':
        start=line1[i+1]
        program_name=line1[i-1]
print("H^",program_name,"^",start,"^",hex((len(program)-3)*3)[2:])
for i in program[1:]:
    lines=i.split()
    for j in range(len(lines)):
        if lines[j] in opcode.keys():
            if lines[j+1] in symtab.keys():
                objcode.append(opcode[lines[j]]+symtab[lines[j+1]])
                continue
print("T^",start,"^",hex(len(objcode)*3)[2:],end='')
for i in objcode:
    print("^",''.join(i),end='');
print()
print("E^",start)

----------------input.txt
    COPY START 1000
LDA ALPHA
STA BETA
LDA GAMMA
ALPHA RESW 1
BETA RESW 1
GAMMA RESW 1
----------------opcode.txt
STA 23
LDA 00
----------------symtab.txt
ALPHA 1006
BETA 1009
GAMMA 100C
    """
    print(s)

def predictive_parser():
    s="""
    table = open("table.txt","r").read()
table = table.split("\n")
T = {'E':0,'S':1,'T':2,'R':3,'F':4}
NT = {'i':0,'+':1,'*':2,'(':3,')':4,'$':5}

p_table = []
for i in table:
    p_table.append(i.split())

#s=i+i*i$
s = input("Enter the input String:")
stack = '$E'
print("\nSTACK","\tINPUT","\t\tOUTPUT")
print(stack,"\t",s)
while(stack[-1]!=s[-1]):

    if stack[-1]==s[0]: #If String 'e' is same as top of stack
        stack = stack[:-1] #Pop same terminals
        s=s[1:]

        print(stack,'\t',s)

    pos = p_table[T[stack[-1]]][NT[s[0]]]
    t = pos[3:]
    stack = stack[:-1]+t[::-1]
    print(stack,'\t',s,'\t\t',pos)

if(stack=='$' and s=='$'):
    print("The String is Parsed Successfully")

    -------------------table.txt
    E->TS - - E->TS - -
- S->+TS - - S-> S->
T->FR - - T->FR - -
- R-> R->*FR - R-> R->
F->i - - F->F(E) - -
    """
    print(s)

