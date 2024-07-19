//1^2 + 2^2 + 3^2 +....+ x^2
#include<iostream>
using namespace std;
int f(int x)
{
	_asm
	{
		mov ebx, [ebp + 8];//x
		mov eax, 1;//i
		mov ecx, eax;
		mul ecx;//eax=eax*eax;
		mov esi, eax;//suma
	for_:
		cmp ecx, ebx;
		jge sfarsit;
		inc ecx;
		mov eax, ecx;
		mul ecx;
		add esi, eax;
		jmp for_;
	sfarsit:
		mov eax, esi;

	}
}
int main()
{
	int x, s;
	cin >> x;
	_asm
	{
		mov eax, x;
		push eax;
		call f;
		add esp, 4;
		mov s, eax;
	}
	cout << s;

}
