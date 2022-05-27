exports.creditCheck = function(str) {
    let creditNum = str.split('');
    //turn str into arr of ints
    let toNum = creditNum.map(Number)
    for(let i = 0; i < toNum.length; i++){
        //loop through every other and multiply by 2
        if(i % 2 === 0){
            toNum.splice(i, 1, toNum[i] * 2);
            if(toNum[i] > 9){
                //if num is greater than 9, split, turn to str, turn back to int and add 
                let splitNum = toNum[i].toString().split('').map(Number).reduce((x,y) => x + y)
                //add back to arr
                toNum.splice(i, 1, splitNum);
            }
        }
    }
    //add all items together 
    let sumAll = toNum.reduce((a,b) => a + b)
    //check if number if valid 
    const result = sumAll % 10 === 0 ? "The number is valid!" : "The number is invalid!"
    return result
}
