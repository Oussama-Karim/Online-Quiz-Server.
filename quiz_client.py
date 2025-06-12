import socket

HOST = '127.0.0.1'
PORT = 65432

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        for _ in range(5):  # expecting 5 questions
            question = client.recv(1024).decode()
            print("Question:", question)

            answer = input("Your answer: ")
            client.sendall(answer.encode())

            feedback = client.recv(1024).decode()
            print("Server:", feedback)

        final_score = client.recv(1024).decode()
        print("Server:", final_score)

if __name__ == "__main__":
    start_client()
