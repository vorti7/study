class Emp(val name:String, val salary:Long) {
  {
    println("this is Emp")
  }

  override def toString = s"Emp($name, $salary)"
}
//def fa(n:Int, m:Int): Unit ={
////  n+m
////}