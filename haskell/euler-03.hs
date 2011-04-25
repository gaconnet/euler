{--
 - The prime factors of 13195 are 5, 7, 13 and 29.
 -
 - What is the largest prime factor of the number 600851475143 ?
--}

m `divides` n = n `mod` m == 0

primes :: (Integral a) => [a]
primes = infinitePrimes [2..] [] [] where
  infinitePrimes (x:xs) [] ps = x:(infinitePrimes xs ps (x:ps))
  infinitePrimes cs@(x:xs) (p:ps) accps = case p `divides` x of
    False -> infinitePrimes cs ps accps
    True  -> infinitePrimes xs accps accps

primesUpTo :: (Integral a) => a -> [a]
primesUpTo n = takeWhile (<n) primes

e03_01 = tie (primesUpTo n) n where
  n = 600851475143 
  tie [] x = x
  tie (p:ps) x = case p `divides` x of
    False -> tie ps x
    True  -> tie (primesUpTo y) y where
      y = x `div` p
