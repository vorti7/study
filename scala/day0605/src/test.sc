//def a() ={
//  println("a")
//  "aa"
//}
//
//def fn2(v : Int*): Unit = {
//  for(a<-v) print(a)
//  "a"
//}
//
//var input = fn2(1)
//input = fn2(1,2,3)
//input = fn2(1,2,3,4,5)
//print(input)
//
//
//def fn3(a:Int)(b:String) = {
//  a + b
//}
//var x = fn3(3)("korea")
//

//var s= "korea, japan, usa"
//var str = s split ", "
//
//print(str)
//
////val ss = s.substring()
//
//var ss = s substring(3,8)
//ss = s.substring(3,8)
//
//val fff: = (Int) =Int = f



def aa(url:String, f1:String=>String, f2:String=>String) = {
  var text = ""
  if(url = "http://m.naver.com"){
    val = "dsafdsadsagadsfdsaf"
    f1(val)
  }else {
    f2()
  }
}

def success()={

}
def fail()={

}
val result = aa("http://m.naver.com")