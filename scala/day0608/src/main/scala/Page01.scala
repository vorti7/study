class Page01 {
  def main(args:Array[String]): Unit ={
    val emp1 = new Emp(name = "홍길동", salary = 200)
    val empList = List(new Emp(name = "홍길동", salary = 340),
      new Emp(name = "김벌레", salary = 10),
      new Emp(name = "박사기꾼", salary = 1000),
      new Emp(name = "노보통", salary = 440))

    empList.sortBy(_.salary).foreach(println(_))
//    for(emp<- empList){
//      print(emp)
//    }
  }
}
