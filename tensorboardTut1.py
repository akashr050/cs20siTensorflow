"""
Author: Akash Rastogi
Date: 7/25/17
"""
import tensorflow as tf

tbLogDir = "./graphs/"

a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
c = tf.add(a, b, name='add')
with tf.Session() as sess:
    writer = tf.summary.FileWriter(tbLogDir, sess.graph)
    print(sess.run(c))
