//The graph to draw

//an array of points.
var arr;
var target;
var searching;
var timer;
var start_time;
var fresh_array;

function setup() {
    var canvas = createCanvas(windowWidth * 4.5/6, windowHeight * 3.6/6);
    canvas.parent('sketch-holder');
    textFont('Georgia');

    arr = {x: -1000,
      y: 60,
      square_width: 50,
      squre_rounding: 10,
      square_color1: color(20, 60, 150),
      data : []}
    
    target = { x: -1000,
              y : height-250,
              string:'',
              index:''
    }

    timer = 0;
    searching = false;
    fresh_array = false;
}

function draw() {

    background(20, 5, 5);
    drawarray();
    

    stroke(241, 209, 225);
    fill(241, 209, 225);
    text("Target: ", 100 + target.x, target.y);
    text(target.string, 200 + target.x, target.y);
    arr.x += 40;
    target.x += 25;

    if (arr.x > 0) {
      arr.x = 0;
    }

    if (target.x > 0) {
      target.x = 0;
    }

    if(searching) {
      timer = Math.round((millis() - timer) / 1000) - start_time;

      console.log(target.index)
      blu = map(sin(frameCount/7), -1, 1, 150, 255);
      redd = map(sin(frameCount/7), -1, 1, 20, 80);
      arr.square_color2 = color(20, redd, blu);
  
      noStroke();
      fill(arr.square_color2);
      square(25 + (timer*arr.square_width) + arr.x, arr.y, arr.square_width, arr.squre_rounding);
  
      stroke(241, 209, 225);
      fill(241, 209, 225);
      
      text(arr.data[timer], 40 + (timer*arr.square_width) + arr.x, 93);

      drawarray2()
    }

    if (timer >= target.index && timer != 0 && !fresh_array) {
      searching = false;
      drawarray2();

      noStroke();
      fill(10, 250, 150);
      square(25 + (target.index*arr.square_width) + arr.x, arr.y, arr.square_width, arr.squre_rounding);

      stroke(241, 209, 225);
      fill(241, 209, 225);
      
      text(arr.data[target.index], 40 + (target.index*arr.square_width) + arr.x, 93);
    }
}

function drawarray() {
  textSize(24);
  strokeWeight(1);
  noStroke();


  for(var i = 0; i < arr.data.length; i++) {
    noStroke();
    fill(arr.square_color1);
    square(25 + (i*arr.square_width) + arr.x, arr.y, arr.square_width, arr.squre_rounding);

    stroke(241, 209, 225);
    fill(241, 209, 225);
    
    text(arr.data[i], 40 + (i*arr.square_width) + arr.x, 93);
  }
}

function drawarray2() { 
  textSize(24);
  strokeWeight(1);
  noStroke();


  for(var i = 0; i < timer; i++) {
    noStroke();
    fill(color(100, 100, 100));
    square(25 + (i*arr.square_width) + arr.x, arr.y, arr.square_width, arr.squre_rounding);

    stroke(241, 209, 225);
    fill(241, 209, 225);
    
    text(arr.data[i], 40 + (i*arr.square_width) + arr.x, 93);
  }
}

function starttimer() {
  start_time = Math.floor(millis() / 1000)
}


function createarray() {
  searching = false;
  arr_size = 20;
  arr.x = -1000;
  arr.data = []

  for (var i=0; i < arr_size; i++) {
    arr.data.push(Math.floor(Math.random() * 100));
  }

  target.string = arr.data[Math.floor(Math.random() * 20)];
  target.index = arr.data.indexOf(parseInt(target.string))
  console.log(arr)
  console.log(target.index)
  fresh_array = true;
}

function startsearch() {
  searching = true;
  starttimer();
  fresh_array = false;
}



function linearsearch(arr, key){

  for(let i = 0; i < arr.length; i++){
    if(arr[i] === key) {
        return i
    }
  }
  return -1
}
