
#include <iostream>
using namespace std;
struct p
{
	int x, y;
}a, b, c, d;

int main()
{
	a.x = 3; a.y = 3;
	b.x = 6; b.y = 6;
	c.x = 3; c.y = 9;
	d.x = 0; d.y = 6;
	int x;
	_asm
	{
		jmp acolo
		distanta :
		push ebp
			mov ebp, esp
			mov esi, [ebp + 8]
			mov eax, [esi]
			mov ebx, [esi + 4]
			mov esi, [ebp + 12]
			mov ecx, [esi]
			mov edx, [esi + 4]
			sub eax, ecx
			sub ebx, edx
			mov edx, 0
			mul eax
			mov ecx, eax
			mov edx, 0
			mov eax, ebx
			mul eax
			mov ebx, eax
			add  ecx, ebx
			mov eax, ecx
			pop ebp
			ret
			acolo :

		lea eax, a
			lea ebx, b
			push eax
			push ebx
			call distanta
			add esp, 8
			push eax

			lea eax, b
			lea ebx, c
			push eax
			push ebx
			call distanta
			add esp, 8
			cmp eax, [esp]
			jne rau

			lea eax, c
			lea ebx, d
			push eax
			push ebx
			call distanta
			add esp, 8
			cmp eax, [esp]
			jne rau

			lea eax, d
			lea ebx, a
			push eax
			push ebx
			call distanta
			add esp, 8
			cmp eax, [esp]
			jne rau
			pop eax

			lea eax, c
			lea ebx, a
			push eax
			push ebx
			call distanta
			add esp, 8
			push eax


			lea eax, d
			lea ebx, b
			push eax
			push ebx
			call distanta
			add esp, 8
			cmp eax, [esp]
			jne rau

			jne rau


			bun :
		mov eax, 1
			mov x, eax
			jmp aici
			rau :
		mov eax, 0
			mov x, eax
			aici :
		pop eax

	}
	cout << x;
	return 0;
}
