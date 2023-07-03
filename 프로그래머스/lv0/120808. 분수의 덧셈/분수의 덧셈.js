// function gcd(a, b) {
//     return b === 0 ? a : gcd(b, a % b);
// }

// function solution(numer1, denom1, numer2, denom2) {
    
//     const lcm = (denom1 * denom2) / gcd(denom1, denom2);
    
//     const newNumer1 = numer1 * (lcm / denom1);
//     const newNumer2 = numer2 * (lcm / denom2);
    
//     const resultNumer = newNumer1 + newNumer2;
    
//     const commonDivisor = gcd(resultNumer, lcm);
//     const reducedNumer = resultNumer / commonDivisor;
//     const reducedDenom = lcm / commonDivisor;
    
//     return [reducedNumer, reducedDenom];
// }

function fnGCD(a, b){
    return (a%b) ? fnGCD(b, a%b) : b;
}

function solution(denum1, num1, denum2, num2) {
    let denum = denum1*num2 + denum2*num1;
    let num = num1 * num2;
    let gcd = fnGCD(denum, num); //최대공약수

    return [denum/gcd, num/gcd];
}