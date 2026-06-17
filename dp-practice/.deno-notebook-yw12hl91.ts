const nums = [1,5,2];
const getWinner = (nums: Array<number>) =>{
    const dp = Array.from({length: nums.length}, (_, index_0)=>Array.from({length: nums.length}, (_, index_1)=>Boolean(index_0 === index_1)));
    console.log(dp)
    for(let i = nums.length - 1; i >= 0; i--){
        for(let j = i; j>=i; j++){

        }
    }
}
getWinner(nums);