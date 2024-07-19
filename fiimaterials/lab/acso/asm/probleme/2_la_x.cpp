#include<iostream>
using namespace std;
int doiLaPutereaX(int x)
{
	_asm
	{
		mov eax, 1;
		mov ecx, 2;
		mov ebx, 0;//contorul;
	for_:
		cmp ebx, [ebp + 8];
		jge sfarsit;
		mul ecx;
		add ebx, 1;
		jmp for_;
	sfarsit:
	}
}
int main()
{
	int x, p;
	cin >> x;
	_asm
	{
		mov eax, x;
		push eax;
		call doiLaPutereaX;
		add esp, 4;
		mov p, eax;
	}
	cout << p;
}