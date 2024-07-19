#include<iostream>
using namespace std;
int maximMatrice(int*, int n, int m)
{
	_asm
	{
		mov ebx, [ebp + 8];
		mov eax, [ebp + 12];//nr linii
		mov ecx, [ebp + 16];//nr coloane
		mul ecx;//eax=n*m
		mov ecx, 0;//contor
		mov edi, [ebx + 4 * ecx];//edi=v[0]
		inc ecx;
	for_:
		cmp ecx, eax;
		je sfarsit;
		cmp[ebx + 4 * ecx], edi;
		jg maxim;
		inc ecx;
		jmp for_;

	maxim:
		mov edi, [ebx + 4 * ecx];
		inc ecx;
		jmp for_;
	sfarsit:
		mov eax, edi;

	}
}
int main()
{
	int v[] = { 1,2,3,4,5,6,10,8,9 };
	int n = 3, m = 3;
	int max;
	_asm
	{
		mov eax, m;
		push eax;
		mov eax, n;
		push eax;
		lea eax, v;
		push eax;
		call maximMatrice;
		add esp, 12;
		mov max, eax;
	}
	cout << max;
	return 0;

}