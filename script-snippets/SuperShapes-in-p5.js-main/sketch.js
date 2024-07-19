var a =1;
var b =1;
var n1=1; 
var n2=1;
var n3=1;
var m;  
var slider; 
var index; 
var total; 
var totInd;

var osc = 0;

function setup() {
  createCanvas(800, 800); 
  button1 = createButton("1"); 
  button2 = createButton("2"); 
  button3 = createButton("3"); 
  button4 = createButton("4"); 
  button5 = createButton("5"); 
  slider = createSlider(1, 4, 1, 0.1); 
}

function supershape(theta) 
{
  var part1 = (1/a) * cos(m/4* theta); 
  part1 = abs(part1); 
  part1 = pow(part1, n2); 

  var part2 = (1/b)*sin(m/4*theta); 
  part2 = abs(part2); 
  part2 = pow(part2, n3); 
  
  var part3 = pow(part1 + part2, 1 / n1); 
  
  return(1/part3); 
}

function draw() {
  
  total = TWO_PI; 
  
  m =map(sin(osc), -1, 1, -6, 6);
  osc += 0.005; 
  //  m = slider.value(); 
  button1.mousePressed(function(){index = 1;}); 
  button2.mousePressed(function(){index = 2;}); 
  button3.mousePressed(function(){index = 3;}); 
  button4.mousePressed(function(){index = 4;}); 
  button5.mousePressed(function(){index = 5;}); 
  
  totalInd = slider.value();
  
  if(index==1)
    n1=n2=n3=1; 
  if(index==2)
    n1=n2=n3=0.3;
  if(index==3){
    n1=40; n2=n3=10;}
  if(index==4){
    n1 = 60; 
    n2 = 55; 
    n3 = 30;} 
  if(index==5){
  n1 = n2= n3 = 0.3; 
  total = 12*PI;
  //m = (slider.value()/ 6)
    m = m/10; 
  } 
  
  background(0); 
  translate(width/2, height/2); 
  
  stroke(255); 
  noFill(); 
  
  beginShape(); 
  for (var angle = 0; angle < total * totalInd; angle +=0.01) 
  {
    //noprotect
    var r = supershape(angle); 
    var x = 200 * r * cos(angle); 
    var y = 200 * r * sin(angle); 
  
    vertex(x, y); 
  }
        stroke(random(255), random(255), random(255)); 
  endShape(CLOSE); 
}
