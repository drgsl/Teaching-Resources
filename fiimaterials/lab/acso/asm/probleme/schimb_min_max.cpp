// SchimbMinCuMax_ArrayTrainingAdrese.cpp : Defines the entry point for the console application.
//


#include<iostream>
using namespace std;
int v[52], n;
void change(int n, int* v) {
	int i = 0;
	n *= 4;
	int* p1, * p2;
	_asm {
		mov eax, v;
		mov p1, eax;
		mov p2, eax;
		mov ecx, [eax];
		mov eax, ecx; //min
		mov ebx, ecx;//max
	_parc:
		mov ecx, i;
		mov edx, v;
		add edx, ecx;
		cmp eax, [edx];
		jg _changeMin;
	_ret:
		mov ecx, i;
		cmp ebx, [edx];
		jl _changeMax;
	_ret2:
		add i, 4;
		mov ecx, n;
		cmp i, ecx;
		jne _parc;
		jmp _fin;
	_changeMin:
		mov eax, [edx];
		mov p1, edx;
		jmp _ret;
	_changeMax:
		mov ebx, [edx];
		mov p2, edx;
		jmp _ret2;
	_fin:
		mov edx, p1;
		mov[edx], ebx;
		mov edx, p2;
		mov[edx], eax;
	}
}
int main()
{
	cin >> n;
	for (int i = 0; i < n; ++i)cin >> v[i];
	change(n, v);
	for (int i = 0; i < n; ++i)cout << v[i] << ' ';

	return 0;
}

