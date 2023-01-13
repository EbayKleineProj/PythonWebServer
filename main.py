import http.server
import socketserver



def main():
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    git_test = 123
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at {PORT}")
        httpd.serve_forever()
if __name__ == "__main__":
    main()
