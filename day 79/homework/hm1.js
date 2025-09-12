let para = document.getElementsByTagName("p");

for (let i = 0; i < para.length; i++) {
    let text = para[i].textContent;
    let wordCount = text.split(" ").length;

    console.log(`Paragraph ${i + 1} has ${wordCount} words`);
}