import com.vorti.test
import com.vorti.test.{Car, SuperCar}

object Page03 {
  def init(): Unit ={
    println("halla")
    val s = new Emp("아이유",100)

    var s2 = new SuperCar("현대", false, "red")
    print(s2.toString)
  }
  def main(args:Array[String]): Unit = {
//    println("halla")
//    val s = new Emp("아이유",100)
    println(args.toList)
    init()
  }
}
