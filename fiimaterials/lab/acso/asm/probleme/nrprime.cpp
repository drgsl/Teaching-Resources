#include<iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	bool result;

	_asm {

		mov ecx, n
		cmp ecx, 1
		jle _ReturnNonprime


		cmp ecx, 2
		je _ReturnPrime


		mov edx, 0
		mov eax, ecx
		mov ebx, 2
		div ebx
		cmp edx, 0
		je _ReturnNonprime


		mov ebx, 3


		_While_start:
		mov eax, ebx
			mul ebx
			cmp eax, ecx
			ja _ReturnPrime


			mov edx, 0
			mov eax, ecx
			div ebx
			cmp edx, 0
			je _ReturnNonprime


			add ebx, 2
			jmp _While_start

			_ReturnPrime :
		mov result, 1
			jmp _End
			_ReturnNonprime :
		mov result, 0
			_End :
	}

	cout << result << '\n';

	return 0;
}