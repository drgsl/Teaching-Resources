
#include <iostream>
using namespace std;
#define MAXSIZE 7
int a[MAXSIZE][MAXSIZE];

void matrice(int*, int)
{
	_asm
	{
		mov ebx, [ebp + 8];
		mov eax, [ebp + 12];
		mov ecx, eax;
		mul ecx;
		mov ecx, 0;//i;

		mov esi, [ebp + 12];
		inc esi;
	for1:
		cmp ecx, eax;
		je sfarsit;
		mov[ebx + 4 * ecx], 0;
		inc ecx;
		jmp for1;
	sfarsit:
		mov ecx, 0;
	for2:
		cmp ecx, eax;
		jge sfarsit2;
		mov[ebx + 4 * ecx], 1;
		add ecx, esi;
		jmp for2;
	sfarsit2:


	}
}
int main()
{
	int n = MAXSIZE;
	//int a[MAXSIZE][MAXSIZE];
	_asm
	{
		mov eax, n;
		push eax;
		lea eax, a;
		push eax;
		call matrice;
		add esp, 8;
	}
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
	return 0;
}