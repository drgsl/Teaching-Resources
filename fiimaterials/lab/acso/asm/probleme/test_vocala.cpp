#include<iostream>
using namespace std;
int testVocala(char c)
{
	_asm
	{
		mov eax, [ebp + 8];
		mov ebx, 'a';
		cmp eax, ebx;
		je adev;

		mov ebx, 'e';
		cmp eax, ebx;
		je adev;

		mov ebx, 'i';
		cmp eax, ebx;
		je adev;

		mov ebx, 'o';
		cmp eax, ebx;
		je adev;

		mov ebx, 'u';
		cmp eax, ebx;
		je adev;

		mov eax, 0;
		jmp sfarsit;

	adev:
		mov eax, 1;
		jmp sfarsit;
	sfarsit:

	}
}
int main()
{
	char c='t';
	cout << testVocala(c);
	return 0;
}