val a:Any = 10
val b = a match{
case s: Int  => "Int"
case s: String  => "String"
case s: Byte  => "Byte"
case s: Double  => "Double"
case s=> "WTF"
}


print(b)
