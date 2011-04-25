{--
 - Find the difference between the sum of the squares of the
 - first one hundred natural numbers and the square of the sum.
--}

e06_01 :: Integer
e06_01 = sqosu 100 - suosq 100 where
  suosq = sum . (map (^2)) . (enumFromTo 1)
  sqosu = (^2) . sum . (enumFromTo 1)
