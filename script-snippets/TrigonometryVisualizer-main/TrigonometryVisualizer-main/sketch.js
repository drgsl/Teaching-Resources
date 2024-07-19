var x = 0; 
var angle =0; 

var ax = -1 ; 
var aangle = -1;
var index =0;  

function setup() {
  createCanvas(TWO_PI * 200, (TWO_PI+PI/4) * 100);
  translate(width/2, height/2); 
  linii(); 
  b1 = createButton("Sinus"); 
  b2 = createButton("Cosinus"); 
  b3 = createButton("Tangenta"); 
  b4 = createButton("Cotangenta"); 
  b5 = createButton("All"); 
  b0 = createButton("None"); 
  createP(' '); 
  b6 = createButton("Arcsinus"); 
  b7 = createButton("Arccosinus"); 
  b8 = createButton("Arctangenta"); 
  b9 = createButton("Arcotangenta"); 
  b10 = createButton("All"); 
    createP(' '); 
  b11 = createButton("x"); 
  b12 = createButton("x^2"); 
  b13 = createButton("x^3"); 
  b14 = createButton("log(x)"); 
  b15 = createButton("log(x^2)"); 
  b16 = createButton("x^1/3"); 
  b17= createButton("x^2/3"); 
  b18= createButton("All"); 
      createP(' '); 
  //b19= createButton("EVERYTHING"); 


}

function linii(){
  background(100); 
  x =0 ; 
  angle = 0;
  strokeWeight(10); 
  stroke(255, 0, 0);
  point(0, 0);
  strokeWeight(1); 
  text("(0.0)", 10, -10);
  stroke(0); 
  strokeWeight(10); 
  point(0, 100);
  point(PI/2 * 100, 0); 
  point(PI * 100, 0); 
  point(3* PI/2 * 100, 0);
  point(-PI/2 * 100, 0); 
  point(-PI * 100, 0); 
  point(-3* PI/2 * 100, 0); 
  point(-3* PI/2 * 100, 100); 
    //point(0, 0);
  point(PI/2 * 100, 100); 
  point(3* PI/2 * 100, -100);
  point(-PI * 100, -100);
  point(-PI/2 * 100, -100);
  point(PI * 100, -100);
  point(-100, PI/2 * 100); 
  point(100, 0); 
  strokeWeight(1); 
  text("(π  / 2, 0)", PI/2 * 100 +10, -10);
  text("(0, -1)", 0 * 100 +10, 100+10);
  text("(π , 0)", PI * 100 +10, -10);
  text("(3 * π / 2, 0)", 3 * PI/2 * 100 +10, -10);
  text("(-π / 2, 0)", -PI/2 * 100 +10, -10);
  text("(-π, 0)", -PI * 100 +10, -10);
  text("(-3 * π / 2, 0)", -3 * PI/2 * 100 +10, -10);
  text("(π  / 2, -1)", PI/2 * 100 +10, 110);
  text("(π , 1)", PI * 100 +10, -110); 
  text("(3 * π / 2 , 1)", 3*PI/2 * 100 +10, -110);
  text("(-π , 1)", -PI * 100 +10, -110);
  text("(-π / 2 , 1)", -PI/2 * 100 +10, -110);
  text("(3 * π / 2 , -1)", -3*PI/2 * 100 +10, 110);
  line(-width/2, 0, width/2, 0); 
  line(0, -height/2, 0, height/2); 
  line(PI/2*100, height, PI/2 * 100, -height); 
  line(PI*100, height, PI*100, -height); 
  line(3*PI / 2 *100, height, 3*PI / 2 *100, -height); 
  line(-PI/2*100, height, -PI/2 * 100, -height); 
  line(-PI*100, height, -PI*100, -height); 
  line(-3*PI / 2 *100, height, -3*PI / 2 *100, -height); 
  line(-width, -PI*100, width, -PI*100);
  line(-width, PI*100, width, PI*100);
  line(-width, PI/2*100, width, PI/2*100);
  line(-width, -PI/2*100, width, -PI/2*100);
}

function draw() {
      translate(width/2, height/2); 
b0.mousePressed(function(){index = 0; linii(); })
b1.mousePressed(function(){index = 1; linii(); })
b2.mousePressed(function(){index = 2; linii(); })
b3.mousePressed(function(){index = 3; linii(); })
b4.mousePressed(function(){index = 4; linii(); })
b5.mousePressed(function(){index = 5; linii(); })
b6.mousePressed(function(){index = 6; linii(); })
b7.mousePressed(function(){index = 7; linii(); })
b8.mousePressed(function(){index = 8; linii(); })
b9.mousePressed(function(){index = 9; linii(); }) 
b10.mousePressed(function(){index = 10; linii(); })  
b11.mousePressed(function(){index = 11; linii(); })
b12.mousePressed(function(){index = 12; linii(); })
b13.mousePressed(function(){index = 13; linii(); })
b14.mousePressed(function(){index = 14; linii(); }) 
b15.mousePressed(function(){index = 15; linii(); })  
b16.mousePressed(function(){index = 16; linii(); })
b17.mousePressed(function(){index = 17; linii(); }) 
b18.mousePressed(function(){index = 18; linii(); })  
//b19.mousePressed(function(){index = 19; linii(); })  

  if(index == 1)
    sinus(); 
  if(index == 2)
    cosinus(); 
  if(index == 3)
    tangenta(); 
  if(index == 4)
    cotangenta(); 
  if(index == 5){
    sinus(); 
    cosinus();
    tangenta(); 
    cotangenta();} 
  if(index == 6)
    arcsinus(); 
  if(index == 7)
    arccosinus(); 
  if(index == 8)
    arctangenta(); 
  if(index == 9)
    arccotangenta(); 
  if(index == 10){
		arcsinus(); 
    arccosinus();
    arctangenta(); 
    arccotangenta();}
  if(index == 11)
    X(); 
  if(index == 12)
    x2(); 
  if(index == 13)
    x3(); 
  if(index == 14)
    logx(); 
  if(index == 15)
    logx2(); 
  if(index == 16)
    rad13x(); 
  if(index == 17)
    rad23x(); 
  if(index == 18){
    X();  
    x2();
    x3(); 
    logx();
    logx2(); 
    x3(); 
    logx();
    rad13x(); 
    rad23x(); 
  } 
  if(index == 19){
    sinus(); 
    cosinus(); 
    tangenta(); 
    cotangenta(); 
    arcsinus(); 
    arccosinus(); 
    arctangenta(); 
    arccotangenta(); 
    X(); 
    x2(); 
    x3(); 
    logx(); 
    log2x(); 
    rad13x(); 
    rad23x(); 
  }
  
}

