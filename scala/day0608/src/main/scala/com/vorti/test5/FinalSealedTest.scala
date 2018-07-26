package com.vorti.test5

//final class A
//class SubA extends A//cannot extend final class

class A{
  final def a(): Unit ={

  }
}
class SubA extends A{
//  override def a(): Unit = super.a()//cannot extend final method
}

sealed class B{

}//enable extend only same .scala
class SubB1 extends B{

}
class SubB2 extends B{

}

object FinalSealedTest {

}
