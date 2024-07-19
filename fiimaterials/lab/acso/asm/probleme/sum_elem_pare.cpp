//SUMA ELEMENTELOR PARE
#include<iostream>
using namespace std;
int suma(int*, int)
{
	_asm
	{
		mov ebx, [ebp + 8];
		mov esi, 0;//contor
		mov edi, 0;//suma
	etifor:
		mov eax, [ebx + 4 * esi];//elementul curent
		mov edx, 0;
		mov ecx, 2;
		div ecx;
		cmp edx, 0;
		jg impar;
		add edi, [ebx + 4 * esi];
	impar:
		add esi, 1;
		cmp esi, [ebp + 12];
		jl etifor;
		mov eax, edi;
	}
}
int main()
{
	int v[5] = { 2,1,2,3,6 }, n, i, s;
	n = 5;
	int* p = v;
	_asm
	{
		mov eax, p;
		mov edi, n;
		push edi;
		push eax;
		call suma;
		add esp, 8;
		mov s, eax;
	}
	cout << s;
	return 0;
}