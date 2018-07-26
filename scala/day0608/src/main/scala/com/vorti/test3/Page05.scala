package com.vorti.test3

class AClass(val num:Int){
  def apply(su:Int):Int={
    num * su
  }
}

object Page05 {
  def main(argsl:Array[String])={
    val mul = new AClass(num = 2)
    var su = mul.apply(3)
    println(su)
    su = mul(9)
    println(su)
    su = mul.apply(5)
    println(su)
  }

}
