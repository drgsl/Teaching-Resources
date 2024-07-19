#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <cfloat>
#include <cstring>
// #include "glut.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <GL/glut.h>

using namespace std;

// dimensiunea ferestrei in pixeli
#define dim 300
#define NMAX 1000
#define DOM_SCAN 100

struct punct {
	int x, y;
};
punct puncte[NMAX];

struct muchie {
	int x1, x2, y1, y2;
};
muchie muchii[NMAX];

struct intersection {
	double ymax;
	double xmin;
	double slope;
};

struct edgeTable {
	int count;
	intersection intersections[NMAX];
};
edgeTable et[DOM_SCAN + 5], final_et[DOM_SCAN + 5], active_ssm;

int criteriu(intersection a, intersection b) {
	return (a.xmin < b.xmin);
}

unsigned char prevKey;

class GrilaCarteziana {
public:
	int n;
	int m;
	double cx;
	double cy;
	double epsilon;
	double distantaLinii;
	double distantaColoane;

	GrilaCarteziana(int n, int m, int cx, int cy) {
		this->n = n;
		this->m = m;
		this->cx = cy;
		this->cy = cx;
		cout << "MAI";
		this->epsilon = 0.1;
		this->CalculeazaDistantaIntreLinii();
		this->DrawBoard();
		glColor3f(1, 0, 0);
		WritePixel(0, 0, 30);
		glColor3f(1, 1, 1);

	}
	GrilaCarteziana() {
		this->n = 16;
		this->m = 16;
		this->cx = 0;
		this->cy = 0;
		this->epsilon = 0.1;
		this->CalculeazaDistantaIntreLinii();
		this->DrawBoard();
		glColor3f(1, 0, 0);
		WritePixel(cx, cy, 30);
		glColor3f(1, 1, 1);
	}

	void WritePixel(int coloana, int linie, int raza) {
		linie = linie + this->cy;
		coloana = coloana + this->cx;

		if (linie < 0 || linie >= this->m || coloana < 0 || coloana >= this->n) {
			return;
		}
		vector<pair<int, int>> listaPuncteCerc = getListaPuncteCerc(coloana, linie, raza);
		int i;
		int maxDimensionSize;
		if (n >= m) {
			maxDimensionSize = n;
		}
		else {
			maxDimensionSize = m;
		}

		double x_ecran = -1 + epsilon + (coloana)*distantaColoane;
		double y_ecran = -1 + epsilon + (linie)*distantaLinii;
		glBegin(GL_POLYGON);
		for (i = 0; i < listaPuncteCerc.size(); i++) {
			double punctCerc_x = x_ecran + ((double)listaPuncteCerc[i].first) / raza / ((float)maxDimensionSize * 1.5);
			double punctCerc_y = y_ecran + ((double)listaPuncteCerc[i].second) / raza / ((float)maxDimensionSize * 1.5);
			glVertex2d(punctCerc_x, punctCerc_y);
		}
		glEnd();
	}


	void CalculeazaDistantaIntreLinii() {
		int windowSizeX = glutGet(GLUT_WINDOW_X);
		int windowSizeY = glutGet(GLUT_WINDOW_Y);
		this->distantaLinii = (double)((2.0 - 2 * epsilon) / double(this->n - 1));
		this->distantaColoane = (double)((2.0 - 2 * epsilon) / double(this->m - 1));
	}

	void DrawBoard() {
		int i;
		int j;

		for (i = 1; i <= m; i++) {
			glBegin(GL_LINES);
			glVertex2d(-1 + epsilon + this->distantaColoane * (i - 1), 1 - epsilon);
			glVertex2d(-1 + epsilon + this->distantaColoane * (i - 1), -1 + epsilon);
			glEnd();
		}

		for (i = 1; i <= n; i++) {
			glBegin(GL_LINES);
			glVertex2d(-1 + epsilon, -1 + epsilon + this->distantaLinii * (i - 1));
			glVertex2d(1 - epsilon, -1 + epsilon + this->distantaLinii * (i - 1));
			glEnd();
		}
	}

