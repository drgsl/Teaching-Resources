// ASM_MAXIMUL DINTRE 3 NUMERE.cpp : Defines the entry point for the console application.
//

#include<iostream>
using namespace std;


int main()
{
	int a = 70, b = 69, c = 30;
	_asm {
		mov eax, a
		mov ebx, b
		mov ecx, c

		_if1 :
		cmp eax, ebx
			ja _if2
			mov eax, ebx

			_if2 :
		cmp eax, ecx
			ja _end
			mov eax, ecx

			_end :
		mov a, eax
	}

	cout << a;
	return 0;
}

