
#include<iostream>

using namespace std;

char GetMaxConsecutiveCharacter(char s[]);

int main()
{
	char s[] = "aa22aahhkkxxxwwii9";
	char c = GetMaxConsecutiveCharacter(s);
	cout << s << endl;
	cout << c << '\n';

	return 0;
}

char GetMaxConsecutiveCharacter(char s[])
{
	char c; int n;
	_asm
	{
		mov ebx, s;
		mov ecx, 0;

	_startWhile:
		cmp byte ptr[ebx], 0;
		je _endWhile;

		inc ebx;
		inc ecx;
		jmp _startWhile;

	_endWhile:
		mov n, ecx;
	}
	n--;
	_asm
	{
		mov ebx, s  // sir
		mov ecx, 1 //maxim
		mov esi, 1 //contor curent
		mov edi, 0 // i

		cmp n, 0  //doar un caracter
		je end_if3

		start_for :
		cmp edi, n
			jge end_for

			mov dh, [ebx + edi]
			inc edi
			mov dl, [ebx + edi]
			cmp dh, dl

			jne end_if1
			inc esi
			cmp esi, ecx

			jl end_if2
			mov ecx, esi
			mov al, dh

			jmp end_if2
			end_if1 :
		mov esi, 1
			end_if2 :

			jmp start_for

			end_for :
		mov c, al
			jmp aici
			end_if3 :
		mov al, [ebx]
			mov c, al

			aici :
	}
	return c;

}