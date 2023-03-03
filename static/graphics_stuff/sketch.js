function setup() {
    smooth();
    w = $('#sketch-list-groupitem').width();
    canvas = createCanvas(w, 200, WEBGL);
    canvas.parent('sketch-list-groupitem');
    
    angleMode(DEGREES);
}

function draw() {
    background(100);
}