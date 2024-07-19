var slider;
var slider2; 

function setup() {
	createCanvas(1000, 700);
	var angle = PI / 4;
	var shrink; 
	slider = createSlider(0, TWO_PI, PI / 4, 0.01);
	slider2 = createSlider(0, 0.8, 0.7, 0.0001);

}

function draw()
{
    background(0);
	angle = slider.value();
	shrink = slider2.value(); 
    print(shrink); 
	//var len = 100;
	stroke(255);
	translate(width/2, height/1.2);
    //stroke(random(255), random(255), random(255));
	branch(100);
}

function branch(len) {
	//stroke(random(255), random(255), random(255));
	line(0, 0, 0, -len);
	translate(0, -len);
	if (len > 4) {
		push();	
		rotate(angle);	
		branch(len * shrink);
		pop();		
		push();
		rotate(-angle);
		branch(len * shrink);
		pop(); 	
	}
}
