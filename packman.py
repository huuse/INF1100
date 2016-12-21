#packman.py



var MAX_VALUE = 1.78E+308;

// fill a new array of size numElements and "value" at every location
var createArray = function (numElements, value) {
    var array = [];
    for(var i = 0; i < numElements; i++) {
        array.push(value);
    }

    return array;
};

var Maze = function(width, height, wallArray, playerX, playerY, cellSize) {

    // wallArray should be an array of 1s and 0s corresponding to walls and
    //  empty space.  The maze is index from the upper left, so the first
    //  entry in the array corresponds to the upper left of the maze.
    //  (x, y) = (0, 0) is the upper left.

    this.w = width;
    this.h = height;
    this.walls = wallArray;

    this.playerX = playerX;
    this.playerY = playerY;

    this.cellSize = cellSize;   // number of pixels per cell, for UI

    // set initial target to go to at initial player location
    this.targetX = playerX;
    this.targetY = playerY;
    this.targetIndex = playerX + playerY * this.w;

    // variables for the breadth-first search:

      // let MAX_VALUE be an undefined cost
    this.costArray = createArray(width * height, MAX_VALUE);

    this.bfsQueue = [];

    // animation variables
    this.currentDx = 0;
    this.currentDy = 0;


};




Maze.prototype.computeIndex = function(x, y) {
    return x + y * this.w;

};

// is the point x, y contained in the maze region defined by this.w, this.h?
Maze.prototype.isLegal = function (x, y) {
    return (x >= 0 && x < this.w && y >= 0 && y < this.h);
};

// return true or false, depending on whether there is a wall.


Maze.prototype.isWall = function (x, y) {
    //  If the x, y location is illegal, pretend there is a wall:
    if(!this.isLegal(x, y)) {
        return true;
    } else {
        return this.walls[this.computeIndex(x, y)] === 1;
    }
};



Maze.prototype.BFS = function() {
    // clear the cost array
    this.costArray = createArray(width * height, MAX_VALUE);

    // cost of getting to the target from the target is zero:
    this.costArray[this.targetIndex] = 0;

    // add the first cell to the queue
    this.bfsQueue = [this.targetIndex];

    while(this.bfsQueue.length > 0) {
        var currentIndex = this.bfsQueue.shift();

        // could check here if goal has been found.

        var currentCost = this.costArray[currentIndex];

        // add neighbors of currentIndex to queue
        var currentX = currentIndex % this.w;
        var currentY = floor(currentIndex / this.w);

        // loop over neighbors:  n, e, s, w
        var dirs = [ [0, -1], [1, 0], [0, 1], [-1, 0] ];
        for(var i = 0; i < dirs.length; i++) {
            var dx = dirs[i][0];
            var dy = dirs[i][1];

            var newX = currentX + dx;
            var newY = currentY + dy;
            var newIndex = this.computeIndex(newX, newY);

            // found a new cell for the first time:
            if(!this.isWall(newX, newY) &&
                    this.costArray[newIndex] > currentCost + 1) {
                // update cell cost:
                this.costArray[newIndex] = currentCost + 1;
                this.bfsQueue.push(newIndex);
            }

        }
    }
};





Maze.prototype.drawPlayer = function() {
    var px = this.playerX * this.cellSize;
    var py = this.playerY * this.cellSize;

    fill(255, 255, 0);
    stroke(0, 0, 0);

    ellipseMode(CORNER);
    ellipse(px + 10, py + 15, this.cellSize - 20, this.cellSize - 20);
};

Maze.prototype.drawTarget = function() {
    var px = this.targetX * this.cellSize;
    var py = this.targetY * this.cellSize;

    fill(255, 200, 200);
    stroke(255, 200, 200);

    rect(px + 1, py + 1, this.cellSize - 2, this.cellSize - 2);

    fill(0, 0, 0);
    textSize(10);
    text("GOAL", px+23, py+7);
};

