#include<iostream>
using namespace std;
int sumaCifrePare(int n)
{
	_asm
	{
		mov eax, [ebp + 8];//n;
		mov esi, 0;//suma
	while_:
		cmp eax, 0;
		je sfarsit;
		mov edx, 0;
		mov ecx, 10;
		div ecx;
		mov ebx, eax;//copia lui eax;
		mov edi, edx;//ultima cidra
		mov eax, edx;//ultima cifra
		mov edx, 0;
		mov ecx, 2;
		div ecx;
		cmp edx, 0;
		jg impar;
		add esi, edi;
	impar:
		mov eax, ebx;//revin la eax;
		jmp while_;
	sfarsit:
		mov eax, esi;
	}
}
int main()
{
	int nr, s;
	cin >> nr;
	_asm
	{
		mov eax, nr;
		push eax;
		call sumaCifrePare;
		add esp, 4;
		mov s, eax;
	}
	cout << s;
	return 0;
}