#!/usr/bin/env python3
"""Simple HTTP server for design previews with live reload."""
import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving designs at http://localhost:{port}")
        print(f"  - Professional:   http://localhost:{port}/style-professional/")
        print(f"  - Technical:      http://localhost:{port}/style-technical/")
        print(f"  - Pastoral:       http://localhost:{port}/style-pastoral/")
        print(f"  - Farmyard:       http://localhost:{port}/style-farmyard/")
        print(f"  - Tech-Pastoral:  http://localhost:{port}/style-tech-pastoral/")
        print("\nPress Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")
