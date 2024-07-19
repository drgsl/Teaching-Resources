#include<iostream>
using namespace std;
void swap(int *a, int *b)
{
	_asm
	{
		mov eax, [ebp + 8] //adresa lui a
		mov ecx, [eax]; //val lui a
		mov ebx, [ebp + 12];//adresa lui b
		mov edx, [ebx];//valoarea lui b;
		mov[eax], edx;//mutam la adresa lui a valoarea lui b
		mov[ebx], ecx;//mutam la adresa lui b valoarea lui a
	}
}

int main()
{
	int a, b,c,d;
	cin >> a >> b;
	swap(&a, &b);
	cout << a << " " << b;
	return 0;
}