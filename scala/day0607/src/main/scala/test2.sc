//var a = List(1,2,3,4,5)
//var heada = a.head
//var taila = a.tail
//var backheada = a.reverse.head
//var backtaila = a.reverse.tail
//print(a == Nil)
//
//
//for(n<-a){
//  println(n)
//}
//
//def f(n:Int): Unit = {
//  println(n)
//}
//
////a.foreach(f)
////a.foreach(n=>println(n))
//a.foreach(n=>{
//  val addNum = 10
//  println(addNum+n)
//})

//val tup = (2,3,4,5,6) //tuple
//
//val list = List(2,3,4,5,6)
//
//val listA = list.map(_-10)
//
////val s = list.reduce((a,b) => a+b)
//val s= list.reduce(_+_)


//val map = Map("r" -> 0xff0000, "g"->0x00ff00, "b"->0x0000ff)
//
//for(a<-map){
//  for(b<-a.productIterator){
//    println(b)
//  }
//  println("*"*10)
//}


var a = List(1,2,3)
var b = List(4,5)

a = a++b

//a = a.filter(_%2==1)
//a = a.slice(from=1, until=3)
//
//
//a foreach(print(_))
a = a.take(3)
var a1 = List("a","b","C")
val c = a.zip(a1)



val aDo = List(1,0,1,0,1,0)

//aDo.foreach(n =>{
//  case 1 => println("OK")
//  case 0 => println("NO")
//})

a.fold(1)(_*_)