package com.vorti.test4

class Sam{
  private val a = 10
  protected val b = 20
  val c = 30
  def pr()={
    println(a,b,c)
  }
}
class SubSam extends Sam{
  def pr1()={
//    println(a)//only for in class
    println(b)
    println(c)
  }
}

object AccessTest{
  def main(args: Array[String]): Unit = {
    var a = new Sam
//    println(a.b)//in class or abstracted class
    println(a.c)
  }
}
