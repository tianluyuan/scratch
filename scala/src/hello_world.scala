/**
 * Created by tianlu on 3/25/14.
 */
println("hello, world")

args.foreach(arg => println(arg))

val mike = (23, "jordan")
println(mike._1)
println(mike._2)

// Try to program in the functional style.  I.e. without using 'vars', only 'vals'.
// Functions should not change the state of any object.  Takes an input, returns output.
// Unit (void) functions are thus not entirely functional.
// Prefer 'vals', immutable objects (Lists, default Maps, default Sets).
println("example of functional code")
def formatArgs(args: Array[String]) = args.mkString("\n")
println(formatArgs(args))

val l = List(1, 2, 3, 2, 1)
val max_reduce = l.reduceLeft((a, b) => if (a>b) a else b)
println(max_reduce)

val lines = List("hello", "world", "this", "ldsfkdalklaslkjsdkakla")

// Note, method parameters are all vals not vars
def widthOfLength(s: String) = s.length.toString.length
val longestLine = lines.reduceLeft(
  (a, b) => if (a.length > b.length) a else b
)
val maxWidth = widthOfLength(longestLine)

for (line <- lines) {
  val numSpaces = maxWidth - widthOfLength(line)
  val padding = " " * numSpaces
  println(padding + line.length +" | "+ line)
}
