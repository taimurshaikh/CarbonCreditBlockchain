# CarbonCreditBlockchain
Made for Slingshot Open Source Sunday. Uses HyperLedger Fabric to simulate a blockchain network for the trading of carbon credits for firms
# What is a Blockchain?
Blockchain technology was first used in the early 90s to timestamp dates on important documents such that noone could tamper with them. Other than that, the technology was mostly unused. That was until, in 2009, Satoshi Nakamoto invented Bitcoin, the world's most popular cryptocurrency.</br>


In it's simplest terms, Blockchain is a list of transactions stored on a digital ledger that uses cryptography to ensure the security of the network. Every transaction is made publicly and is verified at multiple points along the network by different 'nodes'. This process is called consensus (further details below)<br/>


A hash function is a mathematical algorithm that encrypts the data in particular 'block' (transaction)</br>


A block stores three components: The hash, The hash of that block's data, as well as the hash of the data of the block before it. This means that a blockchain structure is conducive to a linked list data structure. If someone tries to commit fraud by changing a data value, the hash of that value would change, thus rendering the blockchain useless (as the linked list would be orphaned at the point where the tampering was made)</br>

For Blockchain technology to be used effectively in enterprise, the following criteria should ideally be met:
- Every Blockchain node must be identified/identifiable
- Networks need to be permissioned
- High transaction throughput performance
- Low latency of transaction confirmation
- Privacy and confidentiality of transactions and data pertaining to business transactions

## Distributed Ledger
As described, Blockchain transactions are stored on a distributed ledger. This is a consensus of replicated, shared, and synchronized digital data that is able to be physically spread across a wide geographical area.
## Smart Contracts
Smart contracts can act as a method of regulating control across the ledger. Since the ledger is continually updating, it helps greatly to have a sound method to support this. Enter Smart Contracts. They allow various different operations to be performed on the ledger (such as actually making a transaction, querying the ledger) efficiently and cleanly. Moreover, they can just act as a quality of life improvement by automating repetitive or intensive tasks on the ledger e.g making a calculation of a data value of a new block on a ledger based on one or more variables.
## Consensus
The process of keeping the ledger transactions synchronized across the network — to ensure that ledgers update only when transactions are approved by the appropriate participants, and that when ledgers do update, they update with the same transactions in the same order — is called consensus. This is at the core of every blockchain system.
# What is HyperLedger Fabric?
In its own words, HLF is "an open source enterprise-grade permissioned distributed ledger technology (DLT) platform, designed for use in enterprise contexts, that delivers some key differentiating capabilities over other popular distributed ledger or blockchain platforms."


The main allure of HLF is its modular architecture, which it describes as "plug and play"
# Carbon Credits
In business, carbon credits are 'permits' that allow the firm that owns them to emit a certain amount of CO2 (or other greenhouse gases for the matter). This amount is stipulated by how many credits they have. The more credits a firm has, the more CO2 they can emit. Exceeding their credit limit results in fines that increase the more of a debt they have. Moreover, firms can sell permits off between one another, which allows firms with excess permits to make more profit, as well as firms that are exceeding their limit to minimise costs by reducing fines by gaining more permits. Overall, this incentivises firms to minimise their CO2 outputs such that they can become a firm that can sell their permits and make profit. This is assuming a basic principle of behavioural economics: that firms act rationally. 
