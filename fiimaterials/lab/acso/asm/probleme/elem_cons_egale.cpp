// ASM_Matrice78.cpp : Defines the entry point for the console application.
//Fiind dat un vector v cu n elemente numere intregi , sa se afiseze de cate ori gasim doua elemente consecutive egale intre ele.  

#include<iostream>
using namespace std;
void f(int* a, int n)
{
	_asm {
		mov ebx, 0
		mov ecx, [ebp + 8]
		mov edx, 0
		_while:
		cmp ebx, [ebp + 12]
			je _endwhile

			mov edi, [ecx + 4 * ebx]
			cmp edi, [ecx + 4 * ebx + 4]
			jne _nope

			inc edx
			_nope :
		inc ebx
			jmp _while
			_endwhile :
		mov eax, edx
	}
}

int main()
{
	int a[9] = { 1, 1, 1, 1, 1, 1, 1, 1, 1 };
	int n = 9, answer;
	_asm {
		push n
		lea eax, a
		push eax
		call f
		add esp, 8
		mov answer, eax
	}
	cout << answer;
	return 0;
}

