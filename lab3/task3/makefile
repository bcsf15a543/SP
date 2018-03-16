myexe: myMathFunc.o myStrFunc.o myMain.o
	gcc myMathFunc.o myStrFunc.o myMain.o -o myexe
myMathFunc.o: myMathFunc.c myMath.h
	gcc -c myMathFunc.c
myStrFunc.o: myStrFunc.c myStr.h
	gcc -c myMathFunc.c
myMain.o: myMain.c myStr.h myMath.h
	gcc -c myMain.c


