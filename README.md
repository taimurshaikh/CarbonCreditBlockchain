# CarbonCreditBlockchain
Made for Slingshot Open Source Sunday. Uses HyperLedger Fabric to simulate a blockchain network for the trading of carbon credits for firms
# What is a Blockchain?
Blockchain technology was first used in the early 90s to timestamp dates on important documents such that noone could tamper with them. Other than that, the technology was mostly unused. That was until, in 2009, Satoshi Nakamoto invented Bitcoin, the world's most popular cryptocurrency.</br>


In it's simplest terms, Blockchain is a list of transactions stored on a distributed ledger that uses cryptography to ensure the security of the network. Every transaction is made publicly and is verified at multiple points along the network by different 'nodes'.<br/>


A hash function is a mathematical algorithm that encrypts the data in particular 'block' (transaction)</br>


A block stores three components: The hash, The hash of that block's data, as well as the hash of the data of the block before it. This means that a blockchain structure is conducive to a linked list data structure. If someone tries to commit fraud by changing a data value, the hash of that value would change, thus rendering the blockchain useless (as the linked list would be orphaned at the point where the tampering was made)</br>
