package com.vorti.test

class Car (var make:String, var reverse:Boolean) {
  def rever(r:Boolean): Unit ={
    reverse = r
  }
  override def toString = s"Car($make, $reverse)"
}
class SuperCar(make:String, reverse:Boolean, var color:String) extends Car (make = make, reverse = reverse) {
  override def toString = s"Car($make, $reverse, $color)"
}