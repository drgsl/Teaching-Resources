#include<iostream>
using namespace std;
int test(int x)//verifica daca nr e puterea a lui 2;
{
	_asm
	{
		mov eax, [ebp + 8];//x
	while_:
		cmp eax, 1;
		je sfarsit_while;
		mov edx, 0;
		mov ecx, 2;
		div ecx;
		cmp edx, 0;
		jne not_ok;
		jmp while_;
	not_ok:
		mov eax, 0;//nu este putere
		jmp sfarsit_test;
	sfarsit_while:
		mov eax, 1;//este putere;
		jmp sfarsit_test
			sfarsit_test :
	}
}
int main()
{
	int n;
	cin >> n;
	cout << test(n);
	return 0;
}