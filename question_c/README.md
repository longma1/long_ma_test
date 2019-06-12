#Question C

LRU cache implementation using double linked list and hash table for constant time lookup/insertion/deletion.

To start an instance of the cache, using the function
>Cache(size, time)

where size is an integer to specify the max size of the cache, time is an integer to specify how long until
a cache is considered expired from the time it is inserted. and country is the country code of where the server is located for
geo location purposes. For example for a server with max size of 10 and an expiring time of 20 minutes, we would call
>cache = Cache(10,20)

To add an object to the cache, use the function
>cache.add(obj)

This function will created a hash key using the built in function hash(obj) and create a cache node that will expire
in the previously stated amount of time.

To access a node from hash key, the function 
>cache.get(key)

is called, this will fetch the data and place it infront of the cache queue in linear time, returning the object cached
if it has not expired, if it has expired, it is removed and a None type is returned.

To run the test, run the command
>python -m unittest test_question_a.py

####Note:

To be honest the requirements are kinda confusing to me, depending on the 
interpretation and the system design my library could be completely off.   
The implementation I thought of to satisfy requirement #5,
>Locality of reference, data should almost always be available from the closest region 

was to have multiple cache servers that host the same cache in different countries.
On access of a existing node/data that is not expired. the server where it was accessed would send out http requests to
the other servers that would alert the other servers of the data access and put it infront of the cache/ linked list.

On network failure at a server, the other servers that would continue to update each-other, keeping in mind which server
was unable to be updated ie keep track of request response code, when the network is restored, the other servers would
update the entire cache of the previously offline server to the most current cache, using the function to_json() to formulate
the cache to json, which the server at the other end would reload based on the order of the json file using the function resync(cache)
, cache being the json sent as a string. Note that, the to_json function expects the object stored can be converted to string
to send as Json.

Also the test takes atleast 1 minute to run, to test expire functionality when resyn-ing.
