// AsmMaxVector.cpp : Defines the entry point for the console application.
//


#include<iostream>
using namespace std;
int a[20], n, sol;
int main()
{
	cin >> n;
	for (int i = 0;i < n;++i) cin >> a[i];
	_asm {
		lea ecx, a;
		mov ebx, [ecx];
		add ecx, 4;
		dec n;
	_while:
		cmp ebx, [ecx];
		jl _schimb;
	_ret:
		dec n;
		add ecx, 4;
		cmp n, 0;
		jne _while;
		jmp _fin;
	_schimb:
		mov ebx, [ecx];
		jmp _ret;
	_fin:
		mov sol, ebx;
	}
	cout << sol << '\n';
	return 0;
}

