// Create a Huffman tree from a list of characters and their frequencies.
// The tree is represented as a list of nodes, each of which has a character
// and a frequency.  The list is sorted by frequency, with the lowest frequency
// at the front of the list.  The tree is built by combining the two lowest
// frequency nodes into a new node, and inserting the new node into the list
// in sorted order.  The process is repeated until there is only one node in
// the list, which is the root of the tree.
//

#include <iostream>
#include <list>
#include <string>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f, Node *l = 0, Node *r = 0)
        : ch(c), freq(f), left(l), right(r) {}
};

// Insert a node into a list of nodes in sorted order.
void insert(list<Node*> &nodes, Node *node)
{
    list<Node*>::iterator it;
    for (it = nodes.begin(); it != nodes.end(); it++)
        if (node->freq < (*it)->freq)
            break;
    nodes.insert(it, node);
}

// Build a Huffman tree from a list of characters and their frequencies.
Node *buildTree(list<Node*> &nodes)
{
    while (nodes.size() > 1) {
        Node *left = nodes.front();
        nodes.pop_front();
        Node *right = nodes.front();
        nodes.pop_front();
        Node *node = new Node(0, left->freq + right->freq, left, right);
        insert(nodes, node);
    }
    return nodes.front();
}

// Print a Huffman tree.
void printTree(Node *node, string prefix = "")
{
    if (node->ch != 0)
        cout << node->ch << " " << prefix << endl;
    else {
        printTree(node->left, prefix + "0");
        printTree(node->right, prefix + "1");
    }
}

int main()
{
    list<Node*> nodes;
    nodes.push_back(new Node('a', 45));
    nodes.push_back(new Node('b', 13));
    nodes.push_back(new Node('c', 12));
    nodes.push_back(new Node('d', 16));
    nodes.push_back(new Node('e', 9));
    nodes.push_back(new Node('f', 5));
    Node *root = buildTree(nodes);
    printTree(root);
    return 0;
}