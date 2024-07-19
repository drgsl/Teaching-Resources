/*
* Filename: sortare_cu-lacate.c
*
* A doua variantă de sortare a unui fișier, completă, în sensul că folosim lacăte pentru acces exclusiv la secțiunea de fișier modificată la un moment dat.
* Lacătele sunt puse pe secțiuni minimale din fișier (i.e., se blochează din fișier doar atât cât este necesar pentru a face inversiunea unei perechi de întregi)
* și sunt menținute pe durate minimale (i.e., doar atât timp cât este nevoie pentru a face inversiunea unei perechi de întregi).
*
* Ca urmare, soluția este corectă -- în sensul că va funcționa corect întotdeauna, producând rezultatele corecte, chiar și atunci când se lansează în execuție
* simultană mai multe instanțe ale programului (i.e., un job de tip SPMD), pentru a sorta concurent un același fișier de date.
* Cu alte cuvinte, nu se vor obține rezultate incorecte, datorită fenomenelor de data race !!!
*/

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

void bubble_sort_cu_blocaje(int filedescr);

int main(int argc,char *argv[])
{
	int fd;
	if(argc < 2)
	{
		printf("Usage: %s datafile\n", argv[0]);  exit(1);
	}

	if(-1 == (fd = open(argv[1],O_RDWR)))
	{
		perror("Eroare la deschiderea fisierului de date");  exit(2);
	}
    
	bubble_sort_cu_blocaje(fd);

	close(fd);

	fprintf(stderr, "Notificare: [PID: %d] Am terminat (contributia mea la) sortarea fisierului %s !\n", getpid(), argv[1]);
	return 0;
}


void bubble_sort_cu_blocaje(int filedescr)
{
	int rcod1,rcod2;
	int numar1,numar2;
	int numar1_recitit,numar2_recitit;

	struct flock lacat_blocaj, lacat_deblocaj;

	lacat_blocaj.l_type   = F_WRLCK;
	lacat_blocaj.l_whence = SEEK_CUR;
	lacat_blocaj.l_start  = 0;
	lacat_blocaj.l_len    = 2*sizeof(int);

	lacat_deblocaj.l_type   = F_UNLCK;
	lacat_deblocaj.l_whence = SEEK_CUR;
	lacat_deblocaj.l_start  = -2*sizeof(int);
	lacat_deblocaj.l_len    = 2*sizeof(int);

	int modificare = 1;

	/* Bucla while în care facem parcurgeri repetate ale fișierului. */
	while(modificare)
	{
		modificare = 0; /* va fi setat dacă se face măcar o inversiune în timpul parcurgerii curente */

		/* Bucla while pentru o singură parcurgere a fișierului. */
		while(1)
		{
			rcod1 = read(filedescr, &numar1, sizeof(int));
			if(rcod1 == 0) break; // am ajuns la EOF
			if(rcod1 ==-1)
			{
				perror("Eroare la citirea primului numar dintr-o pereche");  exit(3);
			}	

			rcod2 = read(filedescr, &numar2, sizeof(int));
			if(rcod2 == 0) break; // am ajuns la EOF
			if(rcod2 ==-1)
			{
				perror("Eroare la citirea celui de-al doileai numar dintr-o pereche");  exit(4);
			}	

			/* Dacă este inversiune, inter-schimbăm cele două numere în fișier. */ 
			if(numar1 > numar2)
			{
				/*  Observație: procedăm similar ca la versiunea demo access_v4.c de la curs:
						întâi punem blocajul, apoi verificăm dacă niciunul dintre cele două numere nu a fost cumva schimbat între timp
						de o altă instanță de execuție a programului, și doar în caz afirmativ facem rescrierea în fișier!
					Remarcă: de fapt, condiția de mai sus poate fi relaxată: chiar dacă între timp a fost schimbat vreunul dintre cele două numere,
						tot putem inversa cele două numere (mai exact, valorile noi ale acestora, recitite după punerea lacătului) dacă este
						cazul să facem inversiune, i.e. dacă nu sunt deja ordonate crescător.  */

				/* Ne întoarcem înapoi cu 2 întregi pentru a face verificarea și apoi, eventual, rescrierea. */
				if(-1 == lseek(filedescr, -2*sizeof(int), SEEK_CUR))
				{
					perror("Eroare (1) la repozitionarea inapoi in fisier");  exit(5);
				}

				/* Punem blocajul pe porțiunea din fișier ce conținea cele două numere abia citite. */
				if(-1 == fcntl(filedescr, F_SETLKW, &lacat_blocaj))
				{
					perror("Eroare la blocaj");  exit(10);
				}
	
				/* Recitim cele 2 numere. */
				if(-1 == read(filedescr, &numar1_recitit, sizeof(int)))
				{
					perror("Eroare la recitirea primului numar dintr-o pereche");  exit(11);
				}	

				if(-1 == read(filedescr, &numar2_recitit, sizeof(int)))
				{
					perror("Eroare la recitirea celui de-al doilea numar dintr-o pereche");  exit(12);
				}	
			
				/* Dacă numerele au rămas neschimbate, atunci efectuăm rescrierea/inversiunea:
					    if( (numar1 == numar1_recitit) && (numar2 == numar2_recitit) )
						...				*/
				/* Sau, și mai eficient, conform celor spuse mai sus: chiar dacă numerele nu au rămas neschimbate,
				   dacă este cazul efectuăm inversiunea valorilor recitite după punerea blocajului:  */
				if(numar1_recitit > numar2_recitit)
				{
					modificare = 1;

					/* Ne întoarcem înapoi cu 2 întregi pentru a face rescrierea. */
					if(-1 == lseek(filedescr, -2*sizeof(int), SEEK_CUR))
					{
						perror("Eroare (4) la repozitionarea inapoi in fisier");  exit(13);
					}

					if(-1 == write(filedescr, &numar2_recitit, sizeof(int)))
					{
						perror("Eroare la rescrierea primului numar dintr-o pereche");  exit(14);
					}
			
					if(-1 == write(filedescr, &numar1_recitit, sizeof(int)))
					{
						perror("Eroare la rescrierea celui de-al doilea numar dintr-o pereche");  exit(15);
					}
				}
			
				/* Indiferent dacă am făcut sau nu inversiune, acum trebuie deblocată porțiunea din fișier pe care
				   am blocat-o mai sus (i.e., scoatem blocajul de pe porțiunea ce conținea cele două numere).  */
				if(-1 == fcntl(filedescr, F_SETLKW, &lacat_deblocaj))
				{
					perror("Eroare la deblocaj");  exit(16);
				}
			}
		
			/* Pregătim următoarea iterație: primul număr din noua pereche este cel de-al doilea număr din perechea precedentă. */
			if(-1 == lseek(filedescr, -sizeof(int), SEEK_CUR))
			{
				perror("Eroare (2) la repozitionarea inapoi in fisier");  exit(8);
			}
		}/* Sfârșitul buclei while pentru o singură parcurgere a fișierului. */

		/* Pregătim următoarea parcurgere: ne repoziționăm la începutul fișierului. */
		if(-1 == lseek(filedescr, 0L, SEEK_SET))
		{
			perror("Eroare (3) la repozitionarea inapoi in fisier");  exit(9);
		}

    }/* Sfârșitul buclei while de parcurgeri repetate ale fișierului. */

}
