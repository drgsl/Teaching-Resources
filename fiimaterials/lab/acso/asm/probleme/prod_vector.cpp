// ASMProdVector.cpp : Defines the entry point for the console application.
//


#include<iostream>
using namespace std;
int a[20], n, prod = 1, ok, nn;
int main()
{
	cin >> n; nn = n;
	for (int i = 0;i < n;++i) cin >> a[i];
	_asm { //cu suma
		lea eax, a;
		mov ecx, 0; //termenul de inmultit
	_while:
		dec n;
		mov ecx, [eax];
		cmp ecx, 0;
		jz _case0;
		mov ebx, prod;
		mov edx, 0;
	_mul:
		add edx, prod;
		dec ecx;
		cmp ecx, 0;
		jne _mul;
		///////
		mov prod, edx;
		add eax, 4;
		cmp n, 0;
		jne _while;
		jmp _fin;
	_case0:
		mov ok, 1;
	_fin:
		;
	}


	if (ok == 1) cout << 0 << '\n';
	else cout << prod << '\n';
	n = nn;
	_asm {//cu mul
		lea ecx, a;
		mov prod, 1;
		mov eax, 1;
	_while_:
		mov ebx, [ecx];
		mul ebx;
		add ecx, 4;
		dec n;
		cmp n, 0;
		jne _while_;
		mov prod, eax;
	}
	cout << prod << '\n';
	return 0;
}
