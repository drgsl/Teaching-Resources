//MAXIMUL DINTRE DOUA NUMERE
#include<iostream>
using namespace std;
int maxim(int a, int b)
{
	_asm
	{
		mov eax, [ebp + 8];
		mov ebx, [ebp + 12];
		cmp eax, ebx;
		jge maximA
			mov esi, ebx;
		jmp sfarsit
			maximA :
		mov esi, eax;
	sfarsit:
		mov eax, esi;
	}
}
int main()
{
	int a, b, max;
	cin >> a >> b;
	_asm
	{
		mov eax, a;
		mov ebx, b;
		push ebx;
		push eax;
		call maxim;
		add esp, 8;
		mov max, eax;
	}
	cout << max;
	return 0;
}