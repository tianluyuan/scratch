add :: Float -> Float -> Float
add x y = x + y

add5 :: Float -> Float
add5 = add 5

add2 :: Num a => a -> a
add2 = (+) 2

-- Hutton Ch. 4
halve :: [a] -> ([a], [a])
halve x = (take h x, drop h x)
  where
    h = length x `div` 2

third :: [a] -> a
third x = head (drop 1 (drop 1 x))

third2 :: [a] -> a
third2 x = x !! 2

third3 :: [a] -> a
third3 (_:(_: (x : _))) = x 

safetail :: [a] -> [a]
safetail x | null x = []
           | otherwise = drop 1 x

safetail2 :: [a] -> [a]
safetail2 x = if null x then []  else drop 1 x

safetail3 :: [a] -> [a]
safetail3 [] = []
safetail3 x = drop 1 x

luhnDouble :: Int -> Int
luhnDouble x = if tx > 9 then tx - 9 else tx
  where
    tx = 2 * x

luhn :: Int -> Int -> Int -> Int -> Bool
luhn x y z w | (luhnDouble x + y + luhnDouble z + w) `mod` 10 == 0 = True
             | otherwise = False

-- Hutton Ch. 5
grid :: Int -> Int -> [(Int, Int)]
grid m n = [(x, y) | x <- [0..m], y<-[0..n]]

square :: Int -> [(Int, Int)]
square m = [(x, y) | (x, y) <- grid m m, x /= y]

myrep :: Int -> a -> [a]
myrep m x = [x | _ <- [1..m]]

pyth :: Int -> [(Int, Int, Int)]
pyth n = concat [[(x, y, z), (y, x, z)] | x <- [1..n], y <- [1..n], z <- [1..n], x < y && y < z && x^2+y^2==z^2]

dotprd :: [Int] -> [Int] -> Int
dotprd xs ys = sum ([x * y | (x, y) <- zip xs ys])

-- Hutton Ch. 6
fac :: Int -> Int
fac 0 = 1
fac n | n > 0 = n * fac (n - 1)

sumdown :: Int -> Int
sumdown 0 = 0
sumdown n | n > 0 = n + sumdown (n - 1)

euclid :: Int -> Int -> Int
euclid n m = case compare n m of
  EQ -> n
  LT -> euclid n (m - n)
  GT -> euclid (n - m) m

merge :: Ord a => [a] -> [a] -> [a]
merge ms [] = ms
merge [] ns = ns
merge (m:ms) (n:ns) | m < n = (m : merge ms (n : ns))
                    | otherwise = (n : merge (m : ms) ns)

msort :: Ord a => [a] -> [a]
msort [] = []
msort [x] = [x]
msort [x, y] | x < y = [x, y]
             | otherwise = [y, x]
msort xs = merge (msort ys) (msort zs)
  where
    (ys, zs) = halve xs

main :: IO ()
main = do
  putStrLn "hello"
  print (add (3^2) 2)
  print (add5 3.3)
  print (add2 3)
  print (halve [1..7])
  print (third [0..3])
  print (third2 [0..5])
  print (third3 [0..4])
  print (safetail [0..4])
  print (null (safetail []))
  print (safetail2 [-2..4])
  print (null (safetail2 []))
  print (safetail3 [-2..4])
  print (null (safetail3 []))
  print (luhn 1 7 8 4)
  print (luhn 4 7 8 3)
  print (sum [x^2 | x <- [1..100]])
  print (grid 1 2)
  print (square 2)
  print (myrep 3 True)
  print (pyth 100)
  print (dotprd [1,2,3] [1,1,2])
  print (fac 4)
  print (sumdown 3)
  print (euclid 6 27)
  print (merge [1, 3, 5] [3, 4, 6])
  print (msort [3, 4, 1, -2, -3])
