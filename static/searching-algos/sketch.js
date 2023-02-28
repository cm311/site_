//The graph to draw

//an array of points.
var arr = [];
var target;
var arr_x = -1000;
var is_searching;
var timer;

function setup() {
    var canvas = createCanvas(windowWidth * 4.5/6, windowHeight * 3.6/6);
    canvas.parent('sketch-holder');
    textFont('Georgia');

    is_searching = false;
    timer = 0;
}

function draw() {
    background(20, 5, 5);
    drawarray();
    

    stroke(241, 209, 225);
    fill(241, 209, 225);
    text("Target: ", 100 + arr_x, height - 150);
    text(target, 200 + arr_x, height- 150);
    arr_x += 20;

    if (arr_x > 0) {
      arr_x = 0;
    }

    


    if(is_searching) {
      console.log(timer);
      console.log(linearsearch(arr, target));
      timer += millis();
    }

    

    
}

function drawarray() {
  textSize(24);
  strokeWeight(1);
  noStroke();


  for(var i = 0; i < arr.length; i++) {
    noStroke();
    fill(20, 60, 150);
    square(25 + (i*50) + arr_x, 60, 50, 10);

    stroke(241, 209, 225);
    fill(241, 209, 225);
    
    text(arr[i], 40 + (i*50) + arr_x, 93);
  }

}


function createarray() {
  arr_size = 20;
  arr = []
  arr_x = -1000;

  for (var i=0; i < arr_size; i++) {
    arr.push(Math.floor(Math.random() * 100));
  }

  target = arr[Math.floor(Math.random() * 20)];
  console.log(arr)

  is_searching = true;
}


function linearsearch(arr, key){

  timer = 0;

  for(let i = 0; i < arr.length; i++){
    noStroke();
    fill(120, 160, 250);
    square(25 + (i*50) + arr_x, 60, 50, 10);
    if(arr[i] === key) {
        return i
    }
  }
  return -1
}



