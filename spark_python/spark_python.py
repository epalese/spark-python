import os
import subprocess
import sys
# import platform
# import atexit

def bootstrap(spark_home):
    # SPARK_HOME="/Users/fix/dev/spark-1.4.1-bin-hadoop2.6"
    SPARK_HOME=spark_home
    os.environ["SPARK_HOME"] = SPARK_HOME
    
    # Run load_spark_env.sh script shipped with the Spark distro and
    # store the environment variables in the current environment
    # http://stackoverflow.com/questions/7040592/calling-the-source-command-from-subprocess-popen
    load_spark_env_path = SPARK_HOME + '/bin/load-spark-env.sh'
    command = 'echo "source ' + load_spark_env_path + '; env" | bash'
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0]
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)

    # Add spark libs to pythonpath
    sys.path.append(SPARK_HOME + '/python/')
    sys.path.append(SPARK_HOME + '/python/lib/py4j-0.8.2.1-src.zip')

    import py4j
    import pyspark

    # TODO: add shell.py initialisation
    # code from the shell.py
    # add_files = None
    # if os.environ.get("ADD_FILES") is not None:
    #    add_files = os.environ.get("ADD_FILES").split(',')