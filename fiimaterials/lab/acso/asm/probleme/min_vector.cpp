// AsmMinVectr.cpp : Defines the entry point for the console application.
//


#include<iostream>
using namespace std;
int a[20], n, sol;
int main()
{
	cin >> n;
	for (int i = 1;i <= n;++i) cin >> a[i - 1];
	_asm {
		lea ecx, a;
		mov ebx, [ecx];
		dec n;
		add ecx, 4;
	_while:
		cmp ebx, [ecx];
		jg _change;
	_ret:
		dec n;
		add ecx, 4;
		cmp n, 0;
		jne _while;
		jmp _fin;
	_change:
		mov ebx, [ecx];
		jmp _ret;
	_fin:
		mov sol, ebx;
	}
	cout << sol << '\n';
	return 0;
}

