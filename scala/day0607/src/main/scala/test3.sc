//val a = List(1,2,3,4,5)
//
//val b= a.mkString("-")
//var tel = "010-1234-4321"
//tel = tel.split("-").mkString("")
//
//var z = List(1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1)
//var changedZ = z.toSet.toList.sorted

var a= List(1,2,3,4)

var b = a.toBuffer
b+=10
b+=11

a =  b.toList
//var z = mutable.Buffer(6)

//val c = Set newBuilder[Int]
//c+=1
//c+=2
//c+=3
//c+=4


//def inc(n:Int): Stream.Cons[Int] = {
//  Stream.cons(n.inc(n+1))
//}

def f1(n:Int, ch:Int):Int = {
  for( i <- 1 to n){
    print(i)
    if (i == ch )
      throw new Exception("e")

  }
  n
}

val ss = util.Try(f1(5,ch = 3))

val nValue = ss getOrElse -999
println("end nValue  : "+nValue)
