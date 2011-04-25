{--
 - By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 - we can see that the 6^(th) prime is 13.
 -
 - What is the 10001^(st) prime number?
--}

m `divides` n = n `mod` m == 0

-- 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
-- x x   x   x        x     x           x     x           x

primes :: (Integral a) => [a]
primes = 2:sieve [3,5..] [2] where
  sieve xs ps = r:sieve rs (r:ps) where
    (r:rs) = dropWhile (\x -> any (`divides` x) ps) xs

e07_01 = primes !! 10000 -- sub1 for 0-based index
