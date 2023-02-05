function isPalindrome(x: number): boolean {
    let palindrome: boolean = false;
    const oldNum: string[] = x.toString().split('')
    const newNum: string[] = x.toString().split('').reverse();
    
    for (let i = 0; i < oldNum.length; i++) {
        console.log(oldNum[i]);
        console.log(newNum[i]);
        if (oldNum[i] === newNum[i]) {            
            palindrome = true;
        } else {                        
            palindrome = false;
            console.log('Else palindrome ' + palindrome)
            return palindrome;
        }
    }
    console.log('Main palindrome' + palindrome)    
    return palindrome;
};

isPalindrome(1000021);