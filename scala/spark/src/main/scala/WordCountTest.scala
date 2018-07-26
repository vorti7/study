import java.util.Arrays
import org.apache.spark.{SparkContext, SparkConf}
import org.scalatest.FlatSpec
import scala.collcetion.mutable.ListBuffer
import org.junit.Test

class WordCountSpec{

  @Test
  def Test(): Unit ={
    val conf = new SparkConf()
    conf.setMaster("local[*]").setAppName("WordCountTest")

    val sc = new SparkContext(conf)
    val input = new ListBuffer[String]
    input += "Apache Spark is a fast and general engine for large-scale data processing."
    input += "Spark runs on both Windows and UNIX-like systems"
    input.toList

    val inputRDD = sc.parallelize(input)
    val resultRDD = WordCount.process(inputRDD)
    val inputRDD = RexultRDD.collecAsMap

    assert(resultMap("spark")==2)
    assert(resultMap("and")==2)
    assert(resultMap("runs")==1)

    println(resultMap)

    sc.stop

  }
}