// draw the cost of getting to square x, y, if cost is available
Maze.prototype.drawCost = function(x, y) {
    var index = this.computeIndex(x, y);
    if(this.costArray[index] !== MAX_VALUE) {
        var px = x * this.cellSize;
        var py = y * this.cellSize;

        var cx = px + this.cellSize / 2;
        var cy = py + this.cellSize / 2;

        textAlign(CENTER, CENTER);
        fill(60, 60, 60);
        if (Program.settings().drawCost) {
            text(this.costArray[index], cx, cy);
        }
    }
};

Maze.prototype.draw = function() {
    background(255, 255, 255);

    this.drawTarget();
    this.drawPlayer();

    for(var y = 0; y < this.h; y++) {
        for(var x = 0; x < this.w; x++) {
            if(this.isWall(x, y)) {
                var px = x * this.cellSize;
                var py = y * this.cellSize;

                fill(200, 200, 200);
                stroke(0, 0, 0);
                rect(px + 1, py + 1, this.cellSize - 2, this.cellSize - 2, 3);

            } else {
                this.drawCost(x, y);
            }

        }
    }

};

// given mouseX and mouseY values (in pixels), compute the
//  clicked square and set as target for the breadth-first search.
//  Don't set a new target unless mx, my is a clear space.
Maze.prototype.setTarget = function(mx, my) {
    var x = floor(mx / this.cellSize);
    var y = floor(my / this.cellSize);

    if(!this.isWall(x, y)) {
        this.targetX = x;
        this.targetY = y;
        this.targetIndex = this.computeIndex(x, y);
        this.BFS();

    }
};

// check if a number is within epsilon of an integer
var closeToInt = function(number, epsilon) {
    var closestInt = floor(number + 0.5);
    return abs(number - closestInt) < epsilon;
};


// clamp player coordinates to nearest int,
//  to take care of numerical drift
Maze.prototype.clampToInt = function() {
    this.playerX = floor(this.playerX + 0.5);
    this.playerY = floor(this.playerY + 0.5);
};

Maze.prototype.animatePlayer = function() {


    // only reset direction if at the center of a square.
    if(closeToInt(this.playerY, 0.01) && closeToInt(this.playerX, 0.01)) {
        this.clampToInt();


       // loop over neighbors:  n, e, s, w
        var dirs = [ [0, -1], [1, 0], [0, 1], [-1, 0] ];

        var bestDir = -1;
        var bestCost = this.costArray[
            this.computeIndex(this.playerX, this.playerY)];

        this.currentDx = 0;
        this.currentDy = 0;

        for(var i = 0; i < dirs.length; i++) {
            var dx = dirs[i][0];
            var dy = dirs[i][1];

            var newX = this.playerX + dx;
            var newY = this.playerY + dy;

            var newIndex = this.computeIndex(newX, newY);

            var cost = this.costArray[newIndex];
            //println("  cost " + cost);
            if(cost < bestCost) {
                bestCost = cost;
                bestDir = i;

                // update direction
                this.currentDx = dirs[bestDir][0];
                this.currentDy = dirs[bestDir][1];


            }


        }

        //println("dx " + this.currentDx);
        //println("dy " + this.currentDy);

    }

    this.playerX += 0.1 * this.currentDx;
    this.playerY += 0.1 * this.currentDy;


};


var walls = new Array(  1, 1, 1, 1, 1, 0, 1, 1,
                        1, 0, 0, 0, 0, 0, 0, 1,
                        1, 0, 1, 1, 1, 1, 0, 1,
                        1, 0, 1, 0, 1, 0, 0, 1,
                        1, 0, 1, 0, 1, 1, 0, 1,
                        1, 0, 1, 0, 1, 0, 0, 1,
                        1, 0, 0, 0, 0, 0, 0, 1,
                        1, 1, 1, 1, 1, 1, 1, 1
                    );

var maze = new Maze(8, 8, walls, 3, 3, 50);
maze.BFS();
frameRate(40);


var mousePressed = function() {
    maze.setTarget(mouseX, mouseY);
};

var draw = function() {
    maze.animatePlayer();
    maze.draw();

};