	vector<pair<int, int>> getListaPuncteCerc(int coloana, int linie, int raza) {
		linie = linie + this->cx;
		coloana = coloana + this->cy;

		vector<pair<int, int>> listaPuncte;
		int x = 0;
		int y = raza;
		int d = 1 - raza;
		int de = 3;
		int dse = -2 * raza + 5;

		listaPuncte.push_back(make_pair(x, y));
		listaPuncte.push_back(make_pair(-x, y));
		listaPuncte.push_back(make_pair(x, -y));
		listaPuncte.push_back(make_pair(-x, -y));
		if (x != y) {
			listaPuncte.push_back(make_pair(y, x));
			listaPuncte.push_back(make_pair(-y, x));
			listaPuncte.push_back(make_pair(y, -x));
			listaPuncte.push_back(make_pair(-y, -x));
		}

		while (y > x) {
			if (d < 0) {
				d += 2 * x + 3;
				x++;
			}
			else {
				d += 2 * (x - y) + 5;
				x++;
				y--;
			}
			listaPuncte.push_back(make_pair(x, y));
			listaPuncte.push_back(make_pair(-x, y));
			listaPuncte.push_back(make_pair(x, -y));
			listaPuncte.push_back(make_pair(-x, -y));
			if (x != y) {
				listaPuncte.push_back(make_pair(y, x));
				listaPuncte.push_back(make_pair(-y, x));
				listaPuncte.push_back(make_pair(y, -x));
				listaPuncte.push_back(make_pair(-y, -x));
			}
		}
		return listaPuncte;
	}

	vector<pair<int, int>> getListaPuncteElipsa(int coloana, int linie, int a, int b) {
		linie = linie;
		coloana = coloana;

		vector<pair<int, int>> listaPuncte;

		int x = 0;
		int y = -b;
		int extremitati[100];
		int i;
		for (i = 0; i <= 99; i++) {
			extremitati[i] = 0;
		}
		double d = b * b * x * x + a * a * y * y - a * a * b * b;
		double deltaV, deltaNV, deltaN;

		extremitati[y + b + (linie - b)] = x + a + (coloana - a);
		listaPuncte.push_back(make_pair(x + a + (coloana - a), y + b + (linie - b)));

		printf("%f\n", d);

		while (x > -a && y < 0) {
			// V
			deltaV = -2 * b * b * x + b * b;
			deltaNV = -2 * b * b * x + b * b + 2 * a * a * y + a * a;
			deltaN = 2 * a * a * y + a * a;

			d += deltaV;
			if (d < 0) {
				x--;
				extremitati[y + b + (linie - b)] = x + a + (coloana - a);
			}
			else {
				d -= deltaV;
				d += deltaNV;
				if (d <= 0) {
					x--;
					y++;
					extremitati[y + b + (linie - b)] = x + a + (coloana - a);
				}
				else {
					d -= deltaNV;
					d += deltaN;
					y++;
					extremitati[y + b + (linie - b)] = x + a + (coloana - a);
				}
			}
			printf("%d %d\n", x, y);
			printf("%f\n", d);
			listaPuncte.push_back(make_pair(x + a + (coloana - a), y + b + (linie - b)));
		}
		for (i = linie - b; i <= linie; i++) {
			printf("%d ", extremitati[i]);
			for (int j = coloana; j >= extremitati[i]; j--) {
				listaPuncte.push_back(make_pair(j, i));
			}
		}

		return listaPuncte;
	}

	vector<pair<int, int>> getPuncteCercPrimulOctant(int coloana, int linie, int raza) {
		linie = linie + this->cx;
		coloana = coloana + this->cy;

		vector<pair<int, int>> listaPuncte;
		int x = raza;
		int y = 0;
		int d = 1 - raza;
		int dn = 3;
		int dnv = -2 * raza + 5;

		listaPuncte.push_back(make_pair(x, y));

		while (x > y) {
			if (d > 0) {
				d += dnv;
				dnv += 4;
				dn += 2;
				x -= 1;
				y += 1;
			}
			else {
				d += dn;
				dnv += 2;
				dn += 2;
				y += 1;
			}
			listaPuncte.push_back(make_pair(x, y));
		}
		return listaPuncte;
	}
};

class Desenare2D {

public:

