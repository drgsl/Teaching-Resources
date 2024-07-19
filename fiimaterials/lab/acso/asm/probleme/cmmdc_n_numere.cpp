// Cmmdc_N_Numere.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;
int v[50], n;
int cmmdc(int* v, int n) {
	int a = 0, b = 0, retu = 0;
	_asm {
		mov ecx, v;
		mov eax, [ecx];
		mov a, eax;
	_for:
		add ecx, 4;
		mov ebx, [ecx];
		mov b, ebx;
		cmp b, 0;
		je _fin;
	_while:
		mov eax, 0;
		mov edx, 0;
		cdq;
		mov eax, a;
		div b;
		mov eax, b;
		mov a, eax;
		mov b, edx;
		cmp b, 0;
		jne _while;
		jmp _for;
	_fin:
	}

	return a;
}
int main()
{
	cin >> n;
	for (int i = 0; i < n; ++i) cin >> v[i];
	v[n] = 0;
	cout << cmmdc(v, n) << '\n';
	return 0;
}

