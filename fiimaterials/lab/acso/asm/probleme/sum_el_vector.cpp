#include <iostream>
using namespace std;
//suma elementelor unui vector prin functie
int suma_el(int v[], int n)
{
	_asm
	{
		mov ebx, [ebp + 8]
		mov ecx, 0
		mov eax, 0
		start_for:
		cmp ecx, [ebp + 12]
			jge exit_for
			mov edx, dword ptr[ebx + ecx * 4]
			add eax, edx
			inc ecx
			jmp start_for
			exit_for :
	}
}
int main()
{
	int v[100];
	int n, s, i;
	cin >> n;
	for (i = 0;i < n;i++)
	{
		cin >> v[i];
	}
	_asm
	{
		push n
		lea ebx, v
		push ebx
		call suma_el
		add esp, 8
		mov s, eax
	}
	//s=suma_el(v,n);

	cout << s;
	return 0;
}