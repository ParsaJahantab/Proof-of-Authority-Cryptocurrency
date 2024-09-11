
# 💸 Proof of Authority Cryptocurrency

A **cryptocurrency** implementation using **Proof of Authority (PoA)** in **Python**, where transactions are validated and propagated through a network of **Authority Nodes** and **Cryptocurrency Nodes**. The system ensures transaction integrity, prevents double-spending, and distributes tokens among clients via socket-based communication.

---

## 🛠️ How It Works

1. **Authority Nodes & Cryptocurrency Nodes**  
   - Two types of nodes: **Authority Nodes** validate transactions, and **Cryptocurrency Nodes** store the blockchain and prevent double-spending.

2. **Client Transactions**  
   - Clients create and sign transactions, which are sent to an **Authority Node**.

3. **Validation Process**  
   - The **Authority Node** checks if the transaction is valid by verifying the client’s balance and signature.
   - If valid, the transaction is stored in the **mempool**.

4. **Transaction Propagation**  
   - The transaction is propagated to neighboring nodes, distributing tokens to connected clients.
     ![image](https://github.com/user-attachments/assets/6e928dfe-88ec-4ff4-9646-50d371e8ba6c)


5. **Token Burning**  
   - If there aren’t enough clients to distribute tokens, excess tokens are **burned**.
     ![image](https://github.com/user-attachments/assets/ec6cd240-d8a2-49f6-a63b-ddd2299e03b6)


6. **Balance Checking**  
   - Clients can check their balances by querying the blockchain of their **neighboring Authority Nodes**.
     ![image](https://github.com/user-attachments/assets/d2de39ce-fa27-4551-b5b5-ae8c3242d0eb)


7. **Double-Spend Prevention**  
   - **Cryptocurrency Nodes** ensure no double-spending or duplicate transactions.

8. **Blockchain Storage**  
   - Transactions are propagated across the network, with each node storing the transaction in its **blockchain**.

9. **Socket Communication**  
   - All communication between clients and nodes happens through **sockets** for fast and reliable transaction propagation.

---

## 🚀 Features

- **Proof of Authority**  
   Transactions are validated by trusted **Authority Nodes** before being broadcasted to the network.
  
- **Socket-Based Networking**  
   Uses sockets for efficient communication between clients and nodes.

- **Double-Spend Prevention**  
   **Cryptocurrency Nodes** enforce double-spending protection and prevent transaction duplication.

- **Token Management**  
   If tokens cannot be distributed, they are **burned**, ensuring proper token circulation.

- **Balance Checking**  
   Clients can query the blockchain of their neighboring **Authority Nodes** to check their balances.

- **Blockchain Storage**  
   Each node maintains a **blockchain** where all valid transactions are stored.

