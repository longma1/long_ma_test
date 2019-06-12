import datetime
import json

class Node:
    """
    Node class to store data in, nodes of a double linked list
    """
    def __init__(self, data, cachetime: int, key):
        """
        Created the node object
        :param data: the data to be stored
        :param cachetime: time in minutes until this node is considered expired
        :param key: hash key of this object
        """
        self.prev=None
        self.next=None
        self.expire = datetime.datetime.now() + datetime.timedelta(minutes=cachetime)
        self.data=data
        self.key=key

    def expired(self):
        """
        Checks if the current node is expired
        :return: A boolean, if the current node is expired
        """
        if datetime.datetime.now()>self.expire:
            return True
        else:
            return False


class Cache:
    """
    Cache implementation, functions similar to a double linked list object
    """
    def __init__(self, size: int, time:int):
        """
        Creates the cache object
        :param size: the maximum size of the cache queue
        :param time: time until expiring of objects in this queue
        """
        self.directory = {}
        self.cacheTime = time
        self.max_size=size
        self.first=None
        self.last = None
        self.size=0


    def _delete(self, key):
        """
        private function, used as a helper function to delete nodes
        :param key: key of the node to be deleted
        :return: None
        """
        node = self.directory[key]

        previous = node.prev
        after = node.next

        if previous is None and after is None:
            self.first = None
            self.last = None

        elif previous is None:
            after.prev = None
            self.first = after

        elif after is None:
            previous.next = None
            self.last = previous

        else:
            previous.next = after
            after.prev = previous
        del self.directory[key]
        self.size = self.size-1


    def _add(self, node):
        """
        Another helper function, inserts a node into the queue at the beginning
        :param node: the node to be inserted
        :return: None
        """
        if self.size != 0:
            second = self.first
            second.prev = node
            node.next = second
            node.prev = None

            self.first = node
            self.directory[node.key] = node
            self.size = self.size + 1
            if self.size > self.max_size:
                self._pop()
        else:
            self.first = node
            self.directory[node.key] = node
            self.size = self.size + 1
            self.last = node

    def _pop(self):
        """
        removes the least recently used node to make space for more nodes
        :return: None
        """
        removed = self.last
        last = removed.prev

        self.last= last
        last.next = None

        self.size=self.size-1

        del self.directory[removed.key]

    def get(self, key: int):
        """
        searches for data associated with the key
        :param key: key of the data we are looking for
        :return: the object associeted with the key, None if the node expired or if it is not in the cache
        """
        if key in self.directory:
            node = self.directory[key]
            if node.expired():
                self._delete(key)
                return None
            else:
                self._delete(key)
                self._add(node)
                return node.data
        return None


    def add(self, data):
        """
        Creates and inserts a node into the cache
        :param data: the data to be stored
        :return: True, meaningless
        """
        key = hash(data)
        if key in self.directory:
            # if we have the node, delete it
            self._delete(key)
        node = Node(data, self.cacheTime, key)
        self._add(node)
        return True


    def resync(self, cache: str):
        """
        resyncs the data using json string
        :param cache: json string from another server
        :return: None
        """
        cache_dict = json.loads(cache)
        cache_list = cache_dict['cache']
        self.directory={}
        prev = None
        for i in range(len(cache_list)):
            current_node = cache_list[i]
            node = Node(current_node['data'], 0, current_node['key'])
            node.expire=datetime.datetime.strptime(current_node['expire'],"%Y-%m-%d %H:%M:%S.%f")

            self.directory[current_node['key']] = node

            prev = node
            if i == 0:
                self.first = node
            else:
                prev.next = node
                node.prev = prev
        self.last = node


    def to_json(self):
        """
        creates Json string from the cache as of right now
        :return: json representation of the current cache
        """
        #assuming the data object has a json() function if it was a custom object
        cache_list = []
        current = self.first
        if self.first==None:
            return json.dumps({'cache':[]})
        while current != None:
            current_dict = {
                'key':current.key,
                'expire':str(current.expire),
                'data': current.data
                }
            cache_list.append(current_dict)
            current=current.next
        resulting_json = {'cache':cache_list}
        return json.dumps(resulting_json)
