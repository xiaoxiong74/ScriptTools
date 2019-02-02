object ApacheLogAnalysis {
  val LOG_ENTRY_PATTERN = "^([\\d.]+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+\\-]\\d{4})\\] \"(\\w+) (\\S+) (\\S+)\" (\\d{3}) (\\S+)".r
  def main(args: Array[String]): Unit = {
    var masterUrl = "local[2]"
    if (args.length > 0) {
      masterUrl = args.apply(0)
    }
    val sparkConf = new SparkConf().setMaster(masterUrl).setAppName("ApacheLogAnalysis")
    val ssc = new StreamingContext(sparkConf,Seconds(5))
    //ssc.checkpoint(".") // 因为使用到了updateStateByKey,所以必须要设置checkpoint
    //主题
    val topics =  Set{ResourcesUtil.getValue(Constants.KAFKA_TOPIC_NAME)}
    //kafka地址
    val brokerList = ResourcesUtil.getValue(Constants.KAFKA_HOST_PORT)
    val kafkaParams = Map[String, String](
      "metadata.broker.list" -> brokerList,
      "serializer.class" -> "kafka.serializer.StringEncoder"
    )
    //连接kafka 创建stream
    val kafkaStream = KafkaUtils.createDirectStream[String, String, StringDecoder, StringDecoder](ssc,kafkaParams,topics)
    val events = kafkaStream.flatMap(line => {
      //正则解析apache log日志
      //192.168.1.249 - - [23/Jun/2017:12:48:43 +0800] "POST /zeus/zeus_platform/user.rpc HTTP/1.1" 200 99
      val LOG_ENTRY_PATTERN(clientip,ident,auth,timestamp,verb,request,httpversion,response,bytes) = line._2
      val logEntryMap = mutable.Map.empty[String,String]
      logEntryMap("clientip") = clientip
      logEntryMap("ident") = ident
      logEntryMap("auth") = auth
      logEntryMap("timestamp") = timestamp
      logEntryMap("verb") = verb
      logEntryMap("request") = request
      logEntryMap("httpversion") = httpversion
      logEntryMap("response") = response
      logEntryMap("bytes") = bytes
      Some(logEntryMap)
    })
    events.print()
    val requestUrls = events.map(x => (x("request"),1L)).reduceByKey(_+_)
    requestUrls.foreachRDD(rdd => {
      rdd.foreachPartition(partitionOfRecords => {
        partitionOfRecords.foreach(pair => {
          val requestUrl = pair._1
          val clickCount = pair._2
          println(s"=================requestUrl count====================  clientip:${requestUrl} clickCount:${clickCount}.")
        })
      })
    })
    ssc.start()
    ssc.awaitTermination()
  }
}
