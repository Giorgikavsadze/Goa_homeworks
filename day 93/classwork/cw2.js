const MathExpression =()=>{
    const expression=prompt("Enter Math Expression: ")
    console.log(expression)
    result=eval(expression)
    console.log(result)
    console.log(parseInt(result))
    console.log(parseFloat(result))
    
    

}
MathExpression()