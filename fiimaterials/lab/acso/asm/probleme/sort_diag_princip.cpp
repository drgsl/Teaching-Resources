#include <iostream>
using namespace std;

void sortare(int a[][5])
{
	/*
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
*/
	int x;
	_asm {
		mov ebx, 0
		mov esi, 1
		mov ecx, a
		et1 : mov edi, 0
		mov esi, 1
		et4 : cmp esi, 5
		je et3
		mov eax, esi
		mov ebx, 5
		mul ebx
		add eax, esi
		mov ebx, [ecx + eax * 4]
		cmp ebx, [ecx + eax * 4 - 24]
		ja et2
		inc edi
		mov ebx, [ecx + eax * 4]
		mov edx, [ecx + eax * 4 - 24]
		mov[ecx + eax * 4], edx
		mov[ecx + eax * 4 - 24], ebx

		et2 : inc esi
		jmp et4
		et3 : cmp edi, 0
		jne et1
	}
	cout << endl;
	for (int i = 0;i < 5;i++) {
		for (int j = 0;j < 5;j++)
			cout << a[i][j] << " ";
		cout << endl;
	}

	
}


int main()
{
	int i, j;
	int a[5][5];
	for (i = 0;i < 5;i++)
		for (j = 0;j < 5;j++) {
			a[i][j] = 5 - j;
		}
	for (i = 0;i < 5;i++) {
		for (j = 0;j < 5;j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
	sortare(a);
	return 0;
}