function sinus(){
  if(floor(abs(x)) == 0){
  stroke(random(255), random(255), random(255));
    angle = 0; 
 	 	x = 0;}
  var y = map(sin(angle), -1, 1, -100, 100); 
  x +=4;
  angle +=0.04; 
  strokeWeight(7); 
  point(x, y);
  //text("ok", x, y); 
  if(x>= width/2)
  x=-width/2;

}

function cosinus(){
  //console.log(x); 
  if(floor(abs(x)) == 0){
  stroke(random(255), random(255), random(255));
    angle = 0; 
 	 	x = 0;}
  var y = map(cos(angle), -1, 1, -100, 100); 
  x +=4;
  angle +=0.04; 
  strokeWeight(7); 
  point(x, y);
  //text("ok", x, y); 
  if(x>= width/2)
  x=-width/2;
}


function tangenta(){
  //console.log(x); 
  if(floor(abs(x)) == 0){
  stroke(random(255), random(255), random(255));
    angle = 0; 
 	 	x = 0;
  }
  var y = map(tan(angle), -1, 1, 100, -100); 
  x +=4;
  angle +=0.04; 
  strokeWeight(7); 
  point(x, y);
  //text("ok", x, y); 
  if(x>= width/2)
  x=-width/2;
}


function cotangenta(){
  //console.log(x); 
  if(floor(abs(x)) == 0){
  stroke(random(255), random(255), random(255));
    angle = 0; 
 	 	x = 0;
  }
  
  var y = map(1/tan(angle), -1, 1, 100, -100); 
  x +=4;
  angle +=0.04; 
  strokeWeight(7); 
  point(x, y);
  //text("ok", x, y); 
  if(x>= width/2)
  x=-width/2;
}

function arcsinus(){
    ax +=0.05; 
    if(ax > 1)
    {ax = -1;
       stroke(random(255), random(255), random(255));}
  var y = asin(ax); 
  strokeWeight(7); 
  point(ax * 100, -y* 100);

}


function arccosinus(){
    ax +=0.05; 
  if(ax > 1)
    {ax = -1;
       stroke(random(255), random(255), random(255));}
  var y = acos(ax); 
  strokeWeight(7); 
  point(ax * 100, -y* 100);

}

function arctangenta(){
  
  if(floor(x*20) ==0)
  stroke(random(255), random(255), random(255));
  
  var y = atan(x);
  x +=0.05; 
  strokeWeight(7); 
  point(x * 100, -y* 100);
  if(x >= width/200)
    x = -width/200;
}

function arccotangenta(){
  
  if(floor(x*20) ==0)
  stroke(random(255), random(255), random(255));
  
  var y = PI/2 - atan(x);
  x +=0.05; 
  strokeWeight(7); 
  point(x * 100, -y* 100);
  if(x >= width/200)
    x = -width/200;
}


function X(){
  if(floor(x*100) == 0)
    stroke(random(255), random(255), random(255));
    strokeWeight(7); 
  point(x*100, x*100);
  x +=0.02; 
    if(x >= 3.6)
    x = -3.6; 
}

function x2(){
  if(floor(x*100) == 0)
   stroke(random(255), random(255), random(255));
    strokeWeight(7);
  y = x*x; 
  point(x*100, -y*100);
  //console.log(x, y);
  x +=0.02; 
    if(x >= 2)
    x = -2; 
}

function x3(){
  if(floor(x*10) == 0)
   stroke(random(255), random(255), random(255));
    strokeWeight(7);
  y = (pow(x, 3)); 
  point(x*100, -y*100);
  //console.log(x, y);
  x +=0.02; 
    if(x >= 1.6)
    x = -1.6; 
}

function logx(){
  //if(floor(x*1) == 0)
    strokeWeight(7);
  y = log(x); 
  point(x*100, -y*100);
  //console.log(x, y);
  x +=0.04; 
    if(x >= 7){
      stroke(random(255), random(255), random(255));
      x = 0; 
}
}

function logx2(){
  if(floor(x*10) == 0)
   stroke(random(255), random(255), random(255));
    strokeWeight(7);
  y = log((x*x)); 
  point(x*100, -y*100);
  //console.log(x, y);
  x +=0.03; 
    if(x >=6)
    x = -6; 
}

function rad13x(){
  if(floor(x*50) == 0)
   stroke(random(255), random(255), random(255));
    strokeWeight(7);
  y = Math.cbrt(x); 
  point(x*100, -y*100);
  //console.log(x, y);
  x +=0.03; 
    if(x >=6.5)
    x = -6.5; 
}


function rad23x(){
  if(floor(x*50) == 0)
   stroke(random(255), random(255), random(255));
    strokeWeight(7);
  y = Math.cbrt(x*x); 
  point(x*100, -y*100);
  //console.log(x, y);
  x +=0.03; 
    if(x >=6.5)
    x = -6.5; 
}










