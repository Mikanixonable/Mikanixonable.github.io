// (作成） a = new Comp(1,1);

// (足し算)　c = Comp.add(a, b);

// （引き算）　c = Comp.sub(a, b);

// （掛け算） c = Comp.mul(a, b);

// （割り算） c = Comp.div(a, b);

// （べき乗） c = Comp.pow(a, b);

// （exp）    c = Comp.exp(a);

// (log)     c = Comp.log(a);



function Comp(x, y) {
    this.x = x;
    this.y = y;

    return this;
}

Comp.add = function (a, b) {
    return Comp(a.x+b.x, a.y+b.y);
}

Comp.sub = function (a, b) {
    return Comp(a.x-b.x, a.y-b.y);
}

Comp.mul = function (a, b) {
    return Comp(a.x*b.x-a.y*b.y, a.x*b.y+a.y*b.x);
}

Comp.div = function (a, b) {
    r2= b.x*b.x + b.y*b.y;
    return Comp((a.x*b.x+a.y*b.y)/r2, (-a.x*b.y+a.y*b.x)/r2);
}

Comp.conj = function (a) {
    return Comp(a.x, -a.y);
}

Comp.exp = function (a) {
    return Comp(Math.exp(a.x)*Math.cos(a.y),Math.exp(a.x)*Math.sin(a.y));

}

Comp.log = function (a) {
    r2= a.x*a.x + a.y*a.y;
    return Comp(0.5*Math.log(r2), Math.atan2(a.y,a.x));
}

Comp.cpow = function (a, b) {
    return Comp.exp(Comp.mul(Comp.log(a),b));
}

function abs(a) {
    return Math.sqrt(a.x*a.x+a.y*a.y);
}

function arg(a) {
    return Math.atan2(a.y,a.x);
}