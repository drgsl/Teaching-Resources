

#include <iostream>
using namespace std;

int canvas[10][10];




int main(int argc, char const *argv[])
{
    // for (int i = 0; i < 10; i++)
    // {
    //     for (int j = 0; j < 10; j++)
    //     {
    //         cout << canvas[i][j] << " "; 
    //     }
    //     cout << endl;
    // }
    
    
    // canvas[5][5] = 1;

    canvas[0][0] = 1;
    canvas[0][1] = 1;
    canvas[0][2] = 1;
    canvas[0][3] = 1;
    canvas[0][4] = 1;
    canvas[0][5] = 1;
    canvas[0][6] = 1;
    canvas[0][7] = 1;
    canvas[0][8] = 1;
    canvas[0][9] = 1;
    

    for (int i = 0; i < 10; i++)
    {
        canvas[1][i] = 2;
    }

    for (int j = 0; j < 10; j++)
    {
        canvas[j][0] = 3;
    }


    // each line has a different number
    for (int i = 0; i < 10; i++)
    {
        canvas[i][i] = i;
    }

    // secondary diagonal
    for (int i = 0; i < 10; i++)
    {
        canvas[i][9-i] = 9-i;
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if(i == j)
            {
                canvas[i][j] = 1;
            }
            else
            {
                canvas[i][j] = 0;
            }

            //secondary diagonal
            if(i+j == 9)
            {
                canvas[i][j] = 2;
            }
        }
        
    }
    
    
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            cout << canvas[i][j] << " "; 
        }
        cout << endl;
    }

    return 0;
}







