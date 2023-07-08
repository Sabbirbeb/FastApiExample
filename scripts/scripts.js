var urlParams;
(window.onpopstate = function () {
    var match,
        pl     = /\+/g,  // Regex for replacing addition symbol with a space
        search = /([^&=]+)=?([^&]*)/g,
        decode = function (s) { return decodeURIComponent(s.replace(pl, " ")); },
        query  = window.location.search.substring(1);

    urlParams = {};
    while (match = search.exec(query))
    urlParams[decode(match[1])] = decode(match[2]);
})();

function myFunction(q = 0) {
    //window.alert((q).toString())
    const a = urlParams['q']
    if (a) {
        document.getElementById("demo").innerHTML = a * a;
    }
    else {
        document.getElementById("demo").innerHTML = myFunction.name;
    }
}

function reset() {
    document.getElementById("demo").innerHTML = reset.name;
}
