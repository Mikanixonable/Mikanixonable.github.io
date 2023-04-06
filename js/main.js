
const body2 = document.getElementsByTagName('body')[0]
let i2 = document.createElement("i")
let str = window.location.href.split('/').pop();
let num0 = parseInt(str.split(".")[0], 10)
let num1 = parseInt(str.split(".")[0], 10) - 1
let num2 = parseInt(str.split(".")[0], 10) + 1
i2.innerHTML = `<a href=\"${num1}.html\"><${num1}</a>` + " "
  + `<a href=\"index.html\">|home|</a>` + " "
  + `<a href=\"${num2}.html\">${num2}></a>`
body2.prepend(i2)