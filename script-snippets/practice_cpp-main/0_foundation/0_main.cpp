


#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    cout << "Hello World" << endl;

    // print cli arguments
    cout << "Received " << argc << " arguments" << endl;
    for (int i = 0; i < argc; i++)
    {
        cout << "argv[" << i << "]: " << argv[i] << endl;
    }

    return 0;
}


