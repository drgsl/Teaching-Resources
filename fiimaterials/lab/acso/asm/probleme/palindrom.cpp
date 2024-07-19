
#include <iostream>

using namespace std;
unsigned int n;
int palindrom(unsigned int) {
	unsigned int r, s;
	_asm {
		MOV EAX, n
		MOV EBX, 10
		MOV EDI, 10
		MOV ESI, 0
		_while:
		CMP EAX, 0
			JE _jos
			MOV EDX, 0
			DIV EBX
			MOV s, EDX
			MOV ECX, EAX
			MOV EAX, ESI
			MUL EDI
			MOV ESI, EAX
			ADD ESI, s
			MOV EAX, ECX
			JMP _while
			_jos :
		MOV r, ESI
			MOV EAX, n
			CMP r, EAX
			JE _palindrom
			MOV r, 0
			JMP _end
			_palindrom :
		MOV r, 1
			_end :
	}
	return r;
}

int main()
{
	cin >> n;
	cout << palindrom(n);
}
