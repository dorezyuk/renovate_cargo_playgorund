import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        for i in range(5):
            self.request.sendall(self.data.upper())
        self.request.sendall(b"")

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


# input [2 ,2, 3, 5, 7]
# output [2, 0, 1, 2, 2]
# step 1 [0, 0, 1, 3, 5]
# step 2 [0, 0, 1, 3, 5]
# step 3 [0, 0, 0, 2, 4]
# step 4 [0, 0, 0, 0, 2]
# step 5 [0, 0, 0, 0, 0]


def foo(output) :
    for i, j in enumerate(output):
        # 5, 4, 3, 2, 1
        reverse_index = len(output) - i 
        # 2 * 5
        # 0 * 4
        # 1 * 3
        # 2 * 2
        # 2 * 1