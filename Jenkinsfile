node {
    agent {
    label 'docker' 
  }

  def myEnv = docker.build 'my-environment:snapshot'
  myEnv.inside {
    sh 'make test'
  }
}