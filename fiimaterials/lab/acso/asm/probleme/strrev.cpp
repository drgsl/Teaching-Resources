// ASM_Exercitiu Ketano.cpp : Defines the entry point for the console application.
//
#include<iostream>
using namespace std;
void f(char a[27])
{
	_asm {
		mov eax, [ebp + 8]
		mov ecx, 0

		_while1:
		cmp[eax + ecx], 0
			je _endwhile1

			inc ecx
			jmp _while1
			_endwhile1 :
		dec ecx

			mov edi, 0
			_while2 :
			cmp edi, ecx
			jge _endwhile2

			mov bl, [eax + ecx]
			mov dl, [eax + edi]

			mov[eax + edi], bl
			mov[eax + ecx], dl

			inc edi
			dec ecx
			jmp _while2
			_endwhile2 :
	}
}

int main()
{
	char a[27] = "restanta";
	_asm {
		lea ebx, a
		push ebx
		call f
		add esp, 4
	}
	cout << a;
	return 0;
}

