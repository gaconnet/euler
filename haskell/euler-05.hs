{--
 - 2520 is the smallest number that can be divided by each of the numbers
 - from 1 to 10 without any remainder.
 -
 - What is the smallest number that is evenly divisible by
 - all of the numbers from 1 to 20?
--}

-- |2           => must be even
-- |3           => 3,6,9,12,15,18,21,24,27,30
-- |4  (2)      => 4,8,16,20,24,28,32,
-- |5           => 5,10,15,20,25,30,35,40
-- |6  (3,2)    => 6,12,18,24,30,36,42
-- |7 
-- |8  (4,2)
-- |9  (3)
-- |10 (5,2)  %[1..10] <- [10,9,8,7,6]
-- |11
-- |12 (6,4,3,2)
-- |13
-- |14 (7,2)
-- |15 (5,3)
-- |16 (8,4,2)
-- |17
-- |18 (9,6,3,2)
-- |19
-- |20 (10,5,4,2) %[1..20] <- [20,19,18,17,16,15,14,13,12,11]
-- 
a `divides` b = b `mod` a == 0

e05_01 :: [Integer]
e05_01 = sieve [20*19,40*19..] where
  zs = [20,19..11]
  p x = all (`divides` x) zs
  sieve = dropWhile (not . p)

e05_02 = foldr1 lcm [20,19..11]
