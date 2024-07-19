#include<iostream>
using namespace std;
int transf(const char*)
{
	_asm
	{
		mov eax, [ebp + 8];//char
		mov ecx, 0;//contorul
	while_:

		cmp[eax + ecx], 0;
		je sfarsit;
		mov bh, 0;
		mov bh, 'a';
		cmp[eax + ecx], bh;
		jb not_mica;
		mov bh, 0;
		mov bh, 'z';
		cmp[eax + ecx], bh;
		jg not_mica;
		mov edx, [eax + ecx];
		sub edx, 32;
		mov[eax + ecx], edx;
	not_mica:
		inc ecx;
		jmp while_;
	sfarsit:

	}
}
int main()
{
	char c[] = "anatalala";
	_asm
	{
		lea eax, c;
		push eax;
		call transf;
		add esp, 4;

	}
	cout << c;
	return 0;

}