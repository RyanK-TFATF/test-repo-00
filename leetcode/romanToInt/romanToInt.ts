function romanToInt(s: string): number {    
    let value = 0;   
    const roman: string[] = s.split('');
    const numerals: number[] = [1, 5, 10, 50, 100, 500, 1000]; // Value Conversions 
    
    console.log(roman); 

    let i = 0
    while (i < roman.length) {
        console.log(roman[i]);
        if (roman[i] === 'I' && roman[i + 1] === 'V') {
            value += numerals[1] - numerals[0];
            i++; 
        } else if (roman[i] === 'I' && roman[i + 1] === 'X') {
            value += numerals[2] - numerals[0];
            i++; 
        } else if (roman[i] === 'X' && roman[i + 1] === 'L') {
            value += numerals[3] - numerals[2];
            i++; 
        } else if (roman[i] === 'X' && roman[i + 1] === 'C') {
            value += numerals[4] - numerals[2];
            i++; 
        } else if (roman[i] === 'C' && roman[i + 1] === 'D') {
            value += numerals[5] - numerals[4];
            i++; 
        } else if (roman[i] === 'C' && roman[i + 1] === 'M') {
            value += numerals[6] - numerals[4];
            i++; 
        } else if (roman[i] === 'I') {
            value += numerals[0];
        } else if (roman[i] === 'V') {
            value += numerals[1];
        } else if (roman[i] === 'X') {
            value += numerals[2];        
        } else if (roman[i] === 'L') {
            value += numerals[3];
        } else if (roman[i] === 'C') {
            value += numerals[4];
        } else if (roman[i] === 'D') {
            value += numerals[5];
        } else if (roman[i] === 'M') {
            value += numerals[6];    
        } 
        console.log(value); 
        i++;
    }    
 
    return value;
}

  // console.log(numerals.s);        
    // write the logic for subtraction rules.     
    // If one char, assign value. Faster to put outside of loop, since it won't execute loop and access values array?
    // Else If two chars, assign value. Faster to put outside of loop, since it won't execute loop and access values array?
    // Iterate through string starting at values[2]. (let i = 2, while i < length of array, i++)
            // If i and i+1 match the subtraction rules use to calculate value, add to total, i++
            // Else add i to total.                                                    
  
romanToInt('III')
romanToInt('LVIII')
romanToInt('MCMXCIV')