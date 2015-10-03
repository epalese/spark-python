# spark-python
Recipes for using Spark with Python

import os
import subprocess
import sys
import atexit
import platform


SPARK_HOME="/Users/fix/dev/spark-1.4.1-bin-hadoop2.6"
os.environ["SPARK_HOME"] = SPARK_HOME
load_spark_env_path = SPARK_HOME + '/bin/load-spark-env.sh'
# http://stackoverflow.com/questions/7040592/calling-the-source-command-from-subprocess-popen
command = 'echo "source ' + load_spark_env_path + '; env" | bash'
pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output = pipe.communicate()[0]
env = dict((line.split("=", 1) for line in output.splitlines()))
os.environ.update(env)
sys.path.append(SPARK_HOME + '/python/')
sys.path.append(SPARK_HOME + '/python/lib/py4j-0.8.2.1-src.zip')

import atexit
import py4j
import pyspark

add_files = None
if os.environ.get("ADD_FILES") is not None:
    add_files = os.environ.get("ADD_FILES").split(',')
