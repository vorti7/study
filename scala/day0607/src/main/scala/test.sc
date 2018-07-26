//val timedUUID = safeStringOp(uuid, {s =>
//  val now = System.currentTimeMillis()
//  val timed = s.take(24) + now
//  timed.toUpperCase
//})
//

def fa(s:String, f:String=>String):String = {
  if(s != null) f(s) else s

}

def fs(s1:String):String = {
  s1.reverse
}

val fss:(String) =>String(s1:String):String = {
  s1.reverse
}

val ss = fa("korea", fs)

print(ss)


val sd = fa("홍길동")( _.reverse)