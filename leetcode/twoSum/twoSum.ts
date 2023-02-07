function twoSum(nums: number[], target: number): number[] {
    let numIndices: number[] = [0,0];   
    let sum: number = 0; 
    for (let i: number = 0; i < nums.length; i++) {        
        for (let j: number = i + 1; j < nums.length; j++) {            
            console.log('i === ' + i);        
            console.log('j === ' + j);
            sum = nums[i] + nums[j]; 
            console.log('Sum of nums[i] + nums[j] ' + sum); 
            if (nums[i] + nums[j] === target) {
                console.log('Two Sum === ', + (nums[i] + nums[j]) + '  target === ' + target);
                console.log('Value of nums[i] ', nums[i] + ' when i ===  ' + i);
                console.log('Value of nums[j] ', nums[j] + ' when j ===  ' + j);
                numIndices[0] = i;                
                numIndices[1] = j;                                
                console.log(numIndices[0] + '  numIndices[0] Value');
                console.log(numIndices[1] + '  numIndices[1] Value');
                return numIndices;             
            }
        }        
    }
    return numIndices; 
};