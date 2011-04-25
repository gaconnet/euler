{--
 - A palindromic number reads the same both ways.
 - The largest palindrome made from the product of two 2-digit numbers
 - is 9009 = 91 × 99.
 -
 - Find the largest palindrome made from the product of two 3-digit numbers.
 -
--}
import Data.List (sort)

-- 5 * 5 = 25
-- 5 * 4 = 20
-- 5 * 3 = 15
-- 5 * 2 = 10
-- 5 * 1 =  5
-- 4 * 4 = 16
-- 4 * 3 = 12
-- 4 * 2 =  8
-- 4 * 1 =  4

e04_01 :: Integer
e04_01 = palindromes !! 0 where
  products = [x*y | x <- [999,998..100], y <- [x,x-1..100]]
  palindromes = (reverse . sort) $ filter palindromic6 products

palindromic6 n = p1 && p2 && p3 where
  digit p = n `div` (10^p) `mod` 10
  p1 = digit 0 == digit 5
  p2 = digit 1 == digit 4
  p3 = digit 2 == digit 3
