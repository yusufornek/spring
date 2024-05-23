#What are the main characteristics of Queue and Stack?
#Queue ve Stack'in ana özellikleri nelerdir ve farkları nelerdir?
#Queue: First in First out (FIFO) mantığı ile çalışır. Yani ilk giren eleman ilk çıkar.
#Stack: Last in First out (LIFO) mantığı ile çalışır. Yani son giren eleman ilk çıkar.
#Sınavda stacks, queue ya da buna benzer bir şeyin ne olduğunu nasıl yazıldığını örneği ve fonksiyonları ile yazınız.


from collections import deque
deque()

a = deque(["apple", "grape","peach"])
b = deque("elif")
c = deque([1, 3, 5, 7, 9])

#Both append(0) and pop() add or remove elements from the right side of the linked list.


my_llist = deque("elifkartal")
my_llist
print(my_llist)

my_llist.append("*")
my_llist
print(my_llist)

my_llist.pop()
my_llist
print(my_llist)

my_llist.appendleft("E")
my_llist
print(my_llist)





from collections import deque
my_queue2 = deque()

my_queue2.appendleft("Buttercup")
my_queue2.appendleft("Blossom")
my_queue2.appendleft("Bubbles")
my_queue2.appendleft("Mojo Jojo")
my_queue2
print(my_queue2)

my_queue2.popleft()
my_queue2.popleft()
my_queue2
print(my_queue2)


#Hierarchical data structures
#Hiyerarşik veri yapıları nedir?
#Hiyerarşik veri yapıları, verilerin ağaç yapısında düzenlenmesini sağlayan veri yapılarıdır. Bu yapılar, birbirine bağlı düğümlerden oluşur ve her düğüm, bir veya birden fazla alt düğüm içerebilir. Hiyerarşik veri yapıları, verilerin kategorize edilmesi ve sınıflandırılması için kullanılır. Örnek olarak, ağaç yapısı, dosya sistemleri ve organizasyon şemaları verilebilir.
#Ebeveyn ve çocuk düğümleri ilişkisi vardır. Ebeveyn düğüm, bir veya daha fazla çocuk düğümüne sahip olabilir. Çocuk düğümler, ebeveyn düğüme bağlıdır ve ebeveyn düğümün altında yer alır.
#Binary Tree Search

#Predeccesor and Successor ilişkisi şudur; Predecessor, bir düğümün solundaki en büyük düğümdür. Successor ise bir düğümün sağındaki en küçük düğümdür.
#Family Tree şudur; Aile ağacı, bir kişinin akrabalarını ve soyunu gösteren bir hiyerarşik veri yapısıdır. Bu yapıda, her düğüm bir kişiyi temsil eder ve düğümler arasındaki ilişkiler, aile bağlarına dayanır. Aile ağacı, genellikle soy ağacı olarak da adlandırılır ve bir kişinin atasını, torunlarını, kardeşlerini ve diğer akrabalarını gösterir.

#Yüksekliğe bakarken n-1 kullanılır. Yani 3 düğüm varsa 2 yükseklik olur.

#General Tree ve Binary Tree arasındaki farklar nelerdir?
#Genel ağaçta her düğümün en fazla bir ebeveyni olabilirken, ikili ağaçta her düğümün en fazla iki çocuğu olabilir.

#The shape of binary tree can be vine-like, bushy, or full. The shape of a binary tree is determined by the number of nodes in the tree and the height of the tree.

#KSS : Preorder, Postorder, Inorder, Levelorder nedir, farkları nelerdir?




from binarytree import Node

# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # print function
    def PrintTree(self):
        print(self.data)

    root = Node(30)
    root.left = Node(40)
    root.right = Node(70)

    root.left.left = Node(100)
    root.left.right = Node(200)
        
    #Getting binary tree
    print('Binary tree:', root)
    #Getting list of nodes
    print('List of nodes:', list(root))
    #Getting inorder of nodes
    print('Inorder of nodes:', root.inorder)
    #Checking tree properties
    print('Size of tree:', root.size)

    print('Height of tree:', root.height)


#Get all properties at once
print("Properties of the tree:", root.properties)
root.is_max_heap
root.is_symmetric
root.min_node_value
root.max_node_value

root = Node(100)
root.left = Node(80)
root.left.left=Node(50)
root.left.right = Node(90)

root.right = Node(120)
root.right.left = Node(110)
root.right.right = Node(100)

print("Binary tree:", root)


from binarytree import build

nodes = [30, 60, 80, 20, 110, None, 30 ]

binary_tree = build(nodes)
print("Binary tree from list : \n", binary_tree)
nodes2 = [100, 80, 120, 50, 90, 100, 160]
binary_tree2 = build(nodes2)

print(binary_tree2)



