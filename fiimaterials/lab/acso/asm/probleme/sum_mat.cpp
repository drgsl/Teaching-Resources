
#include <iostream>
using namespace std;
int sumaMatrici(int*, int size1, int*, int size2)
{
	_asm
	{
		mov ebx, [ebp + 8];//matricea A
		mov ecx, [ebp + 16];//matricea B
		mov eax, [ebp + 12];
		mov edx, eax;
		mul edx;
		mov edx, 0;//contorul

	for1:
		cmp edx, eax;
		jge sfarsit;
		mov edi, [ebx + 4 * edx];
		add edi, [ecx + 4 * edx];
		mov[ebx + 4 * edx], edi;
		inc edx;
		jmp for1;
	sfarsit:
	}
}
int main()
{
	int n = 3;
	int A[3][3] = { 1,0,1,0,1,0, 1,0,1 };
	int B[3][3] = { 2,1,2,1,2,1, 2,1,2 };
	_asm
	{
		mov eax, n;
		push eax;
		lea eax, B;
		push eax;
		mov eax, n;
		push eax;
		lea eax, A;
		push eax;
		call sumaMatrici;
		add esp, 16;
	}
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
			cout << A[i][j] << " ";
		cout << endl;
	}
	return 0;
}
