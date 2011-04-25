{--
 - http://projecteuler.net/index.php?section=problems&id=1
 -
 - If we list all the natural numbers below 10 that are multiples of 3 or 5,
 - we get 3, 5, 6 and 9. The sum of these multiples is 23.
 -
 - Find the sum of all the multiples of 3 or 5 below 1000.
 --}

e01_01 :: (Integral a) => a
e01_01 = sum $ filter (\x -> (x `mod` 3 == 0) || (x `mod` 5 == 0)) [1..999]


-- 0 3 6 9 12 15 18 21 24 27 30 33 36 39 42 
-- 0  5   10  15   20    25  30
xs = [3,5,6,9,10,12,15,18,20,21,24,25,27,30]
xss = iterate (map (+30)) xs
ns = concat xss
e01_02 limit = sum $ takeWhile (< limit) ns

-- e01_02 $ floor 1e3
