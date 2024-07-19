#include<iostream>
using namespace std;
void sortare(int*, int)
{
	_asm
	{
		mov eax, [ebp + 8];//vectorul
		mov ebx, [ebp + 12];//nr de elem
		mov ecx, 0;//primul contor;
		mov edx, 0;//al doilea contor;
	first_for:
		cmp ecx, ebx;
		jge sfarsit1;
		mov edx, ecx;
		inc edx;//edx=ecx+1;
	second_for:
		cmp edx, ebx;
		jge sfarsit2;
		mov edi, [eax + ecx * 4];//v[i];
		mov esi, [eax + edx * 4];//v[i+1];
		cmp edi, esi;
		jle no_swap;
		mov[eax + edx * 4], edi;
		mov[eax + ecx * 4], esi;
	no_swap:
		inc edx;
		jmp second_for;
	sfarsit2:
		inc ecx;
		jmp first_for;
	sfarsit1:
	}
}
int main()
{
	int v[] = { 6, 8, 9, 1, 2, 5, 3, 10 };
	int n = 8;
	_asm
	{
		lea eax, v;
		mov ebx, n;
		push ebx;
		push eax;
		call sortare;
		add esp, 8;
	}
	for (int i = 0; i < n; i++)
		cout << v[i] << " ";
	return 0;
}