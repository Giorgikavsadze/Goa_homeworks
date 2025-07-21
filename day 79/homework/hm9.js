let tagName = prompt("Enter a tag name (like div, p, img):")
tagName = tagName.toLowerCase()
let elements = document.getElementsByTagName(tagName);
alert("There are " + elements.length  + tagName + " elements on this page.");