//The graph to draw

//an array of points.
var vertices = [];
var adjmatrix;
var colormatrix;
var isdrawn;
var pathdrawn;
var end;

function setup() {
    var canvas = createCanvas(windowWidth * 4.5/6, windowHeight * 3.6/6);
    canvas.parent('sketch-holder');
}

function draw() {
    background(0);

    if(isdrawn == true) {

    }
    if(isdrawn == false) {

    }

    
}


function bblSort(arr){
    
    for(var i = 0; i < arr.length; i++){
       
      // Last i elements are already in place 
      for(var j = 0; j < ( arr.length - i -1 ); j++){
         
        // Checking if the item at present iteration
        // is greater than the next iteration
        if(arr[j] > arr[j+1]){
           
          // If the condition is true then swap them
          var temp = arr[j]
          arr[j] = arr[j + 1]
          arr[j+1] = temp
        }
      }
    }

    return arr
}



