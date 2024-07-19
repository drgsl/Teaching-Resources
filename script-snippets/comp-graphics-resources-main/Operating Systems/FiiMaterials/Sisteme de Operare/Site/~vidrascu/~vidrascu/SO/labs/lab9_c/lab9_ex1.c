/*
  Program: șablonul de creare a N fii ai procesului curent.
*/
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int N=0, i;
    pid_t pid;

    /* Obținerea parametrului de intrare N. */
    if(argc < 2)
    {
        printf("Introduceti numarul de fii: ");
        while( (1 != scanf("%d", &N)) && (N < 1) ) { fprintf(stderr,"\nEroare: nu ati introdus un numar intreg strict pozitiv! Incercati din nou..."); }
    }
    else
    {
        if(1 != sscanf(argv[1],"%d", &N)) { fprintf(stderr,"Eroare: nu ati specificat un numar intreg strict pozitiv!\n");  exit(1); }
    }

    printf("Sunt procesul initial cu PID-ul: %d, iar parintele meu este procesul cu PID-ul: %d.\n", getpid(), getppid() );

    /* Bucla de producere a celor N procese fii. */
    for(i = 1; i <= N; i++)
    {
        if(-1 == (pid=fork()) )
        {
            perror("Eroare la fork");  exit(2);
        }
        if(0 == pid)
        {
            printf("Sunt procesul fiu %d, avand PID-ul: %d, iar parintele meu este procesul cu PID-ul: %d.\n", i, getpid(), getppid() );
            return i;  // Important: fiul nu trebuie să reia execuția buclei for, ca să nu creeze la rândul lui alte procese fii !
        }
    }

    /* Așteptarea terminării tuturor celor N fii. */
    for(i = 1; i<= N; i++)  // Procesul inițial va aștepta terminarea celor N fii; altfel, câteodată (i.e., nu neapărat la toate execuțiile)
        wait(NULL);         // este posibil ca unii fii să apară ca fiind orfani (i.e., având drept părinte procesul cu PID-ul 1).

    return 0;
}