function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

function solution(numer1, denom1, numer2, denom2) {
    
    const lcm = (denom1 * denom2) / gcd(denom1, denom2);
    
    const newNumer1 = numer1 * (lcm / denom1);
    const newNumer2 = numer2 * (lcm / denom2);
    
    const resultNumer = newNumer1 + newNumer2;
    
    const commonDivisor = gcd(resultNumer, lcm);
    const reducedNumer = resultNumer / commonDivisor;
    const reducedDenom = lcm / commonDivisor;
    
    return [reducedNumer, reducedDenom];
}