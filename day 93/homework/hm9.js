const numcheck = () => {
    const num = parseFloat(prompt("Enter the first number"));
    const num1 = parseFloat(prompt("Enter the second number"));
    const operator = prompt("Enter an operator (+, -, *, /)");

    if (isNaN(num) || isNaN(num1)) {
        console.log("Calculation can't be performed because one or both inputs are not numbers");
        return;
    }

    let result;
    switch (operator) {
        case '+':
            result = num + num1;
            break;
        case '-':
            result = num - num1;
            break;
        case '*':
            result = num * num1;
            break;
        case '/':
            if (num1 === 0) {
                console.log("Division by zero is not allowed");
                return;
            }
            result = num / num1;
            break;
        default:
            console.log("Invalid operator");
            return;
    }

    
    console.log(result);
}

numcheck();
