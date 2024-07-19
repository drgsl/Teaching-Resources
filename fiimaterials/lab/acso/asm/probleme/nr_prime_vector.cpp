// ASM_Numarul de prime dintr-un v.cpp : Defines the entry point for the console application.
//Sa se afiseze cate numere prime sunt intr-un vector.

#include<iostream>
using namespace std;
void f(int* a, int n)
{
	_asm {

		mov ecx, 0
		mov edi, 0
		_for:
		mov ebx, [ebp + 8]
			cmp ecx, [ebp + 12]
			jge _endfor

			mov esi, [ebx + ecx * 4]
			mov ebx, 2

			_while:
		cmp ebx, esi
			jge _endwhile

			mov eax, esi
			mov edx, 0
			div ebx

			cmp edx, 0
			je _end

			inc ebx
			jmp _while
			_endwhile :
		inc edi
			_end :
		inc ecx
			jmp _for
			_endfor :
		mov eax, edi
	}
}

int main()
{
	int a[10] = { 3, 5, 7, 11, 13, 17, 23, 29, 31, 36 };
	int n = 10, answer;
	_asm {
		push n
		lea ebx, a
		push ebx
		call f
		add esp, 8
		mov answer, eax
	}
	cout << answer;
	return 0;
}

