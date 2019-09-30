var arcane = function () {
  var z = '7';
  var y = '3';
  var x = '8';
  var w = '4';
  var v = '6';
  var u = '1';
  var t = '0';
  var s = '2';
  var r = '5';
  var q = '9';

  var mapper = function (element) {
    var num = parseInt(element);
    return String.fromCharCode(num);
  }

  var flag = [u + t + s, u + t + x, q + z, u + t + y, w + r, z + y, x + x, w + v, u + t + x, z + s, r + u, x + s, z + z, z + y, u + u + v, r + u];
  var mapped = flag.map(mapper);
  return mapped.join('');
}

var result = arcane();
console.log(result);