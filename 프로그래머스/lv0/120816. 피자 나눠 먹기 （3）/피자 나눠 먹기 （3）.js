function solution(slice, n) {
    // return Math.ceil(n/slice);
    let pizzaCount = 1;
    
    while ( pizzaCount * slice < n ) {
        pizzaCount++
    }
    
    return pizzaCount
}