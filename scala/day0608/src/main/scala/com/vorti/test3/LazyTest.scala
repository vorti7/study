package com.vorti.test3

class Sam{
  val a = {println("a"); 10}
  lazy val b = {println("b"); 20}
  def c(): Unit ={
    println("c")
    30
  }
}
object LazyTest {
  def main(args: Array[String]): Unit = {
    val s= new Sam
    println("end")
    s.b
    s.b
    s.b
  }
}
