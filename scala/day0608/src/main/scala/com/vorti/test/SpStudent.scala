package com.vorti.test

class SpStudent (name:String, age:Int, jum:Int, var grade:Char) extends Student (name, age, jum) {
  override def toString: String = s"Student($name, $age, $jum)"
}
