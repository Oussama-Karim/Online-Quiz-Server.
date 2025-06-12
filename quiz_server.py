import socket

HOST = '127.0.0.1'
PORT = 65432

questions = [
    ("What is the capital of France?", "paris"),
    ("What is 2 + 2?", "4"),
    ("Who wrote 'Hamlet'?", "shakespeare"),
    ("What is the chemical symbol for water?", "h2o"),
    ("What is the largest planet in our solar system?", "jupiter"),
]

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Quiz server running on {HOST}:{PORT}...")

        conn, addr = server.accept()
        with conn:
            print(f"Client connected: {addr}")
            score = 0

            for q, a in questions:
                conn.sendall(q.encode())
                client_answer = conn.recv(1024).decode().strip().lower()

                if client_answer == a:
                    score += 1
                    conn.sendall(b"Correct!\n")
                else:
                    conn.sendall(f"Wrong! Correct answer was: {a}\n".encode())

            result = f"Quiz finished! Your score is {score}/{len(questions)}\n"
            conn.sendall(result.encode())

if __name__ == "__main__":
    start_server()
