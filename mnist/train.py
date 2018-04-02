from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("mnist", one_hot=True)
print(type(mnist.test.labels))


# x = tf.placeholder(tf.float32, [None, 784]) #使用占位符placeholder，第一维度可指定图片的数量是任意的
# W = tf.Variable(tf.zeros([784,10]))  #初始化权值
# b = tf.Variable(tf.zeros([10]))      #初始化偏置值
# y = tf.nn.softmax(tf.matmul(x,W) + b)  #根据公式计算
# y_ = tf.placeholder("float", [None,10])  #表示实际的分布
# cross_entropy = -tf.reduce_sum(y_*tf.log(y))  #计算损失函数
# train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  #以梯度下降算法最小化损失函数
# init = tf.initialize_all_variables()  #初始化所有变量
# sess = tf.Session()  #定义会话
# sess.run(init)   #初始化会话
#
# for i in range(1000):   #开始训练，循环训练1000次
#     batch_xs, batch_ys = mnist.train.next_batch(10)
#     sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#
# correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))  #评估
# accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))  #将结果转换为浮点数
# print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))#输出nist = input_data.read_data_sets("MNIST_data/", one_hot=True)