#include <iostream>
#include <math.h>
using namespace std;
//sqrt(delta) pt x^2+5x+2
int main()
{
	int a = 1, b = 5, c = 2, x1, x2;
	int x;
	_asm
	{
		push c;
		push b;
		push a;
		mov eax, b;
		imul[esp + 4];
		mov ebx, eax;
		mov eax, 4;
		imul[esp];
		//mov eax, edx;
		imul[esp + 8];
		sub ebx, eax;
		add esp, 12;
		mov ecx, 1;
		mov eax, 1;
	_for:
		cmp eax, ebx;
		jae endfor;
		mov eax, ecx;
		mul ecx;
		inc ecx;
		jmp _for;
	endfor:
		sub ecx, 2;
		mov x, ecx;
	}
	cout << x;
}