//var s = Stream.from(100,2)
//var s = Stream.range[Char]('A','Z')
//var a = s.take(3).toList
//
//a = s.take(10).toList
//
//var c:Option[Int] = Some(3)
//
//import concurrent.ExecutionContext.Implicits.global
//val f = concurrent.Future {Thread.sleep(5);println("hi")}
//print(f)




class User(val name:String="asdf", val age:Int = 10){
  val isCheck = true
  val a = 30
  def pr(a:Int): Unit ={
    println(a,isCheck,name,age,this.a)
  }
  {
    println("this is user")
  }
//  val name = {println("hahaha");n}
//  val name = name

  def fe():Unit={
    println("sssss")
  }
}

//val user = new User("scala")
val user = new User()
print(user.isInstanceOf[User])
print(user.isInstanceOf[Any])
print(user name)
print(user name)
print(user name)
print(user pr(3))


class Sam (val name:String, val age:Int=10){
  override def toString = s"Sam($name, $age)"
}
val s = new Sam(name = "홍길동")
println(s.toString)