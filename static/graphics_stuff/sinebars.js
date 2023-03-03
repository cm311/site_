var box_size;
var grid;

var confLocs = [];
var confTheta = [];
var boxPeel = [];


function setup() {
    smooth();
    w = $('#holder').width();
    canvas = createCanvas(w, 150, WEBGL);
    canvas.parent('holder');
    
    angleMode(DEGREES);
    
    grid = {x_start: -50,
           x_end: 50,
           z_start: -50,
           z_end: 50,
           size: 4
           };
    
    box_size = 25;
    
    for(var i = 0; i < 200; i++) {
        confLocs.push(createVector(map(Math.random(), 0, 1, -500, 500),
                                  map(Math.random(), 0, 1, -800, 0),
                                  map(Math.random(), 0, 1, -500, 500)));
        confTheta.push(map(Math.random(), 0, 1, 0, 360));
        
    }
    
    for(var i = 0; i < 256; i++) {
        boxPeel.push({isFalling: false,
                     fallDistance: 0});
    } 
}

function draw() {
    background(20, 5, 5);
    camera(800, -600, 800, 
          0, 0, 0,
          0, 1, 0);
    
    directionalLight(100, map(sin(frameCount), -1, 1, 100, 220), 120, -400, 0, 0);
    directionalLight(100, 200, 120, 400, 1000, 0);
    
    rotateY(frameCount/2);
    
    ambientMaterial(255);
    //confetti();
    
    stroke(0);
    strokeWeight(2);
    drawBoxes();

    console.log('script is running...')
}

function drawBoxes() {
    var x, z, height, distance, noise_move;
    
    for(var i = 0; i < grid.size; i+=1) {
        for(var j = 0; j < grid.size; j+= 1) {
            push();
            x = map(i, 0, grid.size, grid.x_start, grid.x_end);
            z = map(j, 0, grid.size, grid.z_start, grid.z_end);
            translate(x, 0, z);
            
            distance = dist(0, 0, x, z);
            noise_move = map(noise(sin(distance) + frameCount/60), 0, 1, 100, 800)
            
            
            height = noise_move;
            box(box_size, height, box_size);
            pop();
        }
    }
}

function confetti() {
    for(var i = 0; i < confLocs.length; i++) {
        push();
        
        translate(confLocs[i].x, confLocs[i].y, confLocs[i].z);
        rotateX(confTheta[i]);
        rotateY(confTheta[i]/2);
        rotateZ(confTheta[i]/i);
        plane(15, 15);
        confLocs[i].y += 1;
        confTheta[i] += 5;
        pop();
        
        if(confLocs[i].y > 0) {
            confLocs[i].y = -800;
        }
    }
}
