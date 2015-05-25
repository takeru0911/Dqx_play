name := """dqx-proj"""

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayJava)

scalaVersion := "2.11.1"

libraryDependencies ++= Seq(
  javaJdbc,
  javaEbean,
  cache,
  javaWs,
  "org.webjars" %% "webjars-play" % "2.3.0-2",
  "org.webjars" % "bootstrap" % "3.1.1-2",
  "org.webjars.bower" % "vue" % "0.11.7",
  "mysql" % "mysql-connector-java" % "5.1.24",
  "org.webjars" % "amcharts" % "3.13.1"
)