	void WriteLine(GrilaCarteziana grilaCarteziana, int x0, int y0, int xn, int yn) {

		double x0_ecran = -1 + grilaCarteziana.epsilon + (x0 + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
		double y0_ecran = -1 + grilaCarteziana.epsilon + (y0 + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;
		double xn_ecran = -1 + grilaCarteziana.epsilon + (xn + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
		double yn_ecran = -1 + grilaCarteziana.epsilon + (yn + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

		glColor3f(1, 0, 0);
		glBegin(GL_LINES);
		glVertex2d(x0_ecran, y0_ecran);
		glVertex2d(xn_ecran, yn_ecran);
		glEnd();
		glColor3f(1, 1, 1);
	}

	void WriteCircle(GrilaCarteziana grilaCarteziana, double x, double y, double raza) {
		double x1;
		double x_prev;
		double y_prev;
		double x_curr = 0;
		double y_curr = sqrt(raza * raza - 0 * 0);
		x_curr = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
		y_curr = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

		glColor3f(1, 0, 0);
		glBegin(GL_LINES);
		glVertex2d(x_curr, y_curr);

		for (x1 = 0.01; x1 <= raza; x1 += 0.01) {
			x_curr = x1;
			y_curr = sqrt(raza * raza - x_curr * x_curr);

			x_curr = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
			y_curr = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

			if (x_curr >= -1 && x_curr <= 1 && y_curr >= -1 && y_curr <= 1) {
				glVertex2d(x_curr, y_curr);
				glVertex2d(x_curr, y_curr);
			}
		}
		glEnd();
		glColor3f(1, 1, 1);
	}

	void WriteElipsa(GrilaCarteziana grilaCarteziana, double x, double y, double a, double b) {

		glColor3f(1, 0, 0);
		glBegin(GL_LINES);

		double x_curr = 0;
		double y_curr = b;
		double x_curr_translatat = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
		double y_curr_translatat = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

		glVertex2d(x_curr_translatat, y_curr_translatat);

		for (x_curr = 0.01; x_curr <= a; x_curr += 0.01) {
			y_curr = sqrt((a * a * b * b - b * b * x_curr * x_curr) / (a * a));


			x_curr_translatat = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
			y_curr_translatat = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

			if (x_curr_translatat >= -1 && x_curr_translatat <= 1 && y_curr_translatat >= -1 && y_curr_translatat <= 1) {
				glVertex2d(x_curr_translatat, y_curr_translatat);
				glVertex2d(x_curr_translatat, y_curr_translatat);
			}
		}

		glEnd();
		glBegin(GL_LINES);
		glVertex2d(x_curr_translatat, y_curr_translatat);

		for (x_curr = a; x_curr >= 0; x_curr -= 0.01) {
			y_curr = -sqrt((a * a * b * b - b * b * x_curr * x_curr) / (a * a));


			x_curr_translatat = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
			y_curr_translatat = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

			if (x_curr_translatat >= -1 && x_curr_translatat <= 1 && y_curr_translatat >= -1 && y_curr_translatat <= 1) {
				glVertex2d(x_curr_translatat, y_curr_translatat);
				glVertex2d(x_curr_translatat, y_curr_translatat);
			}
		}

		glEnd();
		glBegin(GL_LINES);
		glVertex2d(x_curr_translatat, y_curr_translatat);

		for (x_curr = -0.01; x_curr >= -a; x_curr -= 0.01) {
			y_curr = -sqrt((a * a * b * b - b * b * x_curr * x_curr) / (a * a));


			x_curr_translatat = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
			y_curr_translatat = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

			if (x_curr_translatat >= -1 && x_curr_translatat <= 1 && y_curr_translatat >= -1 && y_curr_translatat <= 1) {
				glVertex2d(x_curr_translatat, y_curr_translatat);
				glVertex2d(x_curr_translatat, y_curr_translatat);
			}
		}

		glEnd();
		glBegin(GL_LINES);
		glVertex2d(x_curr_translatat, y_curr_translatat);

		for (x_curr = -a; x_curr <= 0; x_curr += 0.01) {
			y_curr = sqrt((a * a * b * b - b * b * x_curr * x_curr) / (a * a));


			x_curr_translatat = -1 + grilaCarteziana.epsilon + (x_curr + x + grilaCarteziana.cx) * grilaCarteziana.distantaColoane;
			y_curr_translatat = -1 + grilaCarteziana.epsilon + (y_curr + y + grilaCarteziana.cy) * grilaCarteziana.distantaLinii;

			if (x_curr_translatat >= -1 && x_curr_translatat <= 1 && y_curr_translatat >= -1 && y_curr_translatat <= 1) {
				glVertex2d(x_curr_translatat, y_curr_translatat);
				glVertex2d(x_curr_translatat, y_curr_translatat);
			}
		}

		glEnd();
		glColor3f(1, 1, 1);
	}

	void WritePrimulOctant(GrilaCarteziana grilaCarteziana, int x, int y, int raza, int flag) {
		x += grilaCarteziana.cx;
		y += grilaCarteziana.cy;
		vector<pair<int, int>> listaPuncte = grilaCarteziana.getPuncteCercPrimulOctant(x + raza, y, raza);

		drawPoints(grilaCarteziana, listaPuncte, flag);
	}

	void UmpleElipsa(GrilaCarteziana grilaCarteziana, int x, int y, double a, double b) {
		vector<pair<int, int>> listaPuncte = grilaCarteziana.getListaPuncteElipsa(x, y, a, b);

		drawPoints(grilaCarteziana, listaPuncte, 0);
	}

	void WriteLinePixels(GrilaCarteziana grilaCarteziana, int x0, int y0, int xn, int yn, int pattern_flag) {
		vector<pair<int, int>> puncteLinie;
		cout << x0 << " " << y0 << " " << xn << " " << yn << '\n';

		if (x0 > xn) {
			swap(x0, xn);
			swap(y0, yn);
		}
		cout << x0 << " " << y0 << " " << xn << " " << yn << '\n';
		// dy/dx <= 1 si yn>=y0
		cout << abs(xn - x0) << " " << abs(yn - y0) << '\n';
		if (yn >= y0 && abs(xn - x0) >= abs(yn - y0)) {
			cout << "Intru aici\n";
			int dx = xn - x0;
			int dy = abs(yn - y0);
			int d = 2 * dy - dx; //2a+b       a=dy, b=-dx
			int dE = 2 * dy; //2a
			int dNE = 2 * (dy - dx);//2(a+b)
			int x = x0;
			int y = y0;
			puncteLinie.push_back(make_pair(x, y));
			while (x < xn) {
				if (d <= 0) {
					d += dE;
					x++;
				}
				else {
					d += dNE;
					x++; y++;
				}
				puncteLinie.push_back(make_pair(x, y));
			}

			this->drawPoints(grilaCarteziana, puncteLinie, pattern_flag);
		}
		// dy/dx > 1 si yn>=y0
		else if (yn >= y0 && abs(xn - x0) < abs(yn - y0)) {
			cout << "Am intrat";
			int dx = xn - x0;
			int dy = yn - y0;
			//int d = 2 * dx - dy;
			int d = dy - 2 * dx;
			int dN = -2 * dx;
			int dNE = 2 * (dy - dx);
			int x = x0;
			int y = y0;
			puncteLinie.push_back(make_pair(x, y));
			while (y < yn) {
				if (d > 0) {
					d += dN;
					y++;
				}
				else {
					d += dNE;
					x++; y++;
				}
				puncteLinie.push_back(make_pair(x, y));
			}

			this->drawPoints(grilaCarteziana, puncteLinie, pattern_flag);
		}
		// dy/dx <= 1 si yn<=y0
		else if (yn <= y0 && abs(xn - x0) >= abs(yn - y0)) {
			int dx = xn - x0;
			int dy = yn - y0;
			int d = 2 * dy + dx;
			int dE = 2 * dy;
			int dSE = 2 * (dy + dx);
			int x = x0;
			int y = y0;
			puncteLinie.push_back(make_pair(x, y));
			while (x < xn) {
				if (d > 0) {
					d += dE;
					x++;
				}
				else {
					d += dSE;
					x++; y--;
				}
				puncteLinie.push_back(make_pair(x, y));
			}

			this->drawPoints(grilaCarteziana, puncteLinie, pattern_flag);
		}
		// dy/dx > 1 si yn < y0 
		else if (y0 > yn && abs(xn - x0) < abs(yn - y0)) {
			int dx = xn - x0;
			int dy = yn - y0;
			cout << "DY " << dy << '\n';
			int d = (dy + 2 * dx);
			cout << "D " << d << '\n';
			int dS = 2 * dx;
			int dSE = 2 * (dx + dy);
			cout << "DSE " << dSE << '\n';
			cout << "dS " << dS << '\n';
			int x = x0;
			int y = y0;
			puncteLinie.push_back(make_pair(x, y));
			while (y > yn) {
				if (d < 0) {
					d += dS;
					y--;
				}
				else {
					d += dSE;
					x++; y--;
				}
				puncteLinie.push_back(make_pair(x, y));
			}

			this->drawPoints(grilaCarteziana, puncteLinie, pattern_flag);

		}
	}

	void drawPoints(GrilaCarteziana grilaCarteziana, vector<pair<int, int>> points, int pattern_flag) {
		int i;
		for (i = 0; i < points.size(); i++) {
			/*
			...
			X-X
			...
			*/
			if (pattern_flag == 1) {
				grilaCarteziana.WritePixel(points[i].first - 1, points[i].second, 30);
				grilaCarteziana.WritePixel(points[i].first + 1, points[i].second, 30);
			}
			/*
			.X.
			.-.
			.X.
			*/
			else if (pattern_flag == 2) {
				grilaCarteziana.WritePixel(points[i].first, points[i].second - 1, 30);
				grilaCarteziana.WritePixel(points[i].first, points[i].second + 1, 30);
			}
			/*
			.X.
			X-X
			.X.
			*/
			else if (pattern_flag == 3) {
				grilaCarteziana.WritePixel(points[i].first, points[i].second - 1, 30);
				grilaCarteziana.WritePixel(points[i].first, points[i].second + 1, 30);
				grilaCarteziana.WritePixel(points[i].first - 1, points[i].second, 30);
				grilaCarteziana.WritePixel(points[i].first + 1, points[i].second, 30);
			}
			/*
			XXX
			X-X
			XXX
			*/
			else if (pattern_flag == 4) {
				grilaCarteziana.WritePixel(points[i].first - 1, points[i].second - 1, 30);
				grilaCarteziana.WritePixel(points[i].first, points[i].second - 1, 30);
				grilaCarteziana.WritePixel(points[i].first + 1, points[i].second - 1, 30);
				grilaCarteziana.WritePixel(points[i].first - 1, points[i].second, 30);
				grilaCarteziana.WritePixel(points[i].first + 1, points[i].second, 30);
				grilaCarteziana.WritePixel(points[i].first, points[i].second + 1, 30);
				grilaCarteziana.WritePixel(points[i].first - 1, points[i].second + 1, 30);
				grilaCarteziana.WritePixel(points[i].first + 1, points[i].second + 1, 30);
			}
			cout << points[i].first << " " << points[i].second << '\n';
			grilaCarteziana.WritePixel(points[i].first, points[i].second, 30);
		}
	}

	void umplerePoligon(GrilaCarteziana grilaCarteziana, const char* fileName) {
		int n, i, y, j, t;
		char aux;
		for (i = 0; i < DOM_SCAN; i++) {
			et[i].count = 0;
			final_et[i].count = 0;
		}
		active_ssm.count = 0;

		//Citire
		FILE* fin = fopen(fileName, "r");
		fscanf(fin, "%d", &n);

		for (i = 0; i < n; i++) {
			fscanf(fin, "%d %d", &puncte[i].x, &puncte[i].y);
		}
		for (i = 0; i < n - 1; i++) {
			muchii[i].x1 = puncte[i].x;
			muchii[i].y1 = puncte[i].y;
			muchii[i].x2 = puncte[i + 1].x;
			muchii[i].y2 = puncte[i + 1].y;
		}
		muchii[n - 1].x1 = puncte[n - 1].x;
		muchii[n - 1].y1 = puncte[n - 1].y;
		muchii[n - 1].x2 = puncte[0].x;
		muchii[n - 1].y2 = puncte[0].y;

		printf("Puncte\n");
		for (i = 0; i < n; i++) {
			printf("Punctul %d: (%d, %d)\n", i, puncte[i].x, puncte[i].y);
		}
		printf("\nMuchii\n");
		for (i = 0; i < n; i++) {
			printf("Muchia %d: (%d, %d) - (%d, %d)\n", i, muchii[i].x1, muchii[i].y1, muchii[i].x2, muchii[i].y2);
			WriteLine(grilaCarteziana, muchii[i].x1, muchii[i].y1, muchii[i].x2, muchii[i].y2);
		}

		//Initializare ET
		double xm, xM, ym, yM;
		for (i = 0; i < n; i++) {
			if (muchii[i].y1 != muchii[i].y2) {
				ym = (muchii[i].y1 <= muchii[i].y2) ? muchii[i].y1 : muchii[i].y2;
				yM = (muchii[i].y1 > muchii[i].y2) ? muchii[i].y1 : muchii[i].y2;
				xm = (muchii[i].y1 == ym) ? muchii[i].x1 : muchii[i].x2;
				xM = (muchii[i].y1 == yM) ? muchii[i].x1 : muchii[i].x2;
				et[(int)ym].intersections[et[(int)ym].count].ymax = yM;
				et[(int)ym].intersections[et[(int)ym].count].xmin = xm;
				et[(int)ym].intersections[et[(int)ym].count].slope = (xm - xM) / (ym - yM);
				et[(int)ym].count++;
			}
		}

		//Sortare ET
		for (i = 0; i < n; i++) {
			sort(et[i].intersections, et[i].intersections + et[i].count, criteriu);
		}

		for (i = 0; i < n; i++) {
			if (et[i].count > 0) {
				y = i;
				break;
			}
		}

		do {
			for (i = 0; i < et[y].count; i++) {
				active_ssm.intersections[active_ssm.count] = et[y].intersections[i];
				active_ssm.count++;
			}
			for (i = 0; i < active_ssm.count; i++) {
				if (active_ssm.intersections[i].ymax == y) {
					for (j = i + 1; j < active_ssm.count; j++) {
						active_ssm.intersections[j - 1] = active_ssm.intersections[j];
					}
					active_ssm.count--;
					i--;
				}

			}
			sort(active_ssm.intersections, active_ssm.intersections + active_ssm.count, criteriu);
			for (i = 0; i < active_ssm.count; i++) {
				final_et[y].intersections[i] = active_ssm.intersections[i];
			}
			final_et[y].count = active_ssm.count;
			for (i = 0; i < active_ssm.count; i++) {
				if (active_ssm.intersections[i].slope != 0) {
					active_ssm.intersections[i].xmin += active_ssm.intersections[i].slope;
				}
			}

			y++;
		} 		while (active_ssm.count > 0 || et[y].count > 0);

		for (i = 0; i < DOM_SCAN; i++) {
			if (final_et[i].count > 0) {
				for (j = 0; j < final_et[i].count - 1; j += 2) {
					printf("%f %f\n", ceil(final_et[i].intersections[j].xmin), final_et[i].intersections[j + 1].xmin);

					double beginPoint = ceil(final_et[i].intersections[j].xmin);
					double endPoint = floor(final_et[i].intersections[j + 1].xmin - 0.01);
					/*if (endPoint < beginPoint) {
						endPoint = beginPoint;
					}*/
					for (t = beginPoint; t <= endPoint; t++) {
						grilaCarteziana.WritePixel(t, i, 30);
					}
				}
			}
		}

	}
};

void Init(void) {

	glClearColor(1.0, 1.0, 1.0, 1.0);

	glLineWidth(1);

	glPointSize(3);

	glPolygonMode(GL_FRONT, GL_LINE);
}

void Display1() {
	GrilaCarteziana grilaCarteziana(16, 16, 0, 0);
	Desenare2D desenare2D;

	//Cerc primul octant
	desenare2D.WriteCircle(grilaCarteziana, 0, 0, 13);
	desenare2D.WritePrimulOctant(grilaCarteziana, 0, 0, 13, 1);

}
void Display2() {
	GrilaCarteziana grilaCarteziana(27, 27, 0, 0);
	Desenare2D desenare2D;

	// Elipsa + umplere
	desenare2D.WriteElipsa(grilaCarteziana, 13, 7, 13, 7);
	desenare2D.UmpleElipsa(grilaCarteziana, 13, 7, 13, 7);

}
void Display3() {
	GrilaCarteziana grilaCarteziana(15, 15, 0, 0);
	Desenare2D desenare2D;

	// Umplere poligon
	desenare2D.umplerePoligon(grilaCarteziana, "poligon.txt");
}

void Display4() {
	GrilaCarteziana grilaCarteziana(16, 16, 0, 0);
	Desenare2D desenare2D;

	// Umplere poligon
	desenare2D.umplerePoligon(grilaCarteziana, "poligon2.txt");
}



void Display(void)
{
	switch (prevKey)
	{
		case '1':
			glClear(GL_COLOR_BUFFER_BIT);
			Display1();
			break;
		case '2':
			glClear(GL_COLOR_BUFFER_BIT);
			Display2();
			break;
		case '3':
			glClear(GL_COLOR_BUFFER_BIT);
			Display3();
			break;
		case '4':
			glClear(GL_COLOR_BUFFER_BIT);
			Display4();
			break;
	}
	glFlush();
}

void Reshape(int w, int h)
{
	glFlush();
	glClearColor(0, 0, 0, 1);
	glClear(GL_COLOR_BUFFER_BIT);
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);

}

void KeyboardFunc(unsigned char key, int x, int y)
{
	prevKey = key;
	if (key == 27) // escape
		exit(0);
	glutPostRedisplay();
}

void MouseFunc(int button, int state, int x, int y)
{
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitWindowSize(dim, dim);

	glutInitWindowPosition(100, 100);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutCreateWindow(argv[0]);

	Init();

	glutReshapeFunc(Reshape);

	glutKeyboardFunc(KeyboardFunc);

	glutMouseFunc(MouseFunc);

	glutDisplayFunc(Display);

	glutMainLoop();

	return 0;
}
