// asm_impartire.cpp : Defines the entry point for the console application.
//
#include<iostream>
using namespace std;

int main()
{
	short cat, rest;
	_asm {
		mov ax, 300
		mov dx, 0
		mov cx, 70
		div cx

		mov cat, ax
		mov rest, dx

	}
	cout << cat << endl << rest;
	return 0;
}