#include<iostream>
using namespace std;
int nrCaractere(char* sir, int c, int size)
{
	_asm
	{
		mov eax, [ebp + 8];//sir;
		mov ebx, [ebp + 12];//c
		mov ecx, [ebp + 16];//size;
		mov edx, 0;//i;
		mov esi, 0;//nr caractere;
	for_:
		cmp edx, ecx;
		jge sfarsit;
		movzx edi, [eax + edx];
		cmp edi, ebx;
		jne no_ok;
		inc esi;//nr++;
	no_ok:
		inc edx;//i++;
		jmp for_;
	sfarsit:
		mov eax, esi;
	}
}
int main()
{
	char c[] = "ana are mere";
	int size_sir = 12;
	char to_find = 'r';
	int result;
	_asm
	{
		lea eax, c;
		mov ebx, size_sir;
		movzx ecx, to_find;
		push ebx;
		push ecx;
		push eax;
		call nrCaractere;
		add esp, 12;
		mov result, eax;

	}
	cout << result;
	return 0;

}